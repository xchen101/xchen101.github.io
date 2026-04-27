"""Parse Claude's tagged response and publish the post to the Jekyll repo."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


_FRONTMATTER_RE = re.compile(r"<frontmatter>\s*(.*?)\s*</frontmatter>", re.DOTALL | re.IGNORECASE)
_POST_RE = re.compile(r"<post>\s*(.*?)\s*</post>", re.DOTALL | re.IGNORECASE)
_NOTES_RE = re.compile(r"<notes>\s*(.*?)\s*</notes>", re.DOTALL | re.IGNORECASE)


class ResponseParseError(Exception):
    """Raised when Claude's response cannot be parsed."""

    def __init__(self, message: str, raw_response: str):
        super().__init__(message)
        self.raw_response = raw_response


def parse_response(response: str) -> dict:
    fm_match = _FRONTMATTER_RE.search(response)
    post_match = _POST_RE.search(response)
    notes_match = _NOTES_RE.search(response)

    if not fm_match or not post_match:
        missing = []
        if not fm_match:
            missing.append("<frontmatter>")
        if not post_match:
            missing.append("<post>")
        raise ResponseParseError(
            f"Missing required tags in Claude response: {', '.join(missing)}",
            response,
        )

    frontmatter = _parse_frontmatter_block(fm_match.group(1))
    post = post_match.group(1).strip("\n")
    notes = notes_match.group(1).strip() if notes_match else ""

    return {"frontmatter": frontmatter, "post": post, "notes": notes}


def _parse_frontmatter_block(text: str) -> dict:
    result: dict = {}
    for line in text.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, _, value = line.partition(":")
        result[key.strip()] = value.strip()
    return result


def publish(frontmatter: dict, post: str, note_name: str, config: dict) -> Path:
    date = frontmatter.get("date", "").strip()
    if not date:
        raise ValueError("Frontmatter is missing a date")

    filename = f"{date}-{note_name}.md"
    posts_dir = REPO_ROOT / "_posts"
    posts_dir.mkdir(exist_ok=True)
    out_path = posts_dir / filename

    content = _build_post_file(frontmatter, post)
    out_path.write_text(content, encoding="utf-8")

    rel_path = out_path.relative_to(REPO_ROOT).as_posix()
    title = frontmatter.get("title", note_name)
    _git_publish(rel_path, title)
    return out_path


def _build_post_file(frontmatter: dict, post: str) -> str:
    title = frontmatter.get("title", "").strip()
    date = frontmatter.get("date", "").strip()
    tags = frontmatter.get("tags", "").strip()
    description = frontmatter.get("description", "").strip()
    model = frontmatter.get("model", "").strip()

    lines = [
        "---",
        "layout: post",
        f"title: {_yaml_quote(title)}",
        f"date: {date}",
        f"tags: [{tags}]",
        f"description: {_yaml_quote(description)}",
        f"model: {_yaml_quote(model)}",
        "---",
        "",
        post.rstrip() + "\n",
    ]
    return "\n".join(lines)


def _yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _git_publish(rel_path: str, title: str) -> None:
    commit_message = f"publish: {title}"
    _run_git(["git", "add", rel_path])
    _run_git(["git", "commit", "-m", commit_message])
    _run_git(["git", "push"])


def _run_git(cmd: list[str]) -> None:
    try:
        subprocess.run(
            cmd,
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        print("git not found in PATH. Install git and retry.", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as exc:
        print(f"git command failed: {' '.join(cmd)}", file=sys.stderr)
        if exc.stdout:
            print(exc.stdout, file=sys.stderr)
        if exc.stderr:
            print(exc.stderr, file=sys.stderr)
        sys.exit(exc.returncode or 1)
