# Complexity Guide

Define variables before stating a bound. For example, use `n` for total input elements, `m` for
unique values, `k` for requested results, and `V`/`E` for graph vertices and edges.

## Common operations

| Operation | Typical time | Notes |
|---|---:|---|
| List or string scan | `O(n)` | Count nested or repeated scans separately |
| Hash lookup/update | `O(1)` average | State when worst-case behavior matters |
| Sort | `O(n log n)` | Include sorting even when the later scan is linear |
| Heap push/pop | `O(log k)` | Use `k` when the heap is intentionally bounded |
| Binary search | `O(log n)` | Multiply by feasibility-check cost for answer search |
| BFS/DFS | `O(V + E)` | Grid traversal is usually `O(rows × columns)` |

## Space rules

- Count auxiliary maps, sets, heaps, queues, recursion stacks, and copied slices.
- State whether output storage is excluded from auxiliary-space analysis.
- In-place mutation is not automatically `O(1)` if recursion or hidden copies are used.
- A hash map containing all unique values is `O(m)`, which may equal `O(n)` in the worst case.

## Explanation checklist

- Explain why each loop or data-structure operation creates the stated bound.
- Distinguish total input size from the number of unique items.
- For nested loops, decide whether pointers only move forward before declaring `O(n²)`.
- For recursion, include maximum call-stack depth.
- State average-case hash behavior when it materially affects the claim.
