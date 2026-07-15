"""
LeetCode: 162
Title: Find Peak Element
URL: https://leetcode.com/problems/find-peak-element/
Difficulty: Medium
Primary Pattern:
    Binary Search
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Find Peak Element before coding.

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
Input:
nums = [1,2,3,1]

Output: 2
where nums[2] = 3
"""

nums = [1,2,3,1]
def findPeakElement(nums):
     left = 0
     right = len(nums) - 1
     
     while left < right:
          mid = (left + right) // 2
          print(mid)

          if nums[mid] < nums[mid + 1]:
               left = mid + 1
          else:
               right = mid
     return right

print(findPeakElement(nums))


"""
Time Complexity: O(log n)
Space Complexity: O(1)

We compare nums[mid] with nums[mid + 1] to understand the slope. 
If nums[mid] < nums[mid + 1], we are moving uphill, so a peak must exist on the right side. 
Therefore, we can discard the left side including mid.
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
