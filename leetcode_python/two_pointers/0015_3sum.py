"""
LeetCode: 15
Title: 3Sum
URL: https://leetcode.com/problems/3sum/
Difficulty: Medium
Primary Pattern:
    Two Pointers
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for 3Sum before coding.

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
    Time: O(n³)
    Space: O(r)

Optimal Approach:
    Apply the two pointers pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n²)
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
    - Moving the wrong pointer without using the ordering or objective to justify it.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
Given an integer array nums, return all unique triplets:

Let's say: [a, b, c] then a+b+c=0

Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
"""
nums = [-1, 0, 1, 2, -1, -4]

def three_sum(nums):
     if len(nums) < 3:
          return []
     
     nums.sort()
     print(nums)
     result = []

     for i in range(len(nums)):
          if i > 0 and nums[i] == nums[i-1]:
               continue
          left = i + 1
          right = len(nums) - 1

          while left < right:
               total = nums[i] + nums[left] + nums[right]

               if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                         left += 1
                    while left < right and nums[right] == nums[right + 1]:
                         right -= 1
               elif total < 0:
                    left += 1
               else:
                    right -= 1
     return result

print(three_sum(nums))

"""
Time Complexity: O(n²)
Space Complexity: O(1)
"""
while left < rigth and nums[left] == nums[left - 1]:
     left 
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n²)
    Space: O(n)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
