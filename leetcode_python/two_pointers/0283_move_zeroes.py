"""
LeetCode: 283
Title: Move Zeroes
URL: https://leetcode.com/problems/move-zeroes/
Difficulty: Easy
Primary Pattern:
    Two Pointers
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Move Zeroes before coding.

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
    Time: O(n)
    Space: O(n)

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
Given an integer array nums, move all 0s to the end while maintaining 
the relative order of the non-zero elements.

Input: nums = [0,1,0,3,12]
Output: [1, 3, 12, 0, 0]
"""

nums = [0,1,0,3,12]
def move_zeroes(nums):
     write = 0

     for read in range(len(nums)):
          if nums[read] != 0:
               nums[write], nums[read]= nums[read], nums[write]
               write += 1
     return nums
print(move_zeroes(nums))
 

"""
We increment write because we just placed one valid non-zero value into its correct position. 
So the next non-zero value should go into the next slot.
We don't increment read manually because the for loop already moves read forward automatically.

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
