# One-Month Senior Data Engineering Interview Study Plan

This plan is designed for consistent daily practice without turning the repository into a complicated application. Standard learning days contain five focused items and should take approximately 90–150 minutes.

## Use this plan with the Preparation Roadmap

The written 28-day plan is a suggested sequence; the dashboard roadmap is the editable source for
your current stage, modules, and readiness. Question completion/confidence and roadmap readiness are
separate: keep an item at Learning or Practicing until you can explain the recognition clue,
complexity, trade-offs, and follow-ups independently.

- Open **Roadmap** to update individual item status and review stage/module completion.
- Use **Edit curriculum** to add or rearrange stages, modules, real-world problems, and resources.
- Assign automatically discovered Python and SQL questions from **Unassigned questions**.
- Choose the active stage and module under **Settings**.
- Enable automatic advancement only if you want the app to move after every non-skipped required
  item reaches at least Interview ready.
- Export JSON for a restorable plan or Markdown for a readable review copy.

## Daily five-item format

Use this order on every standard learning day:

1. **Coding review** — one completed Python/DSA question that is due or overdue.
2. **Coding growth** — one new, weak, or low-confidence Python/DSA question.
3. **Language or SQL** — one Python fundamentals, debugging, or SQL exercise.
4. **Senior data engineering** — one Spark, data engineering, or system-design topic.
5. **Communication** — one behavioral, project explanation, GenAI, incident, or troubleshooting prompt.

After each coding attempt:

- Record confidence before and after.
- Record time spent.
- Record hints used.
- Record mistakes and unclear reasoning.
- State time and space complexity aloud.
- Schedule the next review through the tracker.

## Week 1 — Stabilize Foundations

### Focus

- Arrays and hashing
- Frequency counting
- Core Python behavior
- SQL window functions
- Spark fundamentals
- Functional and non-functional system requirements
- Introduction and complex-pipeline stories

### Suggested coding topics

- Contains Duplicate
- Two Sum
- Valid Anagram
- Group Anagrams
- Top K Frequent Elements

### Daily schedule

#### Day 1 — Hash-map foundations

- Review: Contains Duplicate
- New/weak: Two Sum
- Python/SQL: dictionary lookup and `dict.get`
- Data engineering: batch versus streaming ingestion
- Communication: 90-second professional introduction

#### Day 2 — Frequency counting

- Review: Two Sum
- New/weak: Valid Anagram
- Python/SQL: `Counter`, dictionary counts, and duplicate rows
- Data engineering: Bronze, Silver, and Gold responsibilities
- Communication: explain the most complex pipeline you built

#### Day 3 — Grouping by signature

- Review: Valid Anagram
- New/weak: Group Anagrams
- Python/SQL: `ROW_NUMBER`, `RANK`, and `DENSE_RANK`
- Data engineering: Spark partitions, transformations, and actions
- Communication: clarify requirements before proposing a solution

#### Day 4 — Ranking and heaps

- Review: Group Anagrams
- New/weak: Top K Frequent Elements
- Python/SQL: heap operations and min-heap behavior
- Data engineering: functional and non-functional requirements
- Communication: explain a difficult technical trade-off

#### Day 5 — Mixed retrieval

- Review: the lowest-confidence Week 1 question
- New/weak: Top K Frequent Words or another frequency problem
- Python/SQL: window-function practice
- Data engineering: data-quality dimensions and validation gates
- Communication: explain an incident from detection through prevention

#### Day 6 — Practice day

- Solve two Week 1 coding questions without notes.
- Complete one timed SQL window-function exercise.
- Explain one Spark concept on a whiteboard.
- Review the mistake log.
- Regenerate overdue review dates.

#### Day 7 — Mixed mock day

- Complete one timed coding question.
- Complete one SQL question.
- Explain one data-platform design.
- Deliver one behavioral story.
- Record feedback and next-week priorities.

### End-of-week outcomes

- One practice day completed
- One mixed mock completed
- Every Week 1 question assigned a confidence score
- Mistake log updated with recurring themes

## Week 2 — Pattern Recognition

### Focus

- Prefix sums
- Sliding windows
- Two pointers
- Binary search
- Intervals
- SQL joins
- Change Data Capture
- Schema evolution
- Pipeline reliability

### Suggested coding topics

- Subarray Sum Equals K
- Longest Substring Without Repeating Characters
- 3Sum
- Merge Intervals
- Binary Search

### Daily schedule

#### Day 8 — Prefix sums

- Review: one due Week 1 question
- New/weak: Subarray Sum Equals K
- Python/SQL: cumulative sums and running totals
- Data engineering: CDC events and replay
- Communication: explain why brute force does not scale

#### Day 9 — Sliding windows

- Review: Subarray Sum Equals K
- New/weak: Longest Substring Without Repeating Characters
- Python/SQL: fixed versus variable windows
- Data engineering: watermark and late-data policy
- Communication: explain a production reliability improvement

#### Day 10 — Two pointers

- Review: longest unique substring
- New/weak: 3Sum
- Python/SQL: sorted-input recognition
- Data engineering: inner, left, and full outer joins
- Communication: ask clarifying questions for ambiguous requirements

#### Day 11 — Intervals

- Review: 3Sum
- New/weak: Merge Intervals
- Python/SQL: interval overlap conditions
- Data engineering: schema compatibility and evolution
- Communication: describe a cross-team disagreement and resolution

#### Day 12 — Binary search

- Review: Merge Intervals
- New/weak: Binary Search
- Python/SQL: lower and upper boundaries
- Data engineering: idempotency and retry behavior
- Communication: explain monitoring and service-level indicators

