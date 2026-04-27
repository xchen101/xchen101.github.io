"""CLI entry point: rewrite an Obsidian note into a blog post and publish it."""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

import extractor
import formatter

try:
    import yaml  # type: ignore

    _HAS_YAML = True
except ImportError:
    _HAS_YAML = False


SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = SCRIPT_DIR / "config.yaml"
PROMPT_PATH = SCRIPT_DIR / "prompts" / "rewrite.md"
SEPARATOR = "═" * 56


def main() -> int:
    # Windows consoles default to cp1252, which can't encode the box-drawing
    # separator. Reconfigure stdio to UTF-8 where supported.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")

    args = _parse_args()
    config = _load_config(CONFIG_PATH)
    _validate_paths(config)

    note_path = (
        Path(config["vault_path"]).expanduser()
        / config.get("publish_folder", "")
        / f"{args.note_name}.md"
    )
    print(f"Reading: {note_path}")

    extracted = extractor.extract(args.note_name, config)

    print(f"Rewriting with {config['model']}...")
    system_prompt, user_template = _load_prompt_template(PROMPT_PATH)

    feedback_log: list[str] = []
    guidance = args.guidance

    while True:
        edited = False

        user_prompt = _build_user_prompt(
            user_template,
            extracted=extracted,
            guidance=guidance,
            model=config["model"],
            feedback_log=feedback_log,
        )
        raw_response = _call_claude(system_prompt, user_prompt, config["model"])

        try:
            parsed = formatter.parse_response(raw_response)
        except formatter.ResponseParseError as exc:
            print(f"\nError: {exc}", file=sys.stderr)
            print("\n--- raw response ---", file=sys.stderr)
            print(exc.raw_response, file=sys.stderr)
            print("--- end raw response ---\n", file=sys.stderr)
            choice = _prompt_choice(
                "[r] retry  [q] quit",
                {"r", "q"},
            )
            if choice == "q":
                return 1
            feedback = input("Feedback for retry (optional): ").strip()
            if feedback:
                feedback_log.append(feedback)
            continue

        post_body = parsed["post"]
        display = _append_transparency_footer(
            post_body, user_prompt, config["model"], edited
        )
        _print_draft(parsed["frontmatter"], display, parsed["notes"])

        choice = _prompt_choice(
            "[y] publish  [e] edit in $EDITOR  [r] retry with feedback  [q] quit",
            {"y", "e", "r", "q"},
        )

        if choice == "q":
            print("Quit without publishing.")
            return 0

        if choice == "r":
            feedback = input("Feedback for Claude: ").strip()
            if not feedback:
                print("Empty feedback — retrying anyway.")
            feedback_log.append(feedback)
            continue

        if choice == "e":
            post_body = _edit_in_editor(post_body)
            edited = True

        final_post = _append_transparency_footer(
            post_body, user_prompt, config["model"], edited
        )

        out_path = formatter.publish(
            parsed["frontmatter"],
            final_post,
            args.note_name,
            config,
        )
        rel = out_path.relative_to(formatter.REPO_ROOT).as_posix()
        print(f"\nPublished: {rel}")
        print("Committed and pushed.")
        return 0


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rewrite an Obsidian note into a Jekyll blog post and publish it.",
    )
    parser.add_argument(
        "note_name",
        help="Note filename without .md (resolved under vault_path/publish_folder/)",
    )
    parser.add_argument(
        "--guidance",
        default=None,
        help="Optional author guidance passed to the rewrite prompt",
    )
    return parser.parse_args()


def _load_config(path: Path) -> dict:
    if not path.exists():
        print(f"Config not found: {path}", file=sys.stderr)
        sys.exit(1)
    text = path.read_text(encoding="utf-8")
    if _HAS_YAML:
        try:
            data = yaml.safe_load(text) or {}
            if not isinstance(data, dict):
                raise ValueError("config.yaml must be a mapping")
            return data
        except yaml.YAMLError as exc:
            print(f"Failed to parse config.yaml: {exc}", file=sys.stderr)
            sys.exit(1)
    return _parse_simple_yaml(text)


def _parse_simple_yaml(text: str) -> dict:
    result: dict = {}
    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip() or ":" not in line:
            continue
        key, _, value = line.partition(":")
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def _validate_paths(config: dict) -> None:
    if "vault_path" not in config:
        print("config.yaml is missing 'vault_path'", file=sys.stderr)
        sys.exit(1)

    vault = Path(config["vault_path"]).expanduser()
    if not vault.exists():
        print(f"Vault path does not exist: {vault}", file=sys.stderr)
        sys.exit(1)

    publish_folder = config.get("publish_folder", "")
    pub_dir = vault / publish_folder
    if not pub_dir.exists():
        print(f"Publish folder does not exist: {pub_dir}", file=sys.stderr)
        sys.exit(1)

    if not PROMPT_PATH.exists():
        print(f"Prompt template not found: {PROMPT_PATH}", file=sys.stderr)
        sys.exit(1)


