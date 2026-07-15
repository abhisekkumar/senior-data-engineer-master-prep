from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

from tracker.analytics import summary
from tracker.catalog import sync_catalog
from tracker.database import ROOT, atomic_write_json, load_questions, read_json
from tracker.scheduler import (
    REVIEW_INTERVALS,
    build_daily_plan,
    effective_confidence,
    next_review_date,
)

QUESTIONS_PATH = ROOT / "tracker/questions.json"
PRACTICE_LOG_PATH = ROOT / "tracker/practice_log.json"
STUDY_PLAN_PATH = ROOT / "tracker/study_plan.json"
RESOURCE_ROOTS = {
    "Interview guides": ROOT / "docs",
    "SQL practice": ROOT / "sql",
    "Company prep": ROOT / "companies",
    "Study plans": ROOT / "study",
}


def _plans() -> list[dict[str, Any]]:
    plans = read_json(STUDY_PLAN_PATH, [])
    if not isinstance(plans, list):
        raise ValueError("tracker/study_plan.json must contain a list")
    return plans


def get_or_create_daily_plan(
    questions: list[dict[str, Any]], target: date | None = None, *, persist: bool = False
) -> dict[str, Any]:
    target = target or date.today()
    plans = _plans()
    existing = next((plan for plan in plans if plan.get("date") == target.isoformat()), None)
    if existing is not None:
        return existing
    plan = build_daily_plan(questions, target)
    if persist:
        plans.append(plan)
        atomic_write_json(STUDY_PLAN_PATH, plans)
    return plan


def dashboard_data(*, persist_plan: bool = False) -> dict[str, Any]:
    catalog_sync = sync_catalog()
    questions = load_questions()
    attempts = read_json(PRACTICE_LOG_PATH, [])
    if not isinstance(attempts, list):
        raise ValueError("tracker/practice_log.json must contain a list")
    return {
        "questions": questions,
        "attempts": attempts,
        "summary": summary(questions, attempts),
        "today": get_or_create_daily_plan(questions, persist=persist_plan),
        "catalog_sync": catalog_sync,
        "resources": study_resources(),
    }


def study_resources() -> list[dict[str, str]]:
    resources: list[dict[str, str]] = []
    for collection, root in RESOURCE_ROOTS.items():
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.suffix.casefold() not in {".md", ".sql"}:
                continue
            relative = path.relative_to(ROOT).as_posix()
            local = path.relative_to(root)
            section = local.parts[0] if len(local.parts) > 1 else "overview"
            title = path.stem.replace("_", " ").replace("-", " ").strip().title()
            if path.suffix.casefold() == ".md":
                first_heading = next(
                    (
                        line.removeprefix("# ").strip()
                        for line in path.read_text(encoding="utf-8").splitlines()
                        if line.startswith("# ")
                    ),
                    None,
                )
                title = first_heading or title
            resources.append(
                {
                    "title": title,
                    "collection": collection,
                    "topic": section.replace("_", " ").title(),
                    "format": "SQL" if path.suffix.casefold() == ".sql" else "Guide",
                    "file_path": relative,
                }
            )
    return resources


def question_by_id(questions: list[dict[str, Any]], question_id: str) -> dict[str, Any] | None:
    return next((question for question in questions if question["id"] == question_id), None)


def question_file(question: dict[str, Any]) -> Path:
    return ROOT / question["file_path"]


def filter_questions(
    questions: list[dict[str, Any]],
    *,
    query: str = "",
    source: str = "All",
    pattern: str = "All",
    category: str = "All",
    difficulty: str = "All",
    status: str = "All",
    confidence: str = "All",
    due: str = "All",
    mistake_tag: str = "",
) -> list[dict[str, Any]]:
    query = query.casefold().strip()
    mistake_tag = mistake_tag.casefold().strip()
    today = date.today()
    week_end = today + timedelta(days=7)

    def due_matches(question: dict[str, Any]) -> bool:
        value = question.get("next_review")
        if due == "All":
            return True
        if not value:
            return due == "Unscheduled"
        review = date.fromisoformat(value)
        if due == "Overdue":
            return review < today
        if due == "Today":
            return review == today
        if due == "This week":
            return today <= review <= week_end
        return True

    return [
        question
        for question in questions
        if (
            not query
            or query in question["title"].casefold()
            or query in question["id"].casefold()
            or query == str(question.get("leetcode_number", ""))
        )
        and (pattern == "All" or question["primary_pattern"] == pattern)
        and (source == "All" or question.get("source") == source)
        and (category == "All" or question["category"] == category)
        and (difficulty == "All" or question["difficulty"] == difficulty)
        and (status == "All" or question["status"] == status)
        and (confidence == "All" or question["confidence"] == int(confidence))
        and due_matches(question)
        and (
            not mistake_tag
            or any(mistake_tag in tag.casefold() for tag in question.get("mistake_tags", []))
        )
    ]


