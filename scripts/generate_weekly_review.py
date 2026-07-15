from __future__ import annotations

import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tracker.database import ROOT, load_questions


def main() -> None:
    end = date.today() + timedelta(days=7)
    due = [
        q for q in load_questions() if q.get("next_review") and q["next_review"] <= end.isoformat()
    ]
    path = ROOT / "study/weekly_reviews" / f"{date.today()}.md"
    lines = [f"# Weekly review — {date.today()}", "", *[f"- {q['id']}: {q['title']}" for q in due]]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(path)


if __name__ == "__main__":
    main()
