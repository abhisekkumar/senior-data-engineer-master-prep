"""
LeetCode: 1
Title: Two Sum
URL: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Primary Pattern:
    Hash Map
Secondary Patterns:
    - Complement Lookup
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Two Sum before coding.

Recognition Clues:
    - The solution needs fast lookup from a value or signature to an index, count, or group.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Are duplicates allowed, what exactly should be returned, and can multiple answers exist?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Show the key being looked up and the map state after the current item is processed.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Use nested scans to compare every relevant pair or group candidate.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(n²)
    Space: O(1)

Optimal Approach:
    Apply the hash map pattern while maintaining its invariant.
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
    - Overwriting information needed for duplicates or storing the current value before checking its complement.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
def two_sums(nums, target):
     seen = {}
     print(seen)
     for i, num in enumerate(nums):
          complement = target - num
          if complement in seen:
               return [seen[complement], i]
          seen[num] = i
print(two_sums([2, 7, 11, 15], 9))



# Time Complexity: O(n)
# Space Complexity: O(1)

"""
Suppose the input has 100 million numbers. The dictionary no longer fits into memory. What would you do?

If the input is too large to fit in memory, I wouldn't keep the full hash map locally. 
I'd move to a distributed or external-memory approach.
One option is to partition the data by value range or hash so each worker handles 
a subset that fits in memory. Another option is to sort the data externally and 
then use a two-pointer approach across sorted chunks.
In a data platform environment, I'd likely use Spark or a database join depending 
on where the data lives. The key idea is to avoid holding all 100 million values in one process.
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
