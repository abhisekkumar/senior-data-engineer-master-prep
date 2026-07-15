"""
LeetCode: 56
Title: Merge Intervals
URL: https://leetcode.com/problems/merge-intervals/
Difficulty: Medium
Primary Pattern:
    Intervals
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Merge Intervals before coding.

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
    Time: O(n²)
    Space: O(n)

Optimal Approach:
    Apply the intervals pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n log n)
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
Input:
intervals = [[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]

First I'd sort intervals by start time. Then I'd maintain a merged result list. 
For each interval, I compare its start with the end of the last interval in result.
If current_start <= last_end, they overlap, so I merge by updating:
last_end = max(last_end, current_end)
Otherwise, there is a gap, so I append the current interval as a new interval.
"""
intervals = [[1,3],[8,10],[2,6],[15,18]]
def mergeIntervals(intervals):
     intervals.sort()
     result = []
     print(intervals)

     for start, end in intervals:
          if not result:
               result.append([start, end])
          elif start <= result[-1][1]:
               result[-1][1] = max(result[-1][1], end)
          else:
               result.append([start, end])
     return result


print(mergeIntervals(intervals))


"""
Time Complexity: O(n log n) because of sorting.
Space Complexity: O(n) for the result.
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n log n)
    Space: O(n)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
