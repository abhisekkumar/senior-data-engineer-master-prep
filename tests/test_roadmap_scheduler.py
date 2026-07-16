from datetime import date

import pytest

from tracker.roadmap import (
    RoadmapError,
    find_item,
    maybe_advance_phase,
    seed_roadmap,
    set_active_phase,
    update_item_status,
)
from tracker.scheduler import build_daily_plan


def questions() -> list[dict[str, object]]:
    return [
        {
            "id": "leetcode-0217",
            "title": "Contains Duplicate",
            "status": "completed",
            "confidence": 2,
            "next_review": "2026-07-13",
        },
        {
            "id": "leetcode-0001",
            "title": "Two Sum",
            "status": "not_started",
            "confidence": 1,
            "next_review": None,
        },
    ]


def test_daily_plan_prioritizes_current_phase_and_overdue_link() -> None:
    document = seed_roadmap(question["id"] for question in questions())
    plan = build_daily_plan(questions(), date(2026, 7, 14), roadmap=document)
    assert len(plan["items"]) == 5
    assert plan["items"][0]["roadmap_item_id"]
    assert plan["items"][0]["question_id"] == "leetcode-0217"
    assert any(item.get("roadmap_item_id") for item in plan["items"])


def test_manual_phase_override_is_required_until_ready() -> None:
    document = seed_roadmap()
    with pytest.raises(RoadmapError, match="explicit override"):
        set_active_phase(document, "phase-b")
    set_active_phase(document, "phase-b", override=True)
    assert document.settings.active_phase_id == "phase-b"


def test_automatic_phase_advancement_requires_interview_ready() -> None:
    document = seed_roadmap()
    document.settings.automatic_advancement = True
    document.settings.manual_phase_mode = False
    assert not maybe_advance_phase(document)
    for module in document.programs[0].phases[0].modules:
        for item in module.items:
            update_item_status(document, item.id, "interview_ready")
    assert maybe_advance_phase(document)
    assert document.settings.active_phase_id == "phase-b"


def test_daily_completion_never_implies_mastery() -> None:
    document = seed_roadmap(["leetcode-0001"])
    item = next(
        item
        for module in document.programs[0].phases[0].modules
        for item in module.items
        if "leetcode-0001" in item.linked_question_ids
    )
    update_item_status(document, item.id, "interview_ready")
    assert find_item(document, item.id).status == "interview_ready"
