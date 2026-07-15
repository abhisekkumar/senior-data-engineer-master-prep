"""
LeetCode: 167
Title: Two Sum II - Input Array Is Sorted
URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Difficulty: Medium
Primary Pattern:
    Two Pointers
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Two Sum II - Input Array Is Sorted before coding.

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
Given a sorted array of integers numbers, return the 1-indexed positions of two numbers that add up to target.

Input:
numbers = [2, 7, 11, 15]
target = 9

Output:
[1, 2]
"""
numbers = [2, 7, 11, 15]
target = 9
def two_sum_sorted(numbers, target):
     left = 0
     right = len(numbers) - 1

     while left < right:
          total = numbers[left] + numbers[right]

          if total == target:
               return [left+1, right+1]
          elif total < target:
               left += 1
          else:
               right -= 1

print(two_sum_sorted(numbers, target))


"""
Time Complexity: O(n)
Space Complexity: O(1)
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