def review_queues(questions: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    today = date.today()
    week_end = today + timedelta(days=7)

    def review_date(question: dict[str, Any]) -> date | None:
        value = question.get("next_review")
        return date.fromisoformat(value) if value else None

    overdue = [q for q in questions if review_date(q) and review_date(q) < today]
    due_today = [q for q in questions if review_date(q) == today]
    due_week = [q for q in questions if review_date(q) and today < review_date(q) <= week_end]
    low_confidence = sorted(questions, key=lambda q: (q.get("confidence", 1), q["title"]))[:10]
    frequently_missed = sorted(
        questions,
        key=lambda q: (len(q.get("mistake_tags", [])), q.get("attempts", 0)),
        reverse=True,
    )[:10]
    return {
        "Overdue": sorted(overdue, key=lambda q: q["next_review"]),
        "Due today": sorted(due_today, key=lambda q: q["title"]),
        "Due this week": sorted(due_week, key=lambda q: q["next_review"]),
        "Lowest confidence": low_confidence,
        "Frequently missed": frequently_missed,
    }


def update_daily_task(
    *,
    plan_date: str,
    position: int,
    status: str,
    minutes_spent: int = 0,
    notes: str = "",
) -> None:
    if status not in {"not_started", "started", "completed"}:
        raise ValueError("invalid task status")
    plans = _plans()
    plan = next((item for item in plans if item.get("date") == plan_date), None)
    if plan is None:
        raise ValueError(f"daily plan not found for {plan_date}")
    task = next((item for item in plan["items"] if item.get("position") == position), None)
    if task is None:
        raise ValueError(f"position {position} was not found in the daily plan")
    task.update(status=status, minutes_spent=minutes_spent, notes=notes)
    atomic_write_json(STUDY_PLAN_PATH, plans)


def log_practice_attempt(
    *,
    question_id: str,
    result: str,
    confidence_before: int,
    confidence_after: int,
    minutes_spent: int,
    hints_used: int,
    mistakes: list[str],
    notes: str,
    clarifying_questions_score: int,
    brute_force_score: int,
    optimal_approach_score: int,
    coding_score: int,
    complexity_score: int,
    communication_score: int,
) -> dict[str, Any]:
    if result not in {"completed", "completed_with_hint", "incorrect"}:
        raise ValueError("invalid practice result")
    questions = load_questions()
    question = question_by_id(questions, question_id)
    if question is None:
        raise ValueError(f"unknown question id: {question_id}")
    attempts = read_json(PRACTICE_LOG_PATH, [])
    if not isinstance(attempts, list):
        raise ValueError("tracker/practice_log.json must contain a list")

    correct = result != "incorrect"
    final_confidence = effective_confidence(
        confidence_after,
        correct=correct,
        major_hints=result == "completed_with_hint" or hints_used > 1,
        complexity_correct=complexity_score >= 4,
        explanation_clear=communication_score >= 4,
        follow_ups_successful=optimal_approach_score >= 4,
    )
    now = datetime.now().isoformat(timespec="seconds")
    sequence = 1 + sum(
        attempt.get("question_id") == question_id
        and attempt.get("practiced_at", "")[:10] == date.today().isoformat()
        for attempt in attempts
    )
    attempt = {
        "attempt_id": f"{date.today()}-{question_id}-{sequence:02d}",
        "question_id": question_id,
        "practiced_at": now,
        "mode": "independent" if hints_used == 0 else "assisted",
        "result": result,
        "confidence_before": confidence_before,
        "confidence_after": final_confidence,
        "minutes_spent": minutes_spent,
        "clarifying_questions_score": clarifying_questions_score,
        "brute_force_score": brute_force_score,
        "optimal_approach_score": optimal_approach_score,
        "coding_score": coding_score,
        "complexity_score": complexity_score,
        "communication_score": communication_score,
        "hints_used": hints_used,
        "mistakes": mistakes,
        "notes": notes,
        "next_action": f"Review in {REVIEW_INTERVALS[final_confidence]} days.",
    }

    previous_attempts = question.get("attempts", 0)
    previous_average = question.get("average_minutes", 0)
    total_minutes = previous_average * previous_attempts + minutes_spent
    mistake_tags = sorted(set(question.get("mistake_tags", [])) | set(mistakes))
    question.update(
        status="completed" if correct else "in_progress",
        confidence=final_confidence,
        attempts=previous_attempts + 1,
        completed_without_help=correct and hints_used == 0,
        last_practiced=date.today().isoformat(),
        next_review=next_review_date(final_confidence).isoformat(),
        average_minutes=round(total_minutes / (previous_attempts + 1), 2),
        best_minutes=min(
            value for value in (question.get("best_minutes"), minutes_spent) if value is not None
        ),
        mistake_tags=mistake_tags,
        notes=notes or question.get("notes", ""),
        updated_at=date.today().isoformat(),
    )
    attempts.append(attempt)
    atomic_write_json(PRACTICE_LOG_PATH, attempts)
    atomic_write_json(QUESTIONS_PATH, questions)
    return attempt


def progress_data(
    questions: list[dict[str, Any]], attempts: list[dict[str, Any]]
) -> dict[str, dict[str, float | int]]:
    attempts_by_day = Counter(attempt.get("practiced_at", "")[:10] for attempt in attempts)
    confidence_by_day: dict[str, list[int]] = defaultdict(list)
    minutes_by_category: dict[str, list[int]] = defaultdict(list)
    question_categories = {question["id"]: question["category"] for question in questions}
    mistake_counts: Counter[str] = Counter()
    for attempt in attempts:
        day = attempt.get("practiced_at", "")[:10]
        confidence_by_day[day].append(attempt.get("confidence_after", 1))
        category = question_categories.get(attempt.get("question_id"), "unknown")
        minutes_by_category[category].append(attempt.get("minutes_spent", 0))
        mistake_counts.update(attempt.get("mistakes", []))
    completed_by_category = Counter(
        question["category"] for question in questions if question.get("status") == "completed"
    )
    return {
        "attempts_by_day": dict(sorted(attempts_by_day.items())),
        "confidence_by_day": {
            day: round(sum(values) / len(values), 2)
            for day, values in sorted(confidence_by_day.items())
        },
        "completed_by_category": dict(completed_by_category),
        "average_minutes_by_category": {
            category: round(sum(values) / len(values), 2)
            for category, values in minutes_by_category.items()
        },
        "mistakes": dict(mistake_counts.most_common()),
    }
