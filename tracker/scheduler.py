from __future__ import annotations

from datetime import date, timedelta
from typing import Any

REVIEW_INTERVALS = {1: 1, 2: 2, 3: 4, 4: 7, 5: 14}


def effective_confidence(
    requested: int,
    *,
    correct: bool = True,
    major_hints: bool = False,
    complexity_correct: bool = True,
    explanation_clear: bool = True,
    follow_ups_successful: bool = True,
) -> int:
    if requested not in REVIEW_INTERVALS:
        raise ValueError("confidence must be between 1 and 5")
    cap = 5
    if not correct:
        cap = 2
    elif major_hints or not complexity_correct:
        cap = 3
    elif not explanation_clear:
        cap = 4
    if requested == 5 and not follow_ups_successful:
        cap = min(cap, 4)
    return min(requested, cap)


def next_review_date(confidence: int, practiced_on: date | None = None) -> date:
    if confidence not in REVIEW_INTERVALS:
        raise ValueError("confidence must be between 1 and 5")
    return (practiced_on or date.today()) + timedelta(days=REVIEW_INTERVALS[confidence])


def build_daily_plan(questions: list[dict[str, Any]], target: date | None = None) -> dict[str, Any]:
    target = target or date.today()
    due = sorted(
        (q for q in questions if q.get("next_review") and q["next_review"] <= target.isoformat()),
        key=lambda q: (q["next_review"], q.get("confidence", 1)),
    )
    review = due[0] if due else (questions[0] if questions else None)
    review_id = review["id"] if review else None
    weak = sorted(
        (q for q in questions if q["id"] != review_id),
        key=lambda q: (q.get("status") == "completed", q.get("confidence", 1)),
    )
    items: list[dict[str, Any]] = []
    if review:
        items.append({"position": 1, "type": "coding_review", "question_id": review["id"]})
    if weak:
        items.append({"position": 2, "type": "coding_new", "question_id": weak[0]["id"]})
    rotation = target.toordinal()
    fundamentals = [
        "mutable default arguments",
        "SQL window functions",
        "Python aliasing and mutation",
        "SQL deduplication with row_number",
    ]
    engineering = [
        ("system_design", "functional and non-functional requirements"),
        ("spark", "partitioning, shuffle, and skew"),
        ("data_engineering", "CDC, idempotency, and replay"),
        ("system_design", "reliability, observability, and recovery"),
    ]
    communication = [
        ("behavioral", "most complex pipeline"),
        ("troubleshooting", "production incident from detection to prevention"),
        ("behavioral", "leadership and conflict resolution"),
        ("genai", "enterprise RAG trade-offs and evaluation"),
    ]
    engineering_area, engineering_topic = engineering[rotation % len(engineering)]
    communication_area, communication_topic = communication[rotation % len(communication)]
    items.extend(
        [
            {
                "position": 3,
                "type": "python_fundamentals",
                "topic": fundamentals[rotation % len(fundamentals)],
            },
            {
                "position": 4,
                "type": "external_study",
                "area": engineering_area,
                "topic": engineering_topic,
            },
            {
                "position": 5,
                "type": "external_study",
                "area": communication_area,
                "topic": communication_topic,
            },
        ]
    )
    for item in items:
        item.update(status="not_started", minutes_spent=0, notes="")
    return {"date": target.isoformat(), "items": items}
