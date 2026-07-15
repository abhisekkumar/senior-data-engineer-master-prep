"""
LeetCode: 57
Title: Insert Interval
URL: https://leetcode.com/problems/insert-interval/
Difficulty: Medium
Primary Pattern:
    Intervals
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Insert Interval before coding.

Recognition Clues:
    - The input contains ranges and the result depends on overlap, ordering, insertion, or merging.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Are intervals sorted, can endpoints touch, are they closed or half-open, and may the input be modified?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Compare the current interval with the last merged interval and show whether it is appended or combined.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Compare intervals repeatedly and merge or report every qualifying overlap.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(n log n)
    Space: O(n)

Optimal Approach:
    Apply the intervals pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n)
    Space: O(n)

Why This Approach:
    It removes the repeated work in the baseline and directly uses the recognition clues above.

Important Edge Cases:
    - Empty or minimum-size input, when permitted
    - Duplicate or repeated values, when relevant
    - Boundary values and no-solution behavior
    - Mutation and output-order requirements

Interviewer Follow-Ups:
    - Can auxiliary memory be reduced?
    - What changes if the input is sorted, streamed, or too large for one machine?
    - How would the trade-off change if output order matters?

Common Mistakes:
    - Using the wrong overlap condition or forgetting to sort when ordering is not guaranteed.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
You are given a list of non-overlapping intervals, sorted by start time.

Input:
intervals = [[1,3],[6,9]]
newInterval = [2,5]

Output: 
[[1,5],[6,9]]
"""

intervals = [[1,3],[6,9]]
newInterval = [2,5]
def insert(intervals, newInterval):

     result = []
     print(result)
     i = 0
     n = len(intervals)

     while i < n and intervals[i][1] < newInterval[0]:
          result.append(intervals[i])
          i += 1
     while i < n and intervals[i][0] <= newInterval[1]:
          newInterval[0] = min(newInterval[0], intervals[i][0])
          newInterval[1] = max(newInterval[1], intervals[i][1])
          i += 1
     result.append(newInterval)

     while i < n:
          result.append(intervals[i])
          i += 1
     return result

print(insert(intervals, newInterval))

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n)
    Space: O(n)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
