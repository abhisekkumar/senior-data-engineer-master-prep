import json
from pathlib import Path

import dashboard.services as services


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value), encoding="utf-8")


def test_practice_attempt_is_appended_and_question_is_updated(tmp_path, monkeypatch) -> None:
    questions_path = tmp_path / "questions.json"
    attempts_path = tmp_path / "practice_log.json"
    plans_path = tmp_path / "study_plan.json"
    question = {
        "id": "leetcode-0001",
        "confidence": 2,
        "attempts": 0,
        "average_minutes": 0,
        "best_minutes": None,
        "mistake_tags": [],
        "notes": "",
        "status": "not_started",
    }
    write_json(questions_path, [question])
    write_json(attempts_path, [])
    write_json(plans_path, [])
    monkeypatch.setattr(services, "QUESTIONS_PATH", questions_path)
    monkeypatch.setattr(services, "PRACTICE_LOG_PATH", attempts_path)
    monkeypatch.setattr(services, "STUDY_PLAN_PATH", plans_path)
    monkeypatch.setattr(services, "load_questions", lambda: json.loads(questions_path.read_text()))

    attempt = services.log_practice_attempt(
        question_id="leetcode-0001",
        result="completed",
        confidence_before=2,
        confidence_after=4,
        minutes_spent=18,
        hints_used=0,
        mistakes=["complexity_explanation"],
        notes="Explain the map invariant more clearly.",
        clarifying_questions_score=4,
        brute_force_score=4,
        optimal_approach_score=4,
        coding_score=4,
        complexity_score=4,
        communication_score=4,
    )

    saved_attempts = json.loads(attempts_path.read_text())
    saved_question = json.loads(questions_path.read_text())[0]
    assert saved_attempts == [attempt]
    assert saved_question["status"] == "completed"
    assert saved_question["confidence"] == 4
    assert saved_question["attempts"] == 1
    assert saved_question["next_review"]
    assert saved_question["mistake_tags"] == ["complexity_explanation"]


def test_daily_task_status_is_persisted(tmp_path, monkeypatch) -> None:
    plans_path = tmp_path / "study_plan.json"
    write_json(
        plans_path,
        [{"date": "2026-07-14", "items": [{"position": 1, "status": "not_started"}]}],
    )
    monkeypatch.setattr(services, "STUDY_PLAN_PATH", plans_path)
    services.update_daily_task(
        plan_date="2026-07-14",
        position=1,
        status="started",
        minutes_spent=5,
        notes="Opened the question.",
    )
    task = json.loads(plans_path.read_text())[0]["items"][0]
    assert task == {
        "position": 1,
        "status": "started",
        "minutes_spent": 5,
        "notes": "Opened the question.",
    }
