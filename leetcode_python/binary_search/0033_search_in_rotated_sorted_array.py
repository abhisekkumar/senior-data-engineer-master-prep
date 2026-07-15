"""
LeetCode: 33
Title: Search in Rotated Sorted Array
URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty: Medium
Primary Pattern:
    Binary Search
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Search in Rotated Sorted Array before coding.

Recognition Clues:
    - The search space is ordered, or a monotonic condition lets us discard half of the candidates.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Is the input sorted or rotated, can duplicates occur, and what should be returned when no match exists?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Track `left`, `right`, and `mid`; state which half or answer range is discarded after each comparison.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Scan candidates from left to right, or try every feasible answer until the condition is satisfied.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(n)
    Space: O(1)

Optimal Approach:
    Apply the binary search pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(log n)
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
    - Using inconsistent interval boundaries or failing to prove that the search range shrinks.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
Recognition Clue

“The array is sorted…
…but something happened.”
[4,5,6,7,0,1,2]
or
[30,40,50,5,10,20]

It is two sorted halves.

Examples:

Input: 
nums = [4,5,6,7,0,1,2]
target = 0

Output: 4
"""

nums = [4,5,6,7,0,1,2]
target = 0

def search_rotate(nums, target):
     left = 0
     right = len(nums) - 1

     while left <= right:
          mid = (left + right) // 2
          if nums[mid] == target:
               return mid
          
          # Left half is sorted
          if nums[left] <= nums[mid]:
               if nums[left] <= target < nums[mid]:
                    right = mid - 1
               else:
                    left = mid + 1
          # Right half is sorted
          else:
               if nums[mid] < target <= nums[right]:
                    left = mid + 1
               else:
                    right = mid - 1
     return -1 

print(search_rotate(nums, target))

"""
Time Complexity: O(log n)
Space Complexity: O(1)

Mental rule:
Find which half is sorted. If target belongs there, search that half. Otherwise search the other half.

⭐ Interview Follow-up (Very Important)

An interviewer may ask:
“Why is this still O(log n) even though the array is rotated?”

A strong answer is:
“Although the array is rotated, at every iteration I can determine which half is sorted. 
Once I know the sorted half, I can determine whether the target lies within it. 
This lets me discard half of the search space each iteration, so the overall time complexity remains O(log n).”
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(log n)
    Space: O(1)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
