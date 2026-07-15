# Contributing

Corrections, original explanations, tests, diagrams, and employer-neutral practice questions are
welcome. Small, focused pull requests are easier to review and just as valuable as large additions.

## Development workflow

1. Fork the repository on GitHub.
2. Clone your fork and create a focused branch such as `question/0347-top-k` or
   `docs/binary-search-guide`.
3. Install dependencies with `make install`.
4. Make one cohesive change and update nearby documentation when commands or structure change.
5. Run `make test`, `make lint`, and `make validate`.
6. Push the branch to your fork and open a pull request.

## Add a coding question

Start with the helper:

```bash
python3 scripts/add_question.py \
  --number 347 \
  --title "Top K Frequent Elements" \
  --category heaps_priority_queues \
  --difficulty medium
```

Then:

- Follow `docs/QUESTION_TEMPLATE.py`.
- Never invent a LeetCode number; use an `unknown_` filename and TODO when uncertain.
- Include problem restatement, recognition clues, realistic clarifying questions, a small example,
  brute-force and optimal reasoning, time/space complexity, a dry run, relevant edge cases,
  common mistakes, and interviewer follow-ups.
- Prefer readable, interview-friendly Python over clever abstractions.
- Preserve existing migrated solution blocks exactly. Put corrections or alternatives outside the
  preservation markers and explain the trade-off.

## Add tests and metadata

- Add pytest coverage for the standard example, smallest valid input, important boundaries,
  duplicate-heavy input, negative values, and empty input when those cases are permitted.
- Update or review the record in `tracker/questions.json`.
- Do not rewrite `tracker/practice_log.json` history; attempts are append-only.
- Use the safe tracker utilities for JSON changes where practical.
- Run `make sync` after adding a Python or SQL solution. The synchronizer adds missing records and
  preserves all existing practice state.

## Pull-request description

Include:

- The problem or learning gap addressed
- The approach taken
- Files/questions added or moved
- Tracker or compatibility changes
- Tests and validation commands run
- Known limitations or items needing manual review

## Originality, privacy, and confidentiality

Use original explanations and code. Do not copy paid or copyrighted solution explanations
verbatim, publish confidential interview questions, or submit content you do not have the right to
share.

Do not include names of private individuals, email addresses, credentials, internal URLs, customer
or patient information, protected health information, real identifiers, employer-specific
architecture, proprietary metrics, screenshots of internal systems, or details learned under a
confidentiality obligation. Replace business examples with fictional, synthetic,
employer-neutral scenarios.

Maintainers may close or remove a contribution immediately when its publication rights or privacy
status are unclear.
