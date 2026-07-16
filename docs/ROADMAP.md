# Preparation Roadmap Guide

The Preparation Roadmap is an editable curriculum layered on top of the existing catalog,
spaced-repetition scheduler, practice log, and study library. It stays intentionally lightweight:
one program contains preparation stages, stages contain subject modules, and modules contain
actionable items.

## Hierarchy and item types

```text
Program
└── Preparation stage
    └── Module
        └── Roadmap item
```

A roadmap item may link to zero, one, or many catalog questions and study resources. It may also
stand alone as Python fundamentals, SQL, Spark, data engineering, system design, behavioral,
GenAI, real-world production work, a mock interview, documentation, or a custom task. This avoids
forcing non-coding preparation into the question catalog.

Stable entity IDs are stored with the curriculum. Display order is editable and is never used as
identity.

## Readiness and progress

Required, non-skipped items determine weighted completion:

| Status | Weight |
|---|---:|
| Not started | 0% |
| Learning | 25% |
| Practicing | 50% |
| Interview ready | 85% |
| Mastered | 100% |
| Skipped | Excluded |

Optional items stay visible but do not block completion. A module is ready when every required,
non-skipped item is Interview ready or Mastered. The dashboard also reports linked low-confidence
questions and overdue linked reviews.

Roadmap status is deliberately independent from question status and confidence. A completed
question may remain Practicing in the roadmap until the candidate can solve it without help,
explain the brute-force and optimal approaches, state complexity, and handle follow-ups. Roadmap
associations never copy or modify question history.

## Default editable curriculum

On first use only, the app creates **Senior Data Engineering Master Prep** with four preparation
stages and subject **Modules A–V** covering coding patterns, Python, SQL, Spark, architecture,
system design, GenAI, behavioral preparation, real-world problems, and mocks. Module A includes
items grouped by duplicate detection, hash-map lookup, frequency counting,
grouping/normalization, sequence detection, and production extensions.

Known Module A questions are linked only when their tracker IDs exist. Missing questions do not
break initialization. Every default name, module, item, requirement, and association can be edited
from localhost; dashboard code does not hardcode how the user must progress after seeding.

## Editing and assigning questions

Open **Roadmap → Edit curriculum** to create, rename, reorder, archive, or restore stages; create,
rename, move, reorder, archive, or restore modules; and create, edit, move, reorder, or delete items. Destructive
operations require confirmation and create a snapshot when possible.

Automatic catalog synchronization remains unchanged. A newly discovered Python or SQL solution
appears under **Unassigned questions** until the user selects a destination module. If a linked
question later disappears, the roadmap item and original ID remain visible with an unresolved-link
warning.

## Today's Five

For a new day, the planner prefers:

1. An overdue roadmap-linked review.
2. A current-stage coding review.
3. A current-stage new, Learning, or Practicing item.
4. A SQL, Python, Spark, data-engineering, documentation, or system-design item.
5. A real-world, behavioral, GenAI, custom, or mock-interview item.

The original scheduler fills unavailable slots. Existing saved daily plans are not regenerated.
When completing a linked task, the user selects a roadmap status; no task completion automatically
means Mastered. Automatic stage advancement is gated until all required, non-skipped items are at
least Interview ready. Manual advancement before that point requires an explicit override.

## Real-world problems

Real-world items can keep draft scenario fields in roadmap data and link to a public Markdown
exercise. Use [`REAL_WORLD_PROBLEM_TEMPLATE.md`](REAL_WORLD_PROBLEM_TEMPLATE.md) for business
scenario, assumptions, constraints, clarifying questions, local/SQL/Spark approaches, complexity,
data quality, reliability, scaling, canonical patterns, and interviewer follow-ups. Empty fields
are allowed while a draft develops. Use synthetic, employer-neutral examples only.

## Local storage, export, and recovery

Personal state defaults to:

```text
.local/roadmap.json
.local/history/roadmap/roadmap-<timestamp>.json
```

`.local/` is gitignored. Writes are atomic and the complete document is validated before saving.
Malformed data is reported and left untouched. Seeding never runs over an existing file. Existing
schema 1 roadmaps are snapshotted and migrated once so the former A–V subjects become modules;
item IDs, links, status, notes, and practice associations are preserved.

Settings can move roadmap storage to another local directory without deleting the previous file.
JSON export preserves the editable machine-readable plan. Markdown export creates a readable
review checklist. Import validates first, snapshots the current version, and then replaces it.
Snapshot restore also keeps a recovery copy of the version being replaced.

## Future improvements

- User-configurable status weights after a real need emerges.
- More seeded items across Modules B–V, based on original employer-neutral exercises.
- Optional weekly roadmap readiness summaries and mock feedback trends.
- Additional tests around simultaneous writes if the dashboard gains multi-user support.
