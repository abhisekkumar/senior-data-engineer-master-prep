from __future__ import annotations

from collections import Counter
from datetime import date, timedelta
from typing import Any


def summary(questions: list[dict[str, Any]], attempts: list[dict[str, Any]]) -> dict[str, Any]:
    today = date.today().isoformat()
    completed = [q for q in questions if q.get("status") == "completed"]
    practiced_days = {a.get("practiced_at", "")[:10] for a in attempts}
    streak = 0
    cursor = date.today()
    while cursor.isoformat() in practiced_days:
        streak += 1
        cursor -= timedelta(days=1)
    return {
        "total_questions": len(questions),
        "completed": len(completed),
        "not_started": sum(q.get("status") == "not_started" for q in questions),
        "due_today": sum(
            bool(q.get("next_review")) and q["next_review"] <= today for q in questions
        ),
        "average_confidence": round(
            sum(q.get("confidence", 1) for q in questions) / len(questions), 2
        )
        if questions
        else 0,
        "patterns": dict(Counter(q.get("primary_pattern", "unknown") for q in questions)),
        "difficulties": dict(Counter(q.get("difficulty", "unknown") for q in questions)),
        "sources": dict(Counter(q.get("source", "unknown") for q in questions)),
        "streak": streak,
        "attempts": len(attempts),
        "average_minutes": round(
            sum(a.get("minutes_spent", 0) for a in attempts) / len(attempts), 2
        )
        if attempts
        else 0,
    }
