from types import SimpleNamespace

import pytest

from ai.client import evaluator_from_environment
from ai.evaluator import RUBRIC_DIMENSIONS, NoOpEvaluator, OpenAIInterviewEvaluator


def complete_evaluation() -> dict[str, object]:
    return {
        "overall_score": 48,
        "rubric_scores": {dimension: 4 for dimension in RUBRIC_DIMENSIONS},
        "strengths": ["Clear invariant."],
        "missing_items": ["Discuss empty input."],
        "complexity_feedback": "The stated bounds are consistent with the approach.",
        "code_feedback": "Readable and direct.",
        "follow_up_questions": ["How would this work as a stream?"],
        "recommended_confidence": 4,
        "recommended_next_review_days": 7,
        "confidence_reason": "The answer is independent and clear, but follow-ups remain.",
    }


def test_no_op_evaluator_sends_nothing() -> None:
    result = NoOpEvaluator().evaluate_answer(
        question="question",
        explanation="explanation",
        code="code",
        stated_time_complexity="O(n)",
        stated_space_complexity="O(n)",
    )
    assert result["overall_score"] == 0
    assert set(result["rubric_scores"]) == set(RUBRIC_DIMENSIONS)


def test_ai_is_disabled_by_default(monkeypatch) -> None:
    monkeypatch.delenv("AI_ENABLED", raising=False)
    assert isinstance(evaluator_from_environment(), NoOpEvaluator)


def test_enabled_ai_requires_model(monkeypatch) -> None:
    monkeypatch.setenv("AI_ENABLED", "true")
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.delenv("OPENAI_MODEL", raising=False)
    with pytest.raises(RuntimeError, match="OPENAI_MODEL"):
        evaluator_from_environment()


def test_openai_evaluator_validates_structured_feedback() -> None:
    import json

    calls: list[dict[str, object]] = []

    def create(**kwargs: object) -> SimpleNamespace:
        calls.append(kwargs)
        message = SimpleNamespace(content=json.dumps(complete_evaluation()))
        return SimpleNamespace(choices=[SimpleNamespace(message=message)])

    client = SimpleNamespace(
        chat=SimpleNamespace(completions=SimpleNamespace(create=create)),
    )
    evaluator = OpenAIInterviewEvaluator(api_key="test-key", model="test-model", client=client)
    result = evaluator.evaluate_answer(
        question="Two Sum",
        explanation="Use a complement map.",
        code="def solve(): ...",
        stated_time_complexity="O(n)",
        stated_space_complexity="O(n)",
    )
    assert result["recommended_confidence"] == 4
    assert calls[0]["model"] == "test-model"
    assert calls[0]["response_format"] == {"type": "json_object"}
