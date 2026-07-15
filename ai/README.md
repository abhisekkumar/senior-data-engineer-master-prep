# Optional AI Feedback

This package contains a provider interface, a default no-op evaluator, and an opt-in OpenAI
evaluator. The project works fully with `AI_ENABLED=false` and sends no content in that mode.

When explicitly enabled, only the five answer strings supplied by the caller are sent. Results
are structured suggestions for human review; they never overwrite solutions or tracker data. See
[`docs/AI_INTEGRATION.md`](../docs/AI_INTEGRATION.md) for setup, rubric, and privacy boundaries.
