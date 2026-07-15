# Pattern Recognition

> Publication note: reorganized as an educational template. Employer-specific details are removed; all scenarios, metrics, and identifiers are fictionalized placeholders and are not claims about the maintainer's employment.

| Problem                   | Main Idea                |
| ------------------------- | ------------------------ |
| Remove Duplicates         | Compare with previous    |
| Move Zeroes               | Move valid values        |
| Merge Arrays              | Merge from back          |
| Two Sum II                | Opposite pointers        |
| Container With Most Water | Move limiting pointer    |
| 3Sum                      | Fix one + Two Sum II     |
| Merge Intervals           | Merge overlapping ranges |
| Insert Interval           | Merge while inserting    |

| LeetCode Pattern          | Real Data Engineering                   |
| ------------------------- | --------------------------------------- |
| Remove Duplicates         | `dropDuplicates()`, `ROW_NUMBER()`      |
| Move Zeroes               | Null cleanup, data quality              |
| Merge Sorted Arrays       | CDC, Bronze→Silver merge, Kafka merge   |
| Two Sum II                | Record matching                         |
| Container With Most Water | Resource optimization (conceptual)      |
| 3Sum                      | Multi-table reconciliation              |
| Merge Intervals           | Eligibility windows, provider schedules |
| Insert Interval           | SCD updates, effective date insertion   |
| Interval Intersection     | Calendar overlap, patient eligibility   |

## Interview Tip

This is one of the first things interviewers look for:

## * Array problem?
    * left = 0
    * right = len(nums) - 1
## * Version numbers / IDs from 1 to n?
    * left = 1
    * right = n

Every Problem in Phase 3 has the same complexity
| Problem                    | Time         | Space  |
| -------------------------- | ------------ | ------ |
| #704 Binary Search         | `O(log n)`   | `O(1)` |
| #35 Search Insert Position | `O(log n)`   | `O(1)` |
| #278 First Bad Version     | `O(log n)`   | `O(1)` |
| #34 First & Last Position  | `O(log n)`   | `O(1)` |
| #33 Rotated Sorted Array   | `O(log n)`   | `O(1)` |
| #153 Find Minimum          | `O(log n)`   | `O(1)` |
| #875 Koko Eating Bananas   | `O(n log m)` | `O(1)` |
| #1011 Ship Packages        | `O(n log m)` | `O(1)` |

| Problem                    | Final Return    | Why?                                                |
| -------------------------- | --------------- | --------------------------------------------------- |
| #704 Binary Search         | `mid`           | We found the exact index.                           |
| #35 Search Insert Position | `left`          | `left` ends at the insertion boundary.              |
| #278 First Bad Version     | `answer`        | We saved the best boundary candidate.               |
| #34 Search Range           | `[first, last]` | We tracked both boundaries separately.              |
| #33 Rotated Search         | `mid`           | We found the target's index.                        |
| #153 Find Minimum          | `nums[left]`    | `left` and `right` converge on the minimum element. |

Notice the difference

