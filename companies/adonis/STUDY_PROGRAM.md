# Study Program

> Publication note: reorganized as an educational template. Employer-specific details are removed; all scenarios, metrics, and identifiers are fictionalized placeholders and are not claims about the maintainer's employment.

Absolutely. I actually want to turn this into your Master Data Engineering Coding Curriculum, not just an Adonis plan.

This is something you'll keep for years and use for Meta, Databricks, Snowflake, OpenAI, Anthropic,
Stripe, Airbnb, Netflix, etc.

⸻

## Master Coding Curriculum

✅ Completed
🟡 Skipped but needs to complete later

Senior / Staff Data Engineer
Target Companies
* Adonis
* Komodo Health
* Arlo
* Meta
* Databricks
* Snowflake
* Airbnb
* Stripe
* OpenAI
* Anthropic

Duration: June 30 - July 13 ([illustrative scale])

Primary Goal
Pass Adonis Coding Interview while building long-term Senior Data Engineering coding skills.

## Daily Study Routine

| Task                      | Duration | Status |
| ------------------------- | -------- | ------ |
| Review previous problems  | 20 min   | ⬜      |
| Learn new pattern         | 45 min   | ⬜      |
| Solve 3 LeetCode problems | 90 min   | ⬜      |
| Debugging exercise        | 30 min   | ⬜      |
| Platform coding exercise  | 45 min   | ⬜      |
| Mock discussion           | 20 min   | ⬜      |

Total:
[illustrative scale]/day

✅ PHASE 0 — Interview Framework
Objective
Learn how to interview, not just solve problems.
| Status | Topic                | Goal                            |
| ------ | -------------------- | ------------------------------- |
| ✅      | Clarifying Questions | Never jump directly into coding |
| ✅      | Think Aloud          | Explain every decision          |
| ✅      | Brute Force          | Discuss naive approach          |
| ✅      | Optimization         | Improve solution                |
| ✅      | Complexity           | Time & Space                    |
| ✅      | Dry Run              | Verify logic                    |
| ✅      | Edge Cases           | Production thinking             |

✅ PHASE 1 — Hash Maps & Sets (Highest Priority)

## ✅ Phase 1A Easy
| Status | Pattern           | LeetCode                            | Platform Equivalent       |
| ------ | ----------------- | ----------------------------------- | ------------------------- |
| ✅      | HashMap Lookup    | #1 Two Sum                          | Patient lookup            |
| ✅      | Set Lookup        | #217 Contains Duplicate             | Remove duplicate patients |
| ✅      | Frequency Counter | #242 Valid Anagram                  | Provider frequency        |
| ✅      | defaultdict       | #49 Group Anagrams                  | Group providers           |
| ✅      | Set Difference    | #2215 Find Difference of Two Arrays | Data reconciliation       |
| ✅      | Counter           | #347 Top K Frequent                 | Top providers by claims   |
| ✅      | Cycle Detection   | #202 Happy Number                   | Duplicate detection logic |

✅ PHASE 1B: Platform Practices
| Status | Exercise                 |
| ------ | ------------------------ |
| ✅      | Deduplicate Patients     |
| ✅      | Missing Claims Detection |
| ✅      | Provider Lookup          |
| ✅      | Record Reconciliation    |
| ✅      | Duplicate Member IDs     |

✅ PHASE 1C: Platform Practices

| Status  | Problem                                           | Pattern              |
| ------  | ------------------------------------------------- | -------------------- |
| ✅      | #128 Longest Consecutive Sequence                 | Hash Set             |
| ✅      | #560 Subarray Sum Equals K                        | Prefix Sum + HashMap |
| ✅      | #3 Longest Substring Without Repeating Characters | Sliding Window + Set |
| ✅      | #692 Top K Frequent Words                         | Counter + Heap       |
| ✅      | #523 Continuous Subarray Sum                      | Prefix Sum           |
| ✅      | #525 Contiguous Array                             | Prefix Sum           |

