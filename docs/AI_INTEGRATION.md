# Optional AI Integration

AI feedback is opt-in. The repository, tracker, tests, plans, and dashboard work without an API
key. With the default `AI_ENABLED=false`, `evaluator_from_environment()` returns a no-op evaluator
that sends nothing.

## Enable the OpenAI provider

Copy `.env.example` to a local `.env` file that remains Git-ignored, then set:

```dotenv
OPENAI_API_KEY=your-local-secret
OPENAI_MODEL=your-selected-model
AI_ENABLED=true
```

The repository does not automatically load or send files. A caller must explicitly pass these
five strings to `evaluate_answer`: the question, the learner's explanation, selected code, stated
time complexity, and stated space complexity. The provider uses a 30-second timeout and one retry.
Errors are returned without logging the key or changing repository files.

## Evaluation rubric

The optional evaluator scores each dimension from 0–5:

- Problem understanding
- Clarifying questions
- Brute-force reasoning
- Pattern recognition
- Optimal reasoning
- Code correctness
- Code readability
- Time complexity
- Space complexity
- Edge cases
- Communication
- Follow-up readiness

It returns structured feedback with the 0–60 total, per-dimension scores, strengths, missing
items, complexity and code feedback, follow-up questions, recommended confidence, recommended
review interval, and the reason for the confidence recommendation.

Feedback is advisory. It must be reviewed by the learner and never automatically overwrite a
question solution, explanation, tracker score, or practice record.