For array search problems (#704, #33)

These matter:

## * Is the array sorted?
## * Duplicates?
## * Return index or value?
## * Empty array?

⸻

For optimization problems (#875)

These matter:

## * Is a solution guaranteed?
## * Range of values?
## * Constraints?
## * What exactly is being minimized/maximized?

⸻

Interview Tip

Don't memorize one list of clarifying questions.

Instead ask yourself:

“What assumptions does my algorithm depend on?”

For Binary Search on an array, your algorithm depends on:

* Sorted order
* Duplicates
* Output type

For Binary Search on the answer, your algorithm depends on:

* Search range
* Validity of solutions
* Constraints

⸻

## Here's a framework I teach Senior candidates

Before every problem, mentally classify it.

Category 1 — Searching an array

Ask:

## * Is it sorted?
## * Duplicates?
## * Empty?
## * Return index/value?

⸻

Category 2 — Intervals

Ask:

## * Sorted?
## * Overlapping?
## * Inclusive boundaries?
## * Can intervals be empty?

⸻

Category 3 — Graph

Ask:

## * Directed or undirected?
## * Weighted?
## * Cycles?
## * Connected?

⸻
---
## Phase 4 — Binary Search on Answer
---
Ask:

## * Is a solution guaranteed?
## * What exactly am I minimizing/maximizing?
## * What is the search range?
## * How do I verify a candidate solution?

Pattern Recognition
| Koko                         | Shipping                |
| ---------------------------- | ----------------------- |
| Guess speed                  | Guess capacity          |
| Can finish within `h` hours? | Can ship within `days`? |
| If yes, try smaller          | If yes, try smaller     |
| If no, try bigger            | If no, try bigger       |

| Problem           | `left`         | `right`        | Why?                                                                                  |
| ----------------- | -------------- | -------------- | ------------------------------------------------------------------------------------- |
| **Koko**          | `1`            | `max(piles)`   | Speed can't be less than 1 or greater than the largest pile.                          |
| **Ship Packages** | `max(weights)` | `sum(weights)` | Ship must carry the heaviest package; at most it carries everything in [illustrative scale].       |
| **Split Array**   | `max(nums)`    | `sum(nums)`    | A subarray must contain the largest element; at most the whole array is one subarray. |

Interview Recognition: Binary Search on Slope
If you see something like:

Find Peak
Local Maximum
Mountain Array
Find a Turning Point

## Phase 4: Sliding Windows

subarray
contiguous
size k

## Does it say?
subarray
substring
contiguous
Then: Probably Sliding Window.

Does it also say:
size = k
Then: Fixed window

## or does it say?
longest
shortest
minimum
maximum
at least
at most
Then: Variable Window

In Fixed Sliding Window, we already know the first window because its size is fixed (k),
so we initialize it before the loop. In Variable Sliding Window, we don't know how large
the window should become, so we start with an empty window (window_sum = 0) and expand
it one element at a time starting from right = 0.

Fixed Sizing Window
## Why am I shrinking?
Only two answers exist.
I'm shrinking because…

I want the smallest valid window.

Then: while window_is_valid (SHRINK)

I'm shrinking because…
The window became invalid.

Then: while window_is_invalid (SHRINK UNTIL IT BECOMES VALID AGAIN)

Interview Cheatsheet:

GOAL                         WHILE condition
Smallest valid window         while valid
Largest valid window          while invalid

| Problem | Window Invalid     | Answer  |
| ------- | ------------------ | ------- |
| #209    | sum >= target      | minimum |
| #3      | duplicate          | maximum |
| #76     | formed == required | minimum |
| #340    | len(window) > k    | maximum |

---
## Phase 5: Stack
---
Whenever I need to find the first greater (or smaller) element to the right
(or left) for every element, a monotonic stack is a strong candidate.

---
## Phase 6: Heap & Priority Queue
---
Recognition Cheat Sheet

| Interview Says...     | Think...       |
| --------------------- | -------------- |
| Top K                 | Min Heap       |
| Largest K             | Min Heap       |
| Smallest K            | Max Heap       |
| K Closest             | Heap           |
| Continuously updating | Streaming Heap |
| Priority              | Priority Queue |
| Merge K Streams       | Heap           |
| Scheduler             | Heap           |
| Running Median        | Two Heaps      |

Kth Largest
Keep the largest K elements.
Among those K, the one you're most willing to throw away is the smallest.
➡️ Use a Min Heap.

Kth Smallest
Keep the smallest K elements.
Among those K, the one you're most willing to throw away is the largest.
➡️ Use a Max Heap.

| Question     | Heap         | Root Represents              |
| ------------ | ------------ | ---------------------------- |
| Kth Largest  | **Min Heap** | Smallest among the largest K |
| Kth Smallest | **Max Heap** | Largest among the smallest K |

Heap = Partially Ordered Tree
Root
↓
Children
↓
Grandchildren

Think MIN HEAP:
Kth Largest
Top K
Largest K

The actual pattern
Whenever the interviewer says:

* Top K
* Largest K
* Most Frequent K
* Closest K
* Highest Priority K

Immediately think:

“I probably need a heap of size K.”
Then ask yourself one question:
## What should each heap node store?

---
## Phase 7: Trees
---

## The recursive pattern

This is the pattern you'll use over and over during the Trees phase:
if not root:
    return ...

left = self.function(root.left)
right = self.function(root.right)

return combine(left, right)

DFS Pattern:
if not root:
    return ...

left = dfs(root.left)
right = dfs(root.right)

return ...
* ✅ Maximum Depth
* ✅ Same Tree
* ✅ Balanced Tree

BFS Pattern:
queue = deque([root])

while queue:

    level_size = len(queue)

    for _ in range(level_size):
        ...
* ✅ Level Order Traversal

| Problem                | Time | Space                           | Why                                      |
| ---------------------- | ---- | ------------------------------- | ---------------------------------------- |
| #104 Maximum Depth     | O(n) | O(h)                            | Visit every node                         |
| #100 Same Tree         | O(n) | O(h)                            | Compare every node                       |
| #110 Balanced Tree     | O(n) | O(h)                            | One DFS over all nodes                   |
| #102 Level Order       | O(n) | O(w)                            | Queue stores one level (`w` = max width) |
| #98 Validate BST       | O(n) | O(h)                            | Every node checked once                  |
| #236 LCA (Binary Tree) | O(n) | O(h)                            | May explore the whole tree               |
| #235 LCA (BST)         | O(h) | O(h) recursive / O(1) iterative | Only one path is explored                |

---
## Phase 8: Graphs
---

DFS Template
def dfs(node):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            dfs(neighbor)

BFS Template
queue = deque([start])

visited = {start}

while queue:

    node = queue.popleft()

    for neighbor in graph[node]:

        if neighbor not in visited:

            visited.add(neighbor)

            queue.append(neighbor)

Course Cycle:
             Start DFS
                 │
                 ▼
           path.add(course)
                 │
        Explore prerequisites
                 │
        ┌────────┴────────┐
        │                 │
    Cycle?            No Cycle
        │                 │
   return False      path.remove(course)
                          │
                    visited.add(course)
                          │
                     return True

"Is this a traversal problem, a cycle detection problem, or a shortest path problem?"
| If you hear...               | Think...                                   |
| ---------------------------- | ------------------------------------------ |
| Matrix / neighbors           | Grid DFS/BFS                               |
| Copy graph                   | DFS + HashMap                              |
| Dependencies / prerequisites | DFS + `path` + `visited` (cycle detection) |
| Shortest path (unweighted)   | BFS                                        |
| Weighted shortest path       | Dijkstra                                   |
