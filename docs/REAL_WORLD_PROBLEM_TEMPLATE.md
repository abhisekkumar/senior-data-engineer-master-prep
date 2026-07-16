# Real-World Data Engineering Problem Template

Use this template for original, employer-neutral production exercises. Keep examples synthetic and
exclude private architecture, personal data, protected health information, credentials, and
confidential interview material. A draft does not need every section completed.

## Problem metadata

- **Title:**
- **Roadmap stage/module:**
- **Canonical patterns:**
- **Target duration:**
- **Status:** Not started / Learning / Practicing / Interview ready / Mastered

## Business scenario

Describe the business outcome and the synthetic data involved.

## Input assumptions

- Data shape and example records:
- Expected output:
- Ordering, uniqueness, and null assumptions:

## Constraints

- Expected volume:
- Latency or freshness target:
- Memory and compute constraints:
- Exactness requirements:

## Clarifying questions

1. What defines a duplicate, match, or valid record?
2. Is the input bounded, ordered, replayable, or late arriving?
3. What should happen to malformed or ambiguous records?

## Brute-force approach

Explain the simplest correct local approach and why it becomes expensive.

- **Time complexity:**
- **Space complexity:**

## Optimal local approach

Explain the data structure, invariant, algorithm, and correctness argument.

- **Time complexity:**
- **Space complexity:**

## SQL interpretation

Describe the relational model, query strategy, indexes/partition pruning, and deterministic tie
handling.

## Spark or distributed interpretation

Describe partition keys, shuffles, skew, state, checkpointing, and idempotent writes.

## Data-quality considerations

- Completeness and validity checks:
- Uniqueness and reconciliation checks:
- Quarantine and correction workflow:

## Reliability considerations

- Retry and idempotency behavior:
- Failure recovery and replay:
- Observability, alerts, and service-level indicators:

## Scaling follow-ups

- What changes when the data does not fit in memory?
- When is external sorting preferable to hashing?
- When is a probabilistic structure acceptable?

## Interviewer follow-ups

- How would you test this with duplicate-heavy and late-arriving data?
- Which trade-off would change under a stricter latency or exactness requirement?
- How would you explain the design in two minutes?

## Completion notes

Record what was completed, remaining gaps, confidence, and the next review date.