✅ PHASE 2 — Arrays & Two Pointers

✅ PHASE 2A — Easy & Medium

| Status  | Pattern                     | Recognition Clue                              | LeetCode | Difficulty | Platform Equivalent                 |
| ------  | --------------------------- | --------------------------------------------- | -------- | ---------- | ----------------------------------- |
| ✅      | Remove Duplicates           | Sorted array + remove duplicates **in-place** | #26      | Easy       | CDC Deduplication                   |
| ✅      | Move Zeroes                 | Move specific values while preserving order   | #283     | Easy       | Null / Missing Value Handling       |
| ✅      | Merge Sorted Arrays         | Merge two sorted arrays **in-place**          | #88      | Easy       | Incremental Data Merge              |
| ✅      | Two Sum II                  | Sorted array + find target pair               | #167     | Easy       | Merge Two Sorted Feeds              |
| ✅      | Container With Most Water   | Maximize area between two boundaries          | #11      | Medium     | Resource Allocation                 |
| ✅      | 3Sum                        | Find all unique triplets summing to target    | #15      | Medium     | Advanced Record Matching            |
| ✅      | Merge Intervals             | Overlapping ranges or schedules               | #56      | Medium     | Schedule / Time Window Merge        |
| ✅      | Insert Interval             | Insert into sorted intervals                  | #57      | Medium     | Incremental Scheduling              |
| ✅      | Interval List Intersections | Compare two ordered interval lists            | #986     | Medium     | Availability / Appointment Matching |

✅ PHASE 2B — Platform Practice
| Status  | Exercise                       | Concepts                               |
| ------  | ------------------------------ | -------------------------------------- |
| ✅      | Merge Provider Feed            | Two pointers + joins                   |
| ✅      | Merge Patient Snapshot         | SCD / Snapshot logic                   |
| ✅      | Incremental CDC Merge          | MERGE INTO, Delta Lake                 |
| ✅      | Watermark Processing           | Streaming, late arrivals               |
| ✅      | Deduplicate Patient Feed       | In-place thinking vs distributed dedup |
| ✅      | Merge Kafka Event Streams      | Ordered event processing               |
| ✅      | Reconcile Bronze vs Silver     | Pointer comparison                     |
| ✅      | Compare Two Sorted Claim Files | Healthcare reconciliation              |

✅ PHASE 3 — Binary Search

| Status  | Pattern                       | Recognition Clue                 | LeetCode | Difficulty | Platform Equivalent                       |
| ------  | ----------------------------- | -------------------------------- | -------- | ---------- | ----------------------------------------- |
| ✅      | Classic Binary Search         | Find value in sorted array       | #704     | Easy       | Lookup in sorted metadata                 |
| ✅      | Search Insert Position        | Find insertion boundary          | #35      | Easy       | Insert new partition / ordered key        |
| ✅      | First True Boundary           | Find first failing/true item     | #278     | Easy       | First corrupted batch / failed deployment |
| ✅      | First & Last Position         | Duplicates + boundaries          | #34      | Medium     | Event boundary detection                  |
| ✅      | Search Rotated Sorted Array   | Sorted but rotated               | #33      | Medium     | Failover shard lookup                     |
| ✅      | Find Minimum in Rotated Array | Find pivot/minimum               | #153     | Medium     | Partition recovery / leader lookup        |
| ✅      | Binary Search on Answer       | Minimum valid speed              | #875     | Medium     | Executor/cluster sizing                   |
| ✅      | Binary Search on Answer       | Minimum valid capacity           | #1011    | Medium     | Batch sizing / throughput                 |
| ✅      | Binary Search on Answer       | Minimize largest workload        | #410     | Hard       | Partition/workload balancing              |
| ✅      | Peak Search                   | Compare `mid` with `mid+1` slope | #162     | Medium     | Find local max throughput / spike         |
| ✅      | Pair Index Binary Search      | Single value breaks pair pattern | #540     | Medium     | Detect unmatched event / missing pair     |

