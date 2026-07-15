from datetime import date

import pytest

from tracker.scheduler import build_daily_plan, effective_confidence, next_review_date


@pytest.mark.parametrize("confidence,days", [(1, 1), (2, 2), (3, 4), (4, 7), (5, 14)])
def test_review_intervals(confidence: int, days: int) -> None:
    assert (next_review_date(confidence, date(2026, 7, 14)) - date(2026, 7, 14)).days == days


def test_confidence_caps() -> None:
    assert effective_confidence(5, correct=False) == 2
    assert effective_confidence(5, major_hints=True) == 3
    assert effective_confidence(5, complexity_correct=False) == 3
    assert effective_confidence(5, explanation_clear=False) == 4
    assert effective_confidence(5, follow_ups_successful=False) == 4


def test_daily_plan_has_five_positions() -> None:
    questions = [
        {"id": "a", "confidence": 2, "status": "not_started", "next_review": "2026-07-14"},
        {"id": "b", "confidence": 1, "status": "not_started", "next_review": None},
    ]
    plan = build_daily_plan(questions, date(2026, 7, 14))
    assert [item["position"] for item in plan["items"]] == [1, 2, 3, 4, 5]
    assert plan["items"][0]["question_id"] != plan["items"][1]["question_id"]
    assert all(item["status"] == "not_started" for item in plan["items"])
