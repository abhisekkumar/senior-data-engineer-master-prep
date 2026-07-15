# Common Python Interview Errors

- **Mutable defaults:** use `None` and create a new list/dictionary inside the function.
- **Aliasing:** shallow copies still share nested objects.
- **Off-by-one ranges:** say whether an interval is inclusive or half-open.
- **Accidental quadratic work:** repeated slicing, string concatenation, or front-of-list removal can
  dominate the intended algorithm.
- **Truthiness mistakes:** `0`, `False`, an empty value, and a missing value may have different
  meanings.
- **Heap direction:** `heapq` is a min-heap; document negation or tuple ordering.
- **Operand order:** stack evaluation must preserve left/right order for subtraction and division.
- **Mutation while iterating:** changing a collection during traversal can skip or duplicate work.
- **Recursion depth:** a correct recursive graph/tree solution may still exceed Python's call limit.
- **Shared rows:** `[[0] * cols] * rows` aliases every row; use a comprehension.

When reviewing a draft, record these issues for correction. Do not silently rewrite code inside a
preserved original-solution block.
