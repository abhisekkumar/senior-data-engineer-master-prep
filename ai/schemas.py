from __future__ import annotations

from typing import TypedDict


class Evaluation(TypedDict):
    overall_score: int
    rubric_scores: dict[str, int]
    strengths: list[str]
    missing_items: list[str]
    complexity_feedback: str
    code_feedback: str
    follow_up_questions: list[str]
    recommended_confidence: int
    recommended_next_review_days: int
    confidence_reason: str