✅ PHASE 4 — Sliding Windows

| Status  | Pattern                                        | Recognition Clue                                                     | LeetCode                                          | Difficulty | Platform Equivalent                            |
| ------  | -----------------------------------------------| -------------------------------------------------------------------- | ------------------------------------------------- | ---------- | ---------------------------------------------- |
| ✅      | Fixed Window (Running Metric)                  | Fixed window size `k`; maintain a running value (sum, average, etc.) | #643 Maximum Average Subarray                     | Easy       | Rolling averages, moving metrics               |
| ✅      | Variable Window (Minimum Valid)                | Find the **smallest** window satisfying a condition                  | #209 Minimum Size Subarray Sum                    | Medium     | Threshold alerts, minimum batch size           |
| ✅      | Variable Window (Uniqueness)**                 | Longest substring/window with **no duplicates**                      | #3 Longest Substring Without Repeating Characters | Medium     | Unique events, session deduplication           |
| ✅      | Fixed Window + Frequency Map**                 | Fixed-size window; compare character/event frequencies               | #567 Permutation in String                        | Medium     | Event validation, schema signature matching    |
| ✅      | Fixed Window + Frequency Map (Collect Results) | Same as #567, but collect **all** matching windows                   | #438 Find All Anagrams in a String                | Medium     | Find all matching event sequences              |
| ✅      | Variable Window + Frequency Map**              | Expand until all requirements are met, then shrink                   | #76 Minimum Window Substring                      | Hard       | Smallest log window containing required events |
| ✅      | Variable Window + Distinct Count**             | At most / exactly K distinct elements                                | #340 / #904 Longest Substring With Atmost K char  | Medium     | User sessions, device IDs, customer behavior   |
| ✅      | Monotonic Deque Window**                       | Need max/min for every fixed-size window                             | #239 Sliding Window Maximum                       | Hard       | Rolling max latency, CPU peaks, throughput     |

✅🟡 Phase 5 — Stack & Monotonic Stack (Senior Data Engineer / FAANG)

| Status  | Pattern                            | Recognition Clue            | LeetCode                         | Difficulty | Platform Equivalent                    |
| ------  | ---------------------------------- | --------------------------- | -------------------------------- | ---------- | -------------------------------------- |
| ✅      | Basic Stack                        | Push / Pop / Matching pairs | #20 Valid Parentheses            | Easy       | JSON/XML validation                    |
| ✅      | Stack Simulation                   | Reverse processing / Undo   | #1047 Remove Adjacent Duplicates | Easy       | Log cleanup / text processing          |
| ✅      | Min Stack                          | Maintain extra information  | #155 Min Stack                   | Medium     | Streaming minimum metrics              |
| 🟡      | Monotonic Increasing Stack         | Next smaller element        | #84 Largest Rectangle            | Hard       | Capacity planning / histogram analysis |
| ✅      | Monotonic Decreasing Stack         | Next greater element        | #739 Daily Temperatures          | Medium     | Alerting / future event detection      |
| ✅      | Next Greater Element               | Reusable monotonic template | #496                             | Easy       | Stock price / sensor monitoring        |
| 🟡      | Previous Greater/Smaller           | Scan left using stack       | #907 / #2104 concepts            | Medium     | Time-series comparisons                |
| ✅      | Expression Evaluation              | Operators & precedence      | #150 Reverse Polish Notation     | Medium     | Calculator / parser engines            |

| Status | Exercise                              |
| ------ | ------------------------------------- |
| 🟡     | Validate nested JSON structure        |
| 🟡     | Track minimum latency over operations |
| 🟡     | Predict next CPU spike                |
| 🟡     | Storage utilization histogram         |

✅🟡 PHASE 6 — Heap / Priority Queue / LinkedList

