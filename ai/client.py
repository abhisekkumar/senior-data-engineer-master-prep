from __future__ import annotations

import os

from ai.evaluator import InterviewEvaluator, NoOpEvaluator, OpenAIInterviewEvaluator


def evaluator_from_environment() -> InterviewEvaluator:
    if os.getenv("AI_ENABLED", "false").lower() != "true":
        return NoOpEvaluator()
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("AI_ENABLED is true but OPENAI_API_KEY is not configured")
    if not os.getenv("OPENAI_MODEL"):
        raise RuntimeError("AI_ENABLED is true but OPENAI_MODEL is not configured")
    return OpenAIInterviewEvaluator(
        api_key=os.environ["OPENAI_API_KEY"],
        model=os.environ["OPENAI_MODEL"],
    )
