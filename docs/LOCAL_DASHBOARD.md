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

## Data files

- `tracker/questions.json` — current question state
- `tracker/practice_log.json` — append-only attempts
- `tracker/study_plan.json` — generated daily plans and task status

The dashboard uses atomic JSON writes. Do not edit a tracker file while submitting a dashboard form.

## No AI key required

The dashboard works with `AI_ENABLED=false` and without an OpenAI API key. Optional AI feedback is separate from progress tracking.