✅ PHASE 6A — Heap Fundamentals (Must Know Before Coding)
| Status  | Topic                   | Goal                                                                     |
| ------  | ----------------------- | ------------------------------------------------------------------------ |
| ✅      | Heap vs Stack vs Queue  | Understand when to use each                                              |
| ✅      | Min Heap                | Smallest element always on top                                           |
| ✅      | Max Heap (Python trick) | Use negative values with `heapq`                                         |
| ✅      | `heapq` Operations      | `heapify()`, `heappush()`, `heappop()`, `heappushpop()`, `heapreplace()` |
| ✅      | Heap Complexity         | Build intuition for `O(log n)`                                           |
| ✅      | Heap Visualization      | Binary tree representation                                               |

✅ PHASE 6B(1) — Core Heap Interview Patterns (Highest Priority)
| Status  | Pattern                 | Recognition Clue              | LeetCode | Difficulty | Platform Equivalent                  |
| ------  | ----------------------- | ----------------------------- | -------- | ---------- | ------------------------------------ |
| ✅      | Kth Largest Element     | Kth Largest / Keep Top K      | #215     | Medium     | Top providers by claims              |
| ✅      | Top K Frequent Elements | Frequency + Top K             | #347     | Medium     | Top diagnoses / top customers        |
| ✅      | K Closest Points        | Closest K items               | #973     | Medium     | Nearest warehouse / closest facility |
| ✅      | Streaming Heap          | Continuously maintain Top K   | #703     | Easy       | Live monitoring dashboard            |
| ✅      | Merge K Sorted Lists    | Merge multiple sorted streams | #23      | Hard       | Merge Kafka partitions / CDC feeds   |

✅ PHASE 6B(2) — Core LinkedList Interview Patterns (Highest Priority)
| Status  | Pattern                  | Recognition Clue             | LeetCode | Difficulty | Why It Matters                              |
| ------  | ------------------------ | ---------------------------- | -------- | ---------- | ------------------------------------------- |
| ✅      | Reverse Linked List      | Pointer reversal             | #206     | Easy       | Master pointer manipulation                 |
| ✅      | Merge Two Sorted Lists   | Dummy node + current pointer | #21      | Easy       | Direct prerequisite for #23                 |
| ✅      | Linked List Cycle        | Fast & Slow pointers         | #141     | Easy       | Floyd's algorithm                           |
| ✅      | Remove Nth Node From End | Two pointers                 | #19      | Medium     | Common interview pattern                    |
| ✅      | Merge K Sorted Lists     | Heap + Linked List           | #23      | Hard       | Combines heap with linked list manipulation |

🟡 PHASE 6C — Data Engineering Platform Practice
| Status  | Exercise                           | Concepts           | Maps To
| ------  | ---------------------------------- | ------------------ | ---------
| ⬜      | Top [illustrative scale]                  | HashMap + Min Heap |  #347
| ⬜      | Largest Insurance Claims           | Top K              |  #215
| ⬜      | Streaming Top Users                | Kafka + Heap       |  #347
| ⬜      | Merge Kafka Event Streams          | Heap Merge         |  #23
| ⬜      | Airflow Priority Scheduler         | Priority Queue     |  Priority Queue
| ⬜      | Merge Bronze → Silver Sorted Files | Heap-based Merge   |  #23
| ⬜      | Top N Slowest Spark Jobs           | Monitoring + Heap  |  #215

🟡 PHASE 6D — Advanced Heap Patterns (After Adonis)
| Status  | Pattern                    | Recognition Clue            | LeetCode            | Difficulty | Platform Equivalent  |
| ------  | -------------------------- | --------------------------- | ------------------- | ---------- | -------------------- |
| ⬜      | Two Heaps                  | Running Median              | #295 Median Finder  | Hard       | Streaming analytics  |
| ⬜      | Sliding Window Median      | Window Statistics           | #480                | Hard       | Real-time dashboards |
| ⬜      | Greedy + Heap              | Task Scheduling             | #621 Task Scheduler | Medium     | Cluster scheduling   |
| ⬜      | IPO / Capital Maximization | Greedy + Heap               | #502                | Hard       | Resource allocation  |
| ⬜      | Meeting Rooms II           | Earliest Available Resource | #253                | Medium     | Executor scheduling  |

