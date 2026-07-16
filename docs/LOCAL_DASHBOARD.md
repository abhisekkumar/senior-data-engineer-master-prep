# Local Progress Dashboard

The repository includes a lightweight Streamlit dashboard. It runs entirely on your machine,
requires no authentication, and keeps question/practice data under `tracker/` plus personal
roadmap state in gitignored `.local/` storage.

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
- Prioritizes overdue and current-phase roadmap items when an active roadmap phase has suitable work
- Lets you select a separate roadmap status after completing a linked daily item

### Roadmap

- Shows the active program and phase, weighted completion, readiness, mastery, overdue reviews,
  weak linked questions, and unassigned catalog questions
- Expands Phase A–V into ordered modules and roadmap items
- Updates an item's Not started, Learning, Practicing, Interview ready, Mastered, or Skipped status
  without changing question confidence
- Filters by phase, module, status, item type, requirement, question link, overdue state,
  confidence, and text
- Creates, edits, reorders, archives, and restores phases
- Creates, edits, moves, and reorders modules and items
- Links multiple catalog questions and study-resource/exercise paths
- Preserves unresolved links and displays a warning when a question record is unavailable
- Assigns newly discovered questions from the Unassigned questions panel
- Supports structured, draft-friendly real-world production exercises

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

### Settings

- Selects the active program, phase, and module
- Enables automatic advancement or manual phase mode
- Requires an explicit override to leave an incomplete phase
- Chooses the default successful-completion roadmap status
- Shows or hides archived phases
- Changes the local roadmap directory without deleting the old file
- Exports JSON or readable Markdown
- Validates imported JSON before creating a snapshot and replacing the roadmap
- Creates and restores local roadmap snapshots

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
- `.local/roadmap.json` — editable personal curriculum and roadmap progress
- `.local/history/roadmap/` — timestamped local roadmap snapshots

The dashboard uses atomic JSON writes. `.local/` is gitignored so personal curriculum progress and
snapshots are not accidentally published. A different local-data directory can be selected under
Settings; a small gitignored location pointer lets the app find it on the next restart. The old
roadmap is preserved when moving storage.

Seeding happens only when no roadmap exists. The initial editable program is **Senior Data
Engineering Master Prep**, with Phase A–V defaults and detailed Phase A modules. Existing roadmap
files are validated and never replaced by seed data. Malformed files produce an error and remain
untouched.

## Question status versus roadmap status

These states serve different purposes:

- Question status/confidence records whether a catalog exercise was attempted, how independently it
  was solved, and when it is due for spaced repetition.
- Roadmap status records curriculum readiness for the broader interview objective, including
  explanation, trade-offs, follow-ups, and production extensions.

Assigning, moving, unlinking, or deleting a roadmap item never removes the question record or its
append-only practice history.

## Editing the curriculum

1. Open **Roadmap → Edit curriculum**.
2. Create or select a phase, module, or item.
3. Link existing question IDs or public study-resource paths as needed.
4. Save; the page refreshes immediately and the change survives restarts.

New Python and SQL files continue to enter the automatic catalog but are not forced into a phase.
Assign them from **Roadmap → Unassigned questions**. For production scenarios, start a linked file
from [`REAL_WORLD_PROBLEM_TEMPLATE.md`](REAL_WORLD_PROBLEM_TEMPLATE.md) and keep examples synthetic.

## Roadmap recovery and portability

Use **Settings** to download the current plan as JSON or Markdown. JSON import is an advanced
replace operation: the app validates the entire document, snapshots the current file, then writes
atomically. Archive, delete, import, relocation, and restore workflows retain local recovery
versions under `.local/history/roadmap/` where possible.

## No AI key required

The dashboard works with `AI_ENABLED=false` and without an OpenAI API key. Optional AI feedback is separate from progress tracking.
