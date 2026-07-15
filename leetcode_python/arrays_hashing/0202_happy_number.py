"""
LeetCode: 202
Title: Happy Number
URL: https://leetcode.com/problems/happy-number/
Difficulty: Easy
Primary Pattern:
    Set
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Happy Number before coding.

Recognition Clues:
    - The task requires fast membership, uniqueness, duplicate detection, or set difference.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Are duplicates meaningful, does output order matter, and may values be negative or empty?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Show the set before each lookup and after a previously unseen value is added.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Use nested scans to compare each value with the remaining input.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(log n) per iteration
    Space: O(log n)

Optimal Approach:
    Apply the set pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(log n) per iteration
    Space: O(log n)

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
    - Adding at the wrong time or using a set when occurrence counts are required.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
I'll keep a set of numbers I've already seen. While n is not 1, 
I calculate the next number by summing the squares of its digits. 
If that next number has already appeared, we're in a cycle, so return False. 
If we eventually reach 1, return True.
"""
n = 19
def is_happy(n):
     seen = set()

     while n != 1:
          if n in seen:
               return False
          seen.add(n)

          total = 0
          for digit in str(n):
               total += int(digit) ** 2
          n = total
     return True

print(is_happy(n))

# Time Complexity: O(log n)

# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(log n) per iteration
    Space: O(log n)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