✅🟡 PHASE 7 — Trees
| Status  | Pattern                     | Recognition Clue      | LeetCode                     | Difficulty | Platform Equivalent        |
| ------  | --------------------------- | --------------------- | ---------------------------- | ---------- | -------------------------- |
| ✅      | DFS Traversal               | Visit every node      | #104 Maximum Depth           | Easy       | Folder traversal           |
| ✅      | DFS + Condition             | Validate property     | #100 Same Tree               | Easy       | Dataset comparison         |
| ✅      | Balanced Recursion          | Height difference     | #110 Balanced Binary Tree    | Easy       | Dependency tree validation |
| ✅      | Binary Search Tree          | Ordered tree          | #98 Validate BST             | Medium     | Metadata index validation  |
| ✅      | Lowest Common Ancestor      | Find shared parent    | #236 LCA                     | Medium     | Organizational hierarchy   |
| ✅      | Level Order Traversal (BFS) | Level by level        | #102 Binary Tree Level Order | Medium     | Workflow execution levels  |
| ✅      | Build Tree                  | Reconstruct hierarchy | #105 Construct Tree          | Medium     | Rebuild lineage graph      |

🟡 Platform Practice
| Status  | Exercise                      |
| ------  | ----------------------------- |
| ⬜      | Organization hierarchy        |
| ⬜      | Folder traversal              |
| ⬜      | Pipeline dependency tree      |
| ⬜      | Metadata hierarchy validation |

✅🟡 PHASE 8 — Graphs
| Status  | Pattern                                  | Recognition Clue                      | LeetCode                         | Difficulty | Platform Equivalent                    |
| ------  | ---------------------------------------- | ------------------------------------- | -------------------------------- | ---------- | -------------------------------------- |
| ✅      | Grid DFS / Connected Components          | Matrix + adjacent cells               | #200 Number of Islands           | Medium     | Connected services / cluster detection |
| ✅      | Graph DFS + HashMap                      | Clone objects with cycles             | #133 Clone Graph                 | Medium     | Infrastructure replication             |
| ✅      | DFS Cycle Detection / Topological Sort   | Dependencies + cycle detection        | #207 Course Schedule             | Medium     | Airflow DAG validation                 |
| 🟡      | Multi-source BFS                         | Spread from many starting points      | #994 Rotting Oranges             | Medium     | Incident or failure propagation        |
| 🟡      | BFS Shortest Path *(Discussion)*         | Minimum steps in unweighted graph     | #127 Word Ladder                 | Hard       | Service routing                        |
| 🟡      | Reverse DFS from Boundaries *(Optional)* | Reachability from multiple boundaries | #417 Pacific Atlantic Water Flow | Medium     | Data-flow reachability                 |

🟡 Platform Practice
| Status  | Exercise                  |
| ------  | ------------------------- |
| ⬜      | Airflow DAG validation    |
| ⬜      | Dependency resolution     |
| ⬜      | Microservice connectivity |
| ⬜      | Data lineage traversal    |

✅🟡 Phase 9 - Dynamic Programming
| Status  | Pattern                   | Recognition Clue                          | LeetCode                            | Difficulty | Platform Equivalent         |
| ------  | ------------------------- | ----------------------------------------- | ----------------------------------- | ---------- | --------------------------- |
| ⬜      | 1-D DP                    | Current answer depends on previous states | #70 Climbing Stairs                 | Easy       | Pipeline retry combinations |
| ⬜      | Decision DP               | Take or skip                              | #198 House Robber                   | Medium     | Resource allocation         |
| ⬜      | Kadane's Algorithm        | Best contiguous range                     | #53 Maximum Subarray                | Medium     | Peak performance interval   |
| ⬜      | Unbounded DP              | Reuse choices to build minimum/maximum    | #322 Coin Change                    | Medium     | Compute-cost optimization   |
| ⬜      | 2-D Grid DP               | Arrive from top or left                   | #62 Unique Paths                    | Medium     | Workflow path counting      |
| ⬜      | Sequence DP *(Optional)*  | Best increasing subsequence               | #300 Longest Increasing Subsequence | Medium     | Trend analysis              |
| ⬜      | Partition DP *(Optional)* | Split values into equal subsets           | #416 Partition Equal Subset Sum     | Medium     | Workload balancing          |

