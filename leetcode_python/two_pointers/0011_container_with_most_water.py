"""
LeetCode: 11
Title: Container With Most Water
URL: https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium
Primary Pattern:
    Two Pointers
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Container With Most Water before coding.

Recognition Clues:
    - The input is ordered or the answer depends on a pair/range whose boundaries can move monotonically.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Is the input sorted, must indices or values be returned, and may the input be modified?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Show both pointer positions, evaluate the current state, and justify which pointer moves next.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Evaluate every valid pair or range and retain the best or matching result.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(n²)
    Space: O(1)

Optimal Approach:
    Apply the two pointers pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n)
    Space: O(1)

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
    - Moving the wrong pointer without using the ordering or objective to justify it.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
height = [1,8,6,2,5,4,8,3,7]
Each number represents a vertical line.

Height

8 |   |         |
7 |   |         |   |
6 |   | |       |   |
5 |   | |   |   |   |
4 |   | |   | | |   |
3 |   | |   | | | | |
2 |   | | | | | | | |
1 | | | | | | | | | |
0 -------------------
    1 2 3 4 5 6 7 8 9

The water height is limited by the shorter wall, and the width is the distance between the two walls.
Area = width x min(left_height, right_height)
"""
height = [1,8,6,2,5,4,8,3,7]
def maxArea(height):
     left = 0
     right = len(height) - 1
     area = 0

     while left < right:
          area = max(area, (right-left) * min(height[left], height[right]))
          if height[left] < height[right]:
               left += 1
          else:
               right -= 1
     return area
print(maxArea(height))

"""
Time Complexity: O(n)
Space Complexity: O(1)

Why is this O(n) instead of O(n²)?

Each iteration moves exactly one pointer inward. 
The left pointer can move at most n times, and the right pointer can also move at most n times. 
Since neither pointer ever moves backward, the total number of pointer movements is bounded by 2n, 
which simplifies to O(n).
"""


# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n)
    Space: O(1)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
