from __future__ import annotations

import json
from typing import Any, Protocol

from ai.prompts import RUBRIC, SYSTEM_PROMPT
from ai.schemas import Evaluation

RUBRIC_DIMENSIONS = (
    "problem_understanding",
    "clarifying_questions",
    "brute_force_reasoning",
    "pattern_recognition",
    "optimal_reasoning",
    "code_correctness",
    "code_readability",
    "time_complexity",
    "space_complexity",
    "edge_cases",
    "communication",
    "follow_up_readiness",
)


class InterviewEvaluator(Protocol):
    def evaluate_answer(
        self,
        *,
        question: str,
        explanation: str,
        code: str,
        stated_time_complexity: str,
        stated_space_complexity: str,
    ) -> Evaluation: ...


class NoOpEvaluator:
    def evaluate_answer(self, **_: str) -> Evaluation:
        return {
            "overall_score": 0,
            "rubric_scores": {dimension: 0 for dimension in RUBRIC_DIMENSIONS},
            "strengths": [],
            "missing_items": ["AI feedback is disabled; review the rubric manually."],
            "complexity_feedback": "Not evaluated.",
            "code_feedback": "Not evaluated.",
            "follow_up_questions": [],
            "recommended_confidence": 1,
            "recommended_next_review_days": 1,
            "confidence_reason": "No automated evaluation was performed.",
        }


class OpenAIInterviewEvaluator:
    """Opt-in evaluator that sends only the five answer fields passed by the caller."""

    def __init__(
        self,
        *,
        api_key: str,
        model: str,
        timeout: float = 30.0,
        client: Any | None = None,
    ) -> None:
        if not api_key:
            raise ValueError("An OpenAI API key is required when AI feedback is enabled")
        if not model:
            raise ValueError("OPENAI_MODEL is required when AI feedback is enabled")
        if client is None:
            from openai import OpenAI

            client = OpenAI(api_key=api_key, timeout=timeout, max_retries=1)
        self._client = client
        self._model = model

    def evaluate_answer(
        self,
        *,
        question: str,
        explanation: str,
        code: str,
        stated_time_complexity: str,
        stated_space_complexity: str,
    ) -> Evaluation:
        selected_content = {
            "question": question,
            "explanation": explanation,
            "code": code,
            "stated_time_complexity": stated_time_complexity,
            "stated_space_complexity": stated_space_complexity,
        }
        try:
            response = self._client.chat.completions.create(
                model=self._model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": f"{RUBRIC}\n\nEvaluate this selected answer:\n"
                        + json.dumps(selected_content),
                    },
                ],
                response_format={"type": "json_object"},
                temperature=0,
            )
            content = response.choices[0].message.content
            if not content:
                raise ValueError("the provider returned an empty response")
            return validate_evaluation(json.loads(content))
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"AI feedback returned an invalid structured result: {exc}") from exc
        except Exception as exc:
            raise RuntimeError(
                "AI feedback could not be completed. Check the selected model, network, and API "
                "configuration; no repository file was changed."
            ) from exc


def validate_evaluation(value: object) -> Evaluation:
    if not isinstance(value, dict):
        raise ValueError("evaluation must be a JSON object")
    scores = value.get("rubric_scores")
    if not isinstance(scores, dict) or set(scores) != set(RUBRIC_DIMENSIONS):
        raise ValueError("rubric_scores must contain every documented rubric dimension")
    if any(not isinstance(score, int) or not 0 <= score <= 5 for score in scores.values()):
        raise ValueError("rubric scores must be integers from 0 to 5")
    overall = value.get("overall_score")
    if not isinstance(overall, int) or not 0 <= overall <= 60:
        raise ValueError("overall_score must be an integer from 0 to 60")
    confidence = value.get("recommended_confidence")
    if not isinstance(confidence, int) or not 1 <= confidence <= 5:
        raise ValueError("recommended_confidence must be an integer from 1 to 5")
    review_days = value.get("recommended_next_review_days")
    if not isinstance(review_days, int) or review_days < 1:
        raise ValueError("recommended_next_review_days must be a positive integer")
    for key in ("strengths", "missing_items", "follow_up_questions"):
        if not isinstance(value.get(key), list) or not all(
            isinstance(item, str) for item in value[key]
        ):
            raise ValueError(f"{key} must be a list of strings")
    for key in ("complexity_feedback", "code_feedback", "confidence_reason"):
        if not isinstance(value.get(key), str):
            raise ValueError(f"{key} must be a string")
    return value  # type: ignore[return-value]