🟡 Platform Practice
| Status  | Exercise                     |
| ------  | ---------------------------- |
| ⬜      | Retry strategy optimization  |
| ⬜      | Resource allocation planning |
| ⬜      | Compute budget optimization  |
| ⬜      | Trend detection in metrics   |

Platform Coding (Most Important)
| Status | Exercise             | Skills           |
| ------ | -------------------- | ---------------- |
| ⬜      | Deduplicate Patients | Set              |
| ⬜      | Merge Claims         | Dict             |
| ⬜      | Provider Aggregation | defaultdict      |
| ⬜      | Data Reconciliation  | Set              |
| ⬜      | Pipeline Validation  | Validation       |
| ⬜      | Schema Validation    | Dict             |
| ⬜      | CSV Parser           | File Processing  |
| ⬜      | JSON Flattener       | Recursion        |
| ⬜      | Log Analyzer         | Counter          |
| ⬜      | CDC Merge            | Merge Logic      |
| ⬜      | Watermark Processing | Incremental Load |
| ⬜      | Batch Retry Logic    | State Management |

Debugging (Highest ROI)
| Status | Exercise             | Focus                  |
| ------ | -------------------- | ---------------------- |
| ⬜      | Missing `seen.add()` | Logic Bug              |
| ⬜      | KeyError             | Safe Dictionary Access |
| ⬜      | NoneType             | Defensive Coding       |
| ⬜      | Mutable Defaults     | Python Pitfall         |
| ⬜      | Infinite Loop        | Debugging              |
| ⬜      | Duplicate Records    | Root Cause Analysis    |
| ⬜      | Memory Leak          | Optimization           |
| ⬜      | Slow Algorithm       | Complexity             |
| ⬜      | Late Arriving Data   | Pipeline Logic         |
| ⬜      | Broken CDC           | Incremental Processing |

Mock Interviews
| Status | Session | Duration |
| ------ | ------- | -------- |
| ⬜      | Mock #1 | 60 min   |
| ⬜      | Mock #2 | 60 min   |
| ⬜      | Mock #3 | 60 min   |
| ⬜      | Mock #4 | 60 min   |
| ⬜      | Mock #5 | 60 min   |

Each mock will include:
Clarifying questions
Coding
Debugging
Complexity analysis
Edge cases
Production follow-ups

Coding Checklist (Use Every Time)
| Status  | Step                              |
| ------  | --------------------------------- |
| ⬜      | Clarify the problem               |
| ⬜      | Ask about edge cases              |
| ⬜      | Explain brute-force solution      |
| ⬜      | Analyze complexity                |
| ⬜      | Optimize approach                 |
| ⬜      | Write clean Python                |
| ⬜      | Dry-run with sample input         |
| ⬜      | Test edge cases                   |
| ⬜      | Discuss production considerations |
| ⬜      | Suggest optimizations             |

Progress Tracker
| Phase                 | Total Items | Completed |
| --------------------- | ----------: | --------: |
| Interview Framework   |           7 |       7/7 |
| Hash Maps & Sets      |           7 |       7/7 |
| Arrays & Two Pointers |           5 |       5/5 |
| Sliding Window        |           4 |       4/4 |
| Sorting & Intervals   |           4 |       4/4 |
| Stack & Queue         |           4 |       4/4 |
| Heap                  |           4 |       4/4 |
| Binary Search         |           3 |       4/3 |
| Trees                 |           3 |       3/3 |
| Platform Coding       |          12 |      0/12 |
| Debugging             |          10 |      0/10 |
| Mock Interviews       |           5 |       0/5 |