#### Day 13 — Pattern-recognition practice

- Classify ten prompts without coding.
- State the likely pattern and recognition clue for each.
- Solve two randomly selected questions.
- Review complexity mistakes.
- Update confidence scores.

#### Day 14 — Technical mock interview

- Complete one timed coding problem.
- Complete one SQL or data-reconciliation problem.
- Design a CDC pipeline.
- Explain failure recovery and observability.
- Record interviewer-style feedback.

### End-of-week outcomes

- One pattern-recognition practice day completed
- One technical mock completed
- Prefix sum, sliding window, two pointers, intervals, and binary search reviewed
- Weak patterns added to the Week 3 review queue

## Week 3 — Senior-Level Engineering

### Focus

- Heaps
- Advanced binary search
- Backfills
- Data skew
- Spark debugging
- Data-platform design
- Kafka partitioning
- Reliability and observability
- Leadership stories

### Suggested coding topics

- Capacity to Ship Packages Within D Days
- Heap-based Top K
- Insert Interval
- Contiguous Array
- Longest Consecutive Sequence

### Daily schedule

#### Day 15 — Binary search on the answer

- Review: one overdue Week 1–2 question
- New/weak: Capacity to Ship Packages Within D Days
- Python/SQL: boundary invariants
- Data engineering: safe historical backfills
- Communication: justify a design trade-off

#### Day 16 — Heap selection

- Review: shipping capacity
- New/weak: Kth Largest Element or heap-based Top K
- Python/SQL: heap size and direction
- Data engineering: Kafka partition keys and consumer groups
- Communication: explain a high-impact technical decision

#### Day 17 — Interval insertion

- Review: heap selection
- New/weak: Insert Interval
- Python/SQL: deterministic merge logic
- Data engineering: skew detection and mitigation
- Communication: describe how you influenced without authority

#### Day 18 — Prefix-state reasoning

- Review: Insert Interval
- New/weak: Contiguous Array
- Python/SQL: state maps and balance transformations
- Data engineering: reading Spark UI metrics
- Communication: explain an incident root-cause analysis

#### Day 19 — Set-based sequences

- Review: Contiguous Array
- New/weak: Longest Consecutive Sequence
- Python/SQL: membership versus sorting trade-offs
- Data engineering: reliability, lineage, and reconciliation
- Communication: leadership and mentoring story

#### Day 20 — Production-incident simulation

- Diagnose a delayed or incorrect pipeline.
- Identify detection gaps.
- Propose immediate mitigation.
- Propose long-term prevention.
- Define operational metrics and alerts.

#### Day 21 — Senior data engineering mock

- Complete one medium coding problem.
- Complete one SQL/data-quality exercise.
- Design a scalable data platform.
- Explain Spark or Kafka bottlenecks.
- Deliver one leadership story and record feedback.

### End-of-week outcomes

- One production-incident simulation completed
- One senior data engineering mock completed
- Advanced binary search, heaps, Kafka, Spark, and reliability reviewed
- Top recurring mistakes selected for Week 4 correction

## Week 4 — Interview Simulation

### Focus

- Weakest coding patterns
- Mixed retrieval
- Timed coding
- Verbal explanations
- Complexity accuracy
- System-design trade-offs
- Behavioral delivery
- Company-specific simulations

### Daily schedule

#### Day 22 — Weak-pattern repair

- Review the lowest-confidence coding question.
- Solve a second question from the same pattern.
- Correct one complexity-explanation mistake.
- Review one related system-design concept.
- Explain what recognition clue was previously missed.

#### Day 23 — Timed mixed coding

- Complete one easy question in 15 minutes.
- Complete one medium question in 30 minutes.
- Explain both solutions without notes.
- Review one SQL query.
- Record time, hints, and confidence.

#### Day 24 — System-design simulation

- Clarify functional requirements.
- Clarify scale and non-functional requirements.
- Draw the high-level architecture.
- Discuss bottlenecks, failure modes, and trade-offs.
- Summarize the design in two minutes.

#### Day 25 — Behavioral and project delivery

- Practice the professional introduction.
- Practice the complex-pipeline story.
- Practice an incident story.
- Practice a leadership/conflict story.
- Remove unnecessary detail and confidential context.

#### Day 26 — Company-specific simulation

- Review the company preparation index.
- Complete one representative coding prompt.
- Complete one platform or system-design prompt.
- Practice relevant domain concepts.
- Record gaps without inventing confidential interview content.

#### Day 27 — Full mock interview

- Coding round
- SQL/data-engineering round
- System-design round
- Behavioral round
- Written readiness feedback

#### Day 28 — Mistake correction and readiness assessment

- Re-solve the three most frequently missed questions.
- Correct every unresolved complexity statement.
- Review overdue questions.
- Assess confidence by category.
- Write the final interview-day review list.

### End-of-week outcomes

- One full mock interview completed
- One mistake-correction day completed
- Final readiness assessment written
- Weakest topics scheduled for continued spaced repetition

## Running the plan

Generate today's five items:

```bash
make daily
```

Start the visual tracker:

```bash
make dashboard
```

Open the URL printed by Streamlit, normally `http://localhost:8501`.

Today's Five first looks for an overdue roadmap-linked review, then current-phase coding review and
growth work, then technical and communication/real-world items. The existing scheduler fills any
empty slot. Completing a daily task updates its daily status; you choose any roadmap status change
explicitly, and the app never infers Mastered from a checkbox.
