"""Read and clean Obsidian notes for the publish pipeline."""

from __future__ import annotations

import re
import sys
from datetime import date, datetime
from pathlib import Path

try:
    import yaml  # type: ignore

    _HAS_YAML = True
except ImportError:
    _HAS_YAML = False


_FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)


def extract(note_name: str, config: dict) -> dict:
    vault_path = Path(config["vault_path"]).expanduser()
    publish_folder = config.get("publish_folder", "")
    note_path = vault_path / publish_folder / f"{note_name}.md"

    if not note_path.exists():
        raise FileNotFoundError(f"Note not found: {note_path}")

    raw = note_path.read_text(encoding="utf-8")
    frontmatter, body = _split_frontmatter(raw)

    title = _resolve_title(frontmatter, note_name, body)
    tags = _resolve_tags(frontmatter)
    note_date = _resolve_date(frontmatter, note_path)
    content = _clean_obsidian_syntax(body)

    return {
        "title": title,
        "tags": tags,
        "date": note_date,
        "content": content,
    }


def _split_frontmatter(raw: str) -> tuple[dict, str]:
    match = _FRONTMATTER_RE.match(raw)
    if not match:
        return {}, raw
    fm_text = match.group(1)
    body = raw[match.end():]
    return _parse_frontmatter(fm_text), body


def _parse_frontmatter(text: str) -> dict:
    if _HAS_YAML:
        try:
            data = yaml.safe_load(text) or {}
            return data if isinstance(data, dict) else {}
        except yaml.YAMLError:
            return _parse_frontmatter_simple(text)
    return _parse_frontmatter_simple(text)


def _parse_frontmatter_simple(text: str) -> dict:
    """Minimal key: value parser for when PyYAML is unavailable.

    Handles scalar strings, inline lists [a, b, c], and multi-line dash lists."""
    result: dict = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value == "" and i + 1 < len(lines) and lines[i + 1].lstrip().startswith("- "):
            items: list[str] = []
            j = i + 1
            while j < len(lines) and lines[j].lstrip().startswith("- "):
                items.append(lines[j].lstrip()[2:].strip().strip('"').strip("'"))
                j += 1
            result[key] = items
            i = j
            continue
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1]
            result[key] = [
                v.strip().strip('"').strip("'")
                for v in inner.split(",")
                if v.strip()
            ]
        else:
            result[key] = value.strip('"').strip("'")
        i += 1
    return result


_H1_RE = re.compile(r"^#\s+(.+?)\s*#*\s*$", re.MULTILINE)


def _resolve_title(fm: dict, note_name: str, body: str) -> str:
    title = fm.get("title")
    if title:
        return str(title).strip()
    h1 = _H1_RE.search(body)
    if h1:
        return h1.group(1).strip()
    return note_name.replace("-", " ").replace("_", " ").strip().title()


def _resolve_tags(fm: dict) -> str:
    tags = fm.get("tags")
    if tags is None:
        return ""
    if isinstance(tags, list):
        return ", ".join(str(t).strip() for t in tags if str(t).strip())
    if isinstance(tags, str):
        # comma-separated or space-separated; normalize on commas
        if "," in tags:
            return ", ".join(t.strip() for t in tags.split(",") if t.strip())
        return ", ".join(t.strip() for t in tags.split() if t.strip())
    return str(tags)


def _resolve_date(fm: dict, note_path: Path) -> str:
    raw = fm.get("date")
    if raw:
        if isinstance(raw, (date, datetime)):
            return raw.strftime("%Y-%m-%d") if isinstance(raw, date) else raw.date().isoformat()
        text = str(raw).strip()
        # accept full ISO timestamps; keep just the date portion
        if len(text) >= 10 and text[4] == "-" and text[7] == "-":
            return text[:10]
        return text
    try:
        mtime = note_path.stat().st_mtime
        return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
    except OSError:
        return date.today().isoformat()


def _clean_obsidian_syntax(content: str) -> str:
    # Dataview blocks → remove
    content = re.sub(
        r"```dataview\b.*?```\s*\n?",
        "",
        content,
        flags=re.DOTALL,
    )

    # %%comments%% → remove (can span lines)
    content = re.sub(r"%%.*?%%", "", content, flags=re.DOTALL)

    # ![[embedded note]] → remove + warn
    def _embed_warn(match: re.Match) -> str:
        print(
            f"warning: dropped embedded note reference {match.group(0)}",
            file=sys.stderr,
        )
        return ""

    content = re.sub(r"!\[\[([^\]]+)\]\]", _embed_warn, content)

    # [[page|display text]] → display text
    content = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", content)

    # [[page]] → page (strip optional #anchor or ^block-id from the displayed text)
    def _wikilink(match: re.Match) -> str:
        target = match.group(1)
        # drop anchor/block portion for the visible label
        for sep in ("#", "^"):
            if sep in target:
                target = target.split(sep, 1)[0]
        return target.strip() or match.group(0)

    content = re.sub(r"\[\[([^\]]+)\]\]", _wikilink, content)

    # Obsidian callout headers — drop the "[!type] title" line, keep nested "> content"
    content = re.sub(
        r"^[ \t]*>[ \t]*\[![^\]]+\][^\n]*\n?",
        "",
        content,
        flags=re.MULTILINE,
    )

    # Inline #tags → strip the leading # (leave heading markers and intra-word # alone)
    content = _strip_inline_tags(content)

    return content


def _strip_inline_tags(text: str) -> str:
    pattern = re.compile(r"#(\w+)")

    def replace(match: re.Match) -> str:
        start = match.start()
        if start == 0:
            return match.group(0)
        prev = text[start - 1]
        if prev == "\n":
            return match.group(0)
        if prev == "#" or prev.isalnum() or prev == "_":
            return match.group(0)
        return match.group(1)

    return pattern.sub(replace, text)
