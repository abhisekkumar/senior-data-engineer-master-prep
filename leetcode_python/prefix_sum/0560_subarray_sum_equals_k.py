"""
LeetCode: 560
Title: Subarray Sum Equals K
URL: https://leetcode.com/problems/subarray-sum-equals-k/
Difficulty: Medium
Primary Pattern:
    Prefix Sum
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Subarray Sum Equals K before coding.

Recognition Clues:
    - The question asks about sums or balances over many contiguous ranges, including ranges with signed values.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Can values be negative, are empty ranges allowed, and is the task to count, find, or maximize ranges?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Update the running prefix value, look up the required prior state, and then record the current prefix.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Start at every index and accumulate each possible ending range.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(n²)
    Space: O(1)

Optimal Approach:
    Apply the prefix sum pattern while maintaining its invariant.
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
    - Forgetting the initial zero-prefix state or recording the current prefix too early.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
Memorize:
At every index, I ask: “Have I seen a previous prefix sum that I can subtract 
from my current running sum to get k?

Input: 
nums = [1, 1, 1], k = 2
Output: 2
[1,1] [1,1]


nums = [1, 2, 3], k = 3
Output: 2

"""

# Return the contiguous sum count 
nums = [-1, -5, -2, 1, 1, 1]
k = 3

def subarray_sum(nums, k):
     count = 0
     running_sum = 0
     seen = {0:1}

     for num in nums:
          running_sum += num
          needed = running_sum - k

          if needed in seen:
               count += seen[needed]
          
          seen[running_sum] = seen.get(running_sum, 0) + 1
     return count

print(subarray_sum(nums, k))


# Return the index of the contiguos sub count

def subarray_sumvalue(nums, k):
     seen = {0:1}
     running_sum = 0
     count = 0

     for num in nums:
          running_sum += num
          needed = running_sum - k

          if needed in seen:
               count += seen[needed]

          seen[running_sum] = seen.get(running_sum, 0) + 1
     return count




"""
Time & Space complexity for both algorithm is O(n)

This is why we use a HashMap
The HashMap remembers every balance (prefix sum) we've seen.
Instead of recalculating sums over and over, we ask:
Have I seen the balance I need before?
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
