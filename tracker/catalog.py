from __future__ import annotations

import re
from datetime import date
from pathlib import Path
from typing import Any

from tracker.database import ROOT, atomic_write_json, read_json

NUMBERED_PYTHON = re.compile(r"^(?P<number>\d{4})_(?P<title>.+)\.py$")


def _slug(value: str, separator: str = "-") -> str:
    normalized = re.sub(r"[^a-z0-9]+", separator, value.casefold()).strip(separator)
    return normalized or "untitled"


def _header_value(content: str, label: str) -> str | None:
    match = re.search(
        rf"(?im)^\s*(?:#|--)?\s*{re.escape(label)}\s*:\s*(?P<value>.+?)\s*$",
        content,
    )
    return match.group("value").strip() if match else None


def _display_title(path: Path, content: str, numbered_title: str | None = None) -> str:
    header_title = _header_value(content, "Title")
    if header_title and header_title.casefold() != "todo":
        return header_title
    return (numbered_title or path.stem).replace("_", " ").strip().title()


def _difficulty(content: str) -> str:
    value = (_header_value(content, "Difficulty") or "medium").casefold()
    return value if value in {"easy", "medium", "hard"} else "medium"


def _pattern(content: str, fallback: str) -> str:
    value = _header_value(content, "Primary Pattern")
    if not value or value.casefold() == "todo":
        return fallback
    return _slug(value, separator="_")


def _base_record(
    *,
    identifier: str,
    title: str,
    source: str,
    category: str,
    pattern: str,
    difficulty: str,
    relative_path: str,
    leetcode_number: int | None,
    phase: str,
) -> dict[str, Any]:
    today = date.today().isoformat()
    return {
        "id": identifier,
        "leetcode_number": leetcode_number,
        "title": title,
        "slug": _slug(title),
        "source": source,
        "category": category,
        "primary_pattern": pattern,
        "secondary_patterns": [],
        "difficulty": difficulty,
        "phase": phase,
        "file_path": relative_path,
        "status": "not_started",
        "confidence": 1,
        "attempts": 0,
        "completed_without_help": False,
        "last_practiced": None,
        "next_review": None,
        "average_minutes": 0,
        "best_minutes": None,
        "mistake_tags": [],
        "notes": "Auto-discovered from the public solution catalog.",
        "created_at": today,
        "updated_at": today,
    }


def _python_record(path: Path, root: Path) -> dict[str, Any]:
    relative = path.relative_to(root).as_posix()
    content = path.read_text(encoding="utf-8")
    category_path = path.parent.relative_to(root / "leetcode_python")
    category = "_".join(category_path.parts) or "python"
    numbered = NUMBERED_PYTHON.match(path.name)
    if numbered:
        number = int(numbered.group("number"))
        title = _display_title(path, content, numbered.group("title"))
        return _base_record(
            identifier=f"leetcode-{number:04d}",
            title=title,
            source="leetcode",
            category=category,
            pattern=_pattern(content, category),
            difficulty=_difficulty(content),
            relative_path=relative,
            leetcode_number=number,
            phase="Phase A",
        )

    title = _display_title(path, content)
    return _base_record(
        identifier=f"custom-{_slug(category)}-{_slug(path.stem)}",
        title=title,
        source="custom",
        category=category,
        pattern=_pattern(content, category),
        difficulty=_difficulty(content),
        relative_path=relative,
        leetcode_number=None,
        phase="Phase B",
    )


def _sql_record(path: Path, root: Path) -> dict[str, Any]:
    relative = path.relative_to(root).as_posix()
    content = path.read_text(encoding="utf-8")
    category_path = path.parent.relative_to(root / "sql")
    section = "_".join(category_path.parts) or "fundamentals"
    category = f"sql_{section}"
    title = _display_title(path, content)
    identifier_path = path.relative_to(root / "sql").with_suffix("")
    identifier = "sql-" + "-".join(_slug(part) for part in identifier_path.parts)
    return _base_record(
        identifier=identifier,
        title=title,
        source="sql",
        category=category,
        pattern=_pattern(content, section),
        difficulty=_difficulty(content),
        relative_path=relative,
        leetcode_number=None,
        phase="Phase C",
    )


def discover_catalog(root: Path = ROOT) -> list[dict[str, Any]]:
    """Return metadata inferred from public Python and SQL solution files."""
    records: list[dict[str, Any]] = []
    python_root = root / "leetcode_python"
    if python_root.is_dir():
        records.extend(
            _python_record(path, root)
            for path in sorted(python_root.rglob("*.py"))
            if path.name != "__init__.py"
        )
    sql_root = root / "sql"
    if sql_root.is_dir():
        records.extend(_sql_record(path, root) for path in sorted(sql_root.rglob("*.sql")))
    return records


def sync_catalog(
    root: Path = ROOT,
    questions_path: Path | None = None,
) -> dict[str, Any]:
    """Add unregistered public solutions without changing existing tracker state."""
    destination = questions_path or root / "tracker/questions.json"
    questions = read_json(destination, [])
    if not isinstance(questions, list):
        raise ValueError(f"{destination} must contain a list")

    registered_paths = {question.get("file_path") for question in questions}
    registered_ids = {question.get("id"): question.get("file_path") for question in questions}
    added: list[dict[str, Any]] = []
    conflicts: list[str] = []

    for candidate in discover_catalog(root):
        if candidate["file_path"] in registered_paths:
            continue
        if candidate["id"] in registered_ids:
            conflicts.append(
                f"{candidate['file_path']} conflicts with {registered_ids[candidate['id']]}"
            )
            continue
        questions.append(candidate)
        added.append(candidate)
        registered_paths.add(candidate["file_path"])
        registered_ids[candidate["id"]] = candidate["file_path"]

    if added:
        atomic_write_json(destination, questions)
    return {"added": added, "conflicts": conflicts, "total": len(questions)}
