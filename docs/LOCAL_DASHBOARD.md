# Local Progress Dashboard

The repository includes a lightweight Streamlit dashboard. It runs entirely on your machine, requires no authentication, and reads/writes the JSON files under `tracker/`.

## Install

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Start the dashboard

Use either command:

```bash
make dashboard
```

or:

```bash
streamlit run dashboard/app.py
```

Open the URL Streamlit prints, normally:

```text
http://localhost:8501
```

Stop it with `Ctrl+C` in the terminal.

## Light and dark modes

Open the Streamlit menu in the upper-right corner, then choose **Settings → Theme**. Both modes
use the repository's configured indigo palette, readable contrast, matching charts, and a
mode-specific sidebar.

## Dashboard sections

### Dashboard

- Total questions
- Completed and not-started questions
- Questions due today
- Average confidence
- Current practice streak
- Total attempts
- Average practice time
- Questions by pattern and difficulty
- Exercises by source and today's five-item completion progress

### Today's Five

- Displays the generated five-item daily plan
- Opens the associated local solution path
- Marks tasks started or completed
- Records time and notes for non-coding work
- Records a complete coding attempt with confidence, hints, mistakes, and interview scores
- Applies confidence caps and schedules the next review automatically

### Question Library

Filter by:

- LeetCode number, title, or tracker ID
- Source: LeetCode, custom Python/data engineering, or SQL
- Pattern
- Category
- Difficulty
- Status
- Confidence
- Due date
- Mistake tag

### Review Queue

- Overdue questions
- Questions due today
- Questions due this week
- Lowest-confidence questions
- Frequently missed questions

### Progress

- Attempts over time
- Confidence over time
- Questions completed by category
- Average practice time by category
- Mistakes by type

### Study library

- Public interview guides and system-design notes under `docs/`
- SQL exercises under `sql/`
- Company preparation under `companies/`
- Operational study plans under `study/`

## Automatic solution discovery

The dashboard synchronizes the public solution catalog every time it opens. It registers:

- `leetcode_python/**/*.py`, excluding package `__init__.py` files
- `sql/**/*.sql`

Numbered filenames such as `0875_koko_eating_bananas.py` become LeetCode records. Non-numbered
Python files become custom exercises, so data-engineering coding problems do not receive invented
LeetCode numbers. SQL records use their folder and filename for a stable tracker ID.

Run synchronization without opening Streamlit with:

```bash
make sync
```

Existing records are matched by file path and are never overwritten. Optional `Title:`,
`Difficulty:`, and `Primary Pattern:` headers improve inferred metadata.

## Data files

- `tracker/questions.json` — current question state
- `tracker/practice_log.json` — append-only attempts
- `tracker/study_plan.json` — generated daily plans and task status

The dashboard uses atomic JSON writes. Do not edit a tracker file while submitting a dashboard form.

## No AI key required

The dashboard works with `AI_ENABLED=false` and without an OpenAI API key. Optional AI feedback is separate from progress tracking.
