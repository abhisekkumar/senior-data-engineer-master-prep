"""
LeetCode: 523
Title: Continuous Subarray Sum
URL: https://leetcode.com/problems/continuous-subarray-sum/
Difficulty: Medium
Primary Pattern:
    Prefix Sum
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Continuous Subarray Sum before coding.

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
LeetCode #523 — Continuous Subarray Sum

Input:
nums = [23, 2, 4, 6, 7]
k = 6

Output: 
True 
Why?
2 + 4 = 6
6 % 6 = 0

or 

23 + 2 + 4 + 6 + 7 = 42
42 % 6 = 0
"""

nums = [23,2,6,4,7]
k = 6


def checkSubarraySum(nums, k):
     count = 0
     running_sum = 0
     seen = {0: -1}

     for i, num in enumerate(nums):
          running_sum += num
          remainder = running_sum % k

          if remainder in seen:
               if i - seen[remainder] >= 2:
                    return True
          else:
               seen[remainder] = i #only runs when remainder not in seen, also because only want to store the first occurence not overwrite
     return False

print(checkSubarraySum(nums, k))


"""
Store the first index where each remainder appeared. 
If I see the same remainder again and the distance is at least 2, 
the subarray between those indices has a sum divisible by k.

Time: O(n)
Space: O(min(n, k)) usually, or O(n) generally.

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