def _load_prompt_template(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")

    sys_match = re.search(
        r"##\s*System prompt\s*\n(.*?)\n---\s*\n##\s*User prompt",
        text,
        re.DOTALL,
    )
    if not sys_match:
        raise ValueError(
            f"Could not locate '## System prompt' section in {path}"
        )
    system_prompt = sys_match.group(1).strip()

    user_match = re.search(
        r"##\s*User prompt\s*\n+```[^\n]*\n(.*?)\n```",
        text,
        re.DOTALL,
    )
    if not user_match:
        raise ValueError(
            f"Could not locate '## User prompt' code fence in {path}"
        )
    user_template = user_match.group(1)

    return system_prompt, user_template


def _build_user_prompt(
    template: str,
    *,
    extracted: dict,
    guidance: str | None,
    model: str,
    feedback_log: list[str],
) -> str:
    title = extracted.get("title", "")
    tags = extracted.get("tags", "")
    note_date = extracted.get("date") or date.today().isoformat()
    note_content = extracted.get("content", "").strip()

    body = template
    body = _resolve_guidance_block(body, guidance)

    substitutions = {
        "title": title,
        "tags": tags,
        "date": note_date,
        "note_content": note_content,
        "model": model,
        "author_guidance": guidance or "",
    }
    for key, value in substitutions.items():
        body = body.replace(f"{{{{{key}}}}}", str(value))

    if feedback_log:
        appended = "\n\n".join(
            f"**Author feedback on previous draft**: {entry}"
            for entry in feedback_log
        )
        body = f"{body}\n\n{appended}"

    return body


def _resolve_guidance_block(template: str, guidance: str | None) -> str:
    if guidance:
        # keep block contents, drop the markers
        template = re.sub(
            r"\{\{#if author_guidance\}\}\s*\n?",
            "",
            template,
        )
        template = re.sub(
            r"\n?\{\{/if\}\}\s*\n?",
            "\n",
            template,
        )
        return template
    # remove block entirely
    return re.sub(
        r"\{\{#if author_guidance\}\}.*?\{\{/if\}\}\s*\n?",
        "",
        template,
        flags=re.DOTALL,
    )


def _call_claude(system_prompt: str, user_prompt: str, model: str) -> str:
    claude_path = shutil.which("claude")
    if not claude_path:
        print(
            "Claude Code CLI not found. Install it: "
            "https://docs.anthropic.com/en/docs/claude-code",
            file=sys.stderr,
        )
        sys.exit(1)

    base_cmd = [
        claude_path,
        "-p",
        user_prompt,
        "--output-format",
        "text",
        "--model",
        model,
    ]

    if _claude_supports_system_prompt(claude_path):
        cmd = base_cmd + ["--system-prompt", system_prompt]
    else:
        combined = f"{system_prompt}\n\n---\n\n{user_prompt}"
        cmd = [
            claude_path,
            "-p",
            combined,
            "--output-format",
            "text",
            "--model",
            model,
        ]

    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            stdin=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as exc:
        print(f"claude -p failed (exit {exc.returncode})", file=sys.stderr)
        if exc.stderr:
            print(exc.stderr, file=sys.stderr)
        sys.exit(exc.returncode or 1)

    return result.stdout


_SYSTEM_PROMPT_SUPPORT_CACHE: bool | None = None


def _claude_supports_system_prompt(claude_path: str) -> bool:
    global _SYSTEM_PROMPT_SUPPORT_CACHE
    if _SYSTEM_PROMPT_SUPPORT_CACHE is not None:
        return _SYSTEM_PROMPT_SUPPORT_CACHE
    try:
        help_result = subprocess.run(
            [claude_path, "--help"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=10,
            stdin=subprocess.DEVNULL,
        )
        combined = (help_result.stdout or "") + (help_result.stderr or "")
        _SYSTEM_PROMPT_SUPPORT_CACHE = "--system-prompt" in combined
    except (subprocess.SubprocessError, OSError):
        _SYSTEM_PROMPT_SUPPORT_CACHE = False
    return _SYSTEM_PROMPT_SUPPORT_CACHE


def _append_transparency_footer(
    post: str, user_prompt: str, model: str, edited: bool
) -> str:
    edit_clause = ", with manual edits by the author" if edited else ""
    label = (
        f"<em>This post was rewritten from a note using {html.escape(model)}"
        f"{edit_clause}. The prompt used:</em>"
    )
    escaped_prompt = html.escape(user_prompt)
    footer = (
        '\n\n<div class="transparency-footer" markdown="0">\n'
        f'<p class="transparency-label">{label}</p>\n'
        '<pre class="transparency-prompt">\n'
        f"{escaped_prompt}\n"
        "</pre>\n"
        "</div>\n"
    )
    return post.rstrip() + footer


def _print_draft(frontmatter: dict, post: str, notes: str) -> None:
    title = frontmatter.get("title", "(untitled)")
    print()
    print(SEPARATOR)
    print(f"DRAFT: {title}")
    print(SEPARATOR)
    print()
    print(post)
    print()
    print(SEPARATOR)
    if notes:
        print()
        print("Notes from Claude:")
        print(notes)
    print()


def _prompt_choice(prompt: str, valid: set[str]) -> str:
    while True:
        print(prompt)
        choice = input("> ").strip().lower()
        if choice in valid:
            return choice
        print(f"Please choose one of: {', '.join(sorted(valid))}")


def _edit_in_editor(content: str) -> str:
    editor = os.environ.get("EDITOR") or ("notepad" if os.name == "nt" else "vim")
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".md",
        delete=False,
        encoding="utf-8",
    ) as tmp:
        tmp.write(content)
        tmp_path = tmp.name
    try:
        subprocess.run([editor, tmp_path], check=True)
        return Path(tmp_path).read_text(encoding="utf-8")
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


if __name__ == "__main__":
    sys.exit(main())
