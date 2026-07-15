from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tracker.database import ROOT, load_questions
from tracker.models import Question

REQUIRED_SECTIONS = (
    "LeetCode:",
    "Title:",
    "URL:",
    "Difficulty:",
    "Primary Pattern:",
    "Secondary Patterns:",
    "Interview Phase:",
    "Restate the Problem:",
    "Recognition Clues:",
    "Clarifying Questions:",
    "Small Example and Dry Run:",
    "Brute-Force Approach:",
    "Brute-Force Complexity:",
    "Optimal Approach:",
    "Optimal Complexity:",
    "Why This Approach:",
    "Important Edge Cases:",
    "Interviewer Follow-Ups:",
    "Common Mistakes:",
    "Original Implementation:",
    "Complexity of the Original Implementation:",
)
ORIGINAL_START = "# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---"
ORIGINAL_END = "# --- ORIGINAL SOLUTION END ---"


def validate() -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for raw in load_questions():
        try:
            question = Question.from_dict(raw)
        except (TypeError, ValueError) as exc:
            errors.append(f"{raw.get('id', '<unknown>')}: {exc}")
            continue
        if question.id in seen:
            errors.append(f"duplicate id: {question.id}")
        seen.add(question.id)
        path = ROOT / question.file_path
        if not path.is_file():
            errors.append(f"missing file: {question.file_path}")
            continue
        if question.leetcode_number is not None and not re.match(r"^\d{4}_", path.name):
            errors.append(f"numbered file required: {question.file_path}")
        if question.leetcode_number is not None:
            content = path.read_text(encoding="utf-8")
            missing = [section for section in REQUIRED_SECTIONS if section not in content]
            if missing:
                errors.append(f"{question.file_path}: missing sections: {', '.join(missing)}")
            if content.count(ORIGINAL_START) != 1 or content.count(ORIGINAL_END) != 1:
                errors.append(f"{question.file_path}: expected one preserved-solution marker pair")
    return errors


def main() -> None:
    errors = validate()
    if errors:
        raise SystemExit("Validation failed:\n- " + "\n- ".join(errors))
    print(f"Validated {len(load_questions())} question records and preserved solution boundaries.")


if __name__ == "__main__":
    main()
