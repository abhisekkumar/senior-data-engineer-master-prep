# Interview Workflow

Use the same sequence until it becomes automatic:

1. **Restate the problem.** Define the input, required output, and objective in your own words.
2. **Clarify the contract.** Ask only relevant questions about empty input, duplicates, ordering,
   mutation, return type, ties, constraints, and memory.
3. **Walk through an example.** Choose the smallest example that exposes the core behavior.
4. **Establish a baseline.** Explain a correct brute-force approach, why it works, its time and
   space bounds, and why it may not scale.
5. **Recognize the pattern.** Connect constraints and output shape to a reusable pattern and state
   the invariant.
6. **Derive the optimal approach.** Explain the data structures, algorithm, bounds, and trade-offs
   before coding.
7. **Write readable Python.** Prefer clear names, type hints, direct control flow, and the expected
   return contract.
8. **Dry-run the implementation.** Trace the important state changes on a meaningful example.
9. **Test edge cases.** Cover only cases allowed or implied by the contract.
10. **Discuss follow-ups.** Consider memory, in-place behavior, streaming, large data, Spark, and
    output ordering when relevant.
11. **Record the attempt.** Log time, hints, mistakes, communication/complexity scores, confidence,
    and the next review date.
