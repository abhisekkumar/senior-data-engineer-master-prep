# Senior Data Engineer Master Prep

A lightweight, open-source study system for senior data engineering interviews. It keeps Python
and DSA practice, SQL, system design, company preparation, spaced repetition, and progress
tracking organized without turning interview preparation into a large application.

Created and maintained by [Abhisek Kumar](https://github.com/abhisekkumar). Thoughtful issues,
corrections, original examples, and pull requests are welcome.

> Dashboard screenshot placeholder: add `docs/images/dashboard.png` after the first public
> release.

## Who this is for

This repository is for engineers preparing for Python coding, senior data engineering, SQL,
Spark, data-platform design, GenAI, production troubleshooting, and behavioral interviews. It is
also designed for learners who want a repeatable five-item daily practice loop instead of an
unstructured collection of solutions.

## Key features

- 68 numbered LeetCode question files organized by interview pattern
- Six employer-neutral Python and data engineering exercises
- An interview template around every migrated solution, with the original code preserved
- Confidence-based spaced repetition and an append-only practice log
- A five-item daily plan covering coding, fundamentals, engineering, and communication
- A local Streamlit dashboard with tracking forms, filters, review queues, and progress charts
- Separate documentation, SQL, and company-preparation libraries
- Pytest, Ruff, metadata validation, safe JSON writes, and helpful command-line tools
- Optional AI feedback that is disabled by default and never required

## Repository structure

```text
senior-data-engineer-master-prep/
├── leetcode_python/      # Numbered LeetCode and custom Python exercises by pattern
├── sql/                  # SQL practice, kept separate from Python questions
├── docs/                 # General interview notes, diagrams, plans, and guides
├── companies/adonis/     # Adonis-specific preparation, including all migrated text notes
├── study/                # Current month, daily plan, reviews, mocks, and mistake log
├── tracker/              # Question metadata, attempts, plans, scheduling, and analytics
├── dashboard/            # Local Streamlit application
├── scripts/              # Migration, planning, logging, validation, and export commands
├── ai/                   # Optional no-op and OpenAI feedback providers
├── tests/                # Tracker, dashboard, scripts, migration, and catalog tests
└── exports/              # Generated progress exports
```

The private source folder is retained locally only as migration evidence and is excluded by
`.gitignore`. Public material is generalized and checked for private employer references.

The Adonis library includes all 19 original text notes. Start at
[`companies/adonis/README.md`](companies/adonis/README.md); the detailed recognition guide is
[`companies/adonis/dsa/FAST_RECOGNITION_SUMMARY.md`](companies/adonis/dsa/FAST_RECOGNITION_SUMMARY.md).

## Setup

Python 3.11 or newer is required.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Common commands:

```bash
make test       # Run the complete pytest suite
make lint       # Run Ruff checks
make validate   # Validate tracker records and question documentation
make daily      # Generate today's five-item study plan
make weekly     # Generate a weekly review
make export     # Export progress summaries
make dashboard  # Start the local Streamlit tracker
```

## Run tests and validation

Before opening a pull request, run:

```bash
pytest -q
ruff check .
python3 scripts/validate_questions.py
```

Numbered files deliberately retain the author's original formatting and draft issues inside
clearly marked preservation boundaries. Ruff does not rewrite those blocks. Structural tests
ensure that each tracked question has its required interview sections and preservation markers.
Known draft limitations are documented in [`docs/MIGRATION_REPORT.md`](docs/MIGRATION_REPORT.md).

## Start the localhost dashboard

```bash
streamlit run dashboard/app.py
```

Then open [http://localhost:8501](http://localhost:8501). No authentication or AI key is needed.
The dashboard provides:

- Summary metrics and question breakdowns
- Today's five tasks, local file links, status updates, and practice forms
- Question search by number/title and filters for pattern, category, difficulty, status,
  confidence, due date, and mistake tag
- Overdue, due-today, due-this-week, low-confidence, and frequently missed review queues
- Attempt, confidence, completion, timing, and mistake charts

The tracker writes locally to `tracker/questions.json`, `tracker/practice_log.json`, and
`tracker/study_plan.json`. See [`docs/LOCAL_DASHBOARD.md`](docs/LOCAL_DASHBOARD.md) for the full
workflow.

## Five-item daily workflow

Run `make daily` or open the **Today's Five** dashboard tab. A standard day contains:

1. One completed Python/DSA question due for review
2. One new or weak Python/DSA question
3. One SQL, Python fundamentals, or debugging topic
4. One Spark, data engineering, or system-design topic
5. One behavioral, project explanation, GenAI, or troubleshooting topic

Log coding practice in the dashboard or from the command line:

```bash
python3 scripts/log_practice.py \
  --question leetcode-0001 \
  --result completed \
  --confidence-before 3 \
  --confidence-after 4 \
  --minutes 20 \
  --clarifying-score 4 \
  --brute-force-score 4 \
  --optimal-score 4 \
  --coding-score 4 \
  --complexity-score 4 \
  --communication-score 4
```

Every attempt is appended; previous attempts are not overwritten. The tracker updates aggregate
question statistics and schedules the next review.

## Confidence and spaced repetition

| Confidence | Meaning | Default next review |
|---:|---|---:|
| 1 | Could not begin | 1 day |
| 2 | Understood after substantial help | 2 days |
| 3 | Completed with hints | 4 days |
| 4 | Completed independently | 7 days |
| 5 | Can explain, code, optimize, and answer follow-ups | 14 days |

Quality caps keep the score honest:

- An incorrect solution is capped at 2.
- A correct solution requiring major hints is capped at 3.
- Correct code with incorrect complexity is capped at 3.
- An independent solution with a weak explanation is capped at 4.
- Confidence 5 requires correct code and complexity, a clear explanation, pattern recognition,
  and successful follow-up answers.

## Required question format

Each numbered file begins with its LeetCode number and lives in its pattern folder, for example
`leetcode_python/heaps_priority_queues/0347_top_k_frequent_elements.py`. Documentation around the
solution covers:

- Problem restatement, recognition clues, and realistic clarifying questions
- A small example and dry run
- Brute-force idea, correctness, time/space complexity, and scaling limitation
- Optimal insight, data structure, algorithm, time/space complexity, and trade-offs
- Relevant edge cases, follow-ups, and common mistakes
- Practice-tracking guidance

The author's migrated implementation remains exactly between:

```python
# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
# original code
# --- ORIGINAL SOLUTION END ---
```

Documentation may be improved around that block, but automation must not reformat, optimize, or
silently correct it. Use [`docs/QUESTION_TEMPLATE.py`](docs/QUESTION_TEMPLATE.py) for new work.

## Add a question

```bash
python3 scripts/add_question.py \
  --number 347 \
  --title "Top K Frequent Elements" \
  --category heaps_priority_queues \
  --difficulty medium
```

Then:

1. Complete the generated interview documentation and solution.
2. Add standard, boundary, duplicate-heavy, negative, and empty-input tests when applicable.
3. Review the new record in `tracker/questions.json`.
4. Run tests, Ruff, and validation.

Never guess a LeetCode number. Use an `unknown_` filename and a TODO when the mapping is uncertain.
See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the complete contribution workflow.

## One-month preparation structure

- **Week 1 — Stabilize foundations:** arrays/hashing, Python behavior, SQL windows, Spark basics,
  requirements, and core stories
- **Week 2 — Pattern recognition:** prefix sums, windows, pointers, binary search, intervals,
  joins, CDC, and reliability
- **Week 3 — Senior-level engineering:** heaps, backfills, skew, Spark debugging, platforms,
  Kafka, observability, and leadership
- **Week 4 — Interview simulation:** weak patterns, mixed timed practice, verbal explanation,
  design trade-offs, behavioral delivery, and full mocks

The complete 28-day plan with five bullet-pointed tasks per day is in
[`docs/STUDY_PLAN.md`](docs/STUDY_PLAN.md). The current operational plans are in
[`study/current_month.md`](study/current_month.md) and [`study/daily_plan.md`](study/daily_plan.md).

## Optional AI feedback

The repository works fully without AI. `AI_ENABLED=false` selects a no-op evaluator that sends
nothing. To opt in, copy `.env.example`, select a model, and pass only the answer fields you
explicitly want evaluated. Feedback is advisory and never overwrites a solution.

See [`docs/AI_INTEGRATION.md`](docs/AI_INTEGRATION.md) for configuration, privacy boundaries, and
the scoring rubric.

## Contribute

Contributions are welcome—from typo fixes and better diagrams to tests, original explanations,
and new employer-neutral exercises. Please open an issue or pull request, even for a small
improvement.

Before contributing, read [`CONTRIBUTING.md`](CONTRIBUTING.md) and
[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Do not submit paid/copyrighted explanations,
confidential interview questions, employer-internal material, real company datasets, credentials,
personal information, or protected health information. Use original wording and synthetic data.

## Roadmap

Planned improvements are tracked in [`docs/ROADMAP.md`](docs/ROADMAP.md), including deeper
question tests, more SQL/Spark practice, mock-interview workflows, and optional provider-neutral
AI feedback improvements.

## License

This project is available under the [MIT License](LICENSE).

## Disclaimer

This is an independent educational project. It is not affiliated with or endorsed by LeetCode,
Adonis, OpenAI, or any current or former employer. Public content must remain original,
generalized, and free of confidential employer information, proprietary interview content,
credentials, protected health information, and real personal data.
