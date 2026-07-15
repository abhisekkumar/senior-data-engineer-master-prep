"""
LeetCode: 986
Title: Interval List Intersections
URL: https://leetcode.com/problems/interval-list-intersections/
Difficulty: Medium
Primary Pattern:
    Intervals
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Interval List Intersections before coding.

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
    Time: O(nm)
    Space: O(r)

Optimal Approach:
    Apply the intervals pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n + m)
    Space: O(r)

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
You are given two sorted interval lists.
Return every overlapping interval lists.

Input: 
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

Output: 
[
 [1,2],
 [5,5],
 [8,10],
 [15,23],
 [24,24],
 [25,25]
]
"""
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
def interval_intersection(firstList, secondList):
    result = []
    i = 0
    j = 0

    while i < len(firstList) and j < len(secondList):
        start = max(firstList[i][0], secondList[j][0])
        end = min(firstList[i][1], secondList[j][1])

        if start <= end:
            result.append([start, end])

        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return result

print(interval_intersection(firstList, secondList))



"""
Time Complexity: O(m + n)
Space Complexity: O(1)
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n + m)
    Space: O(r)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
