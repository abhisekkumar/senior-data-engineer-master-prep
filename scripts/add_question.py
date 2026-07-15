from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tracker.database import ROOT, atomic_write_json, load_questions


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a numbered question stub and metadata.")
    parser.add_argument("--number", type=int, required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--difficulty", choices=["easy", "medium", "hard"], required=True)
    args = parser.parse_args()
    category = ROOT / "leetcode_python" / args.category
    if not category.is_dir():
        parser.error(f"unknown category: {args.category}")
    slug = slugify(args.title)
    relative = f"leetcode_python/{args.category}/{args.number:04d}_{slug}.py"
    destination = ROOT / relative
    if destination.exists():
        parser.error(f"file already exists: {relative}")
    template = (ROOT / "docs/QUESTION_TEMPLATE.py").read_text(encoding="utf-8")
    destination.write_text(
        template.replace("LeetCode: TODO", f"LeetCode: {args.number}")
        .replace("Title: TODO", f"Title: {args.title}")
        .replace("URL: TODO", f"URL: https://leetcode.com/problems/{slug.replace('_', '-')}/")
        .replace("Difficulty: TODO", f"Difficulty: {args.difficulty.title()}")
        .replace(
            "    TODO\nSecondary Patterns:",
            f"    {args.category.replace('_', ' ').title()}\nSecondary Patterns:",
            1,
        ),
        encoding="utf-8",
    )
    questions = load_questions()
    identifier = f"leetcode-{args.number:04d}"
    if any(q["id"] == identifier for q in questions):
        destination.unlink()
        parser.error(f"metadata already exists: {identifier}")
    today = date.today().isoformat()
    questions.append(
        {
            "id": identifier,
            "leetcode_number": args.number,
            "title": args.title,
            "slug": slug.replace("_", "-"),
            "source": "leetcode",
            "category": args.category,
            "primary_pattern": args.category,
            "secondary_patterns": [],
            "difficulty": args.difficulty,
            "phase": "Phase A",
            "file_path": relative,
            "status": "not_started",
            "confidence": 1,
            "attempts": 0,
            "completed_without_help": False,
            "last_practiced": None,
            "next_review": None,
            "average_minutes": 0,
            "best_minutes": None,
            "mistake_tags": [],
            "notes": "",
            "created_at": today,
            "updated_at": today,
        }
    )
    atomic_write_json(ROOT / "tracker/questions.json", questions)
    print(destination)


if __name__ == "__main__":
    main()
