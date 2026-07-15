"""
LeetCode: 739
Title: Daily Temperatures
URL: https://leetcode.com/problems/daily-temperatures/
Difficulty: Medium
Primary Pattern:
    Monotonic Stack
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Daily Temperatures before coding.

Recognition Clues:
    - The most recent unresolved item must be processed first, or nested structure must be matched.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Which tokens or values are valid, are operations guaranteed valid, and what should malformed input return?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Show the stack before and after each push or pop and explain what invariant the stack maintains.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Repeatedly scan for the next resolvable pair or relationship until no work remains.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(n²)
    Space: O(1)

Optimal Approach:
    Apply the monotonic stack pattern while maintaining its invariant.
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
    - Popping an empty stack or reversing operand order for a non-commutative operation.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait 
after the ith day to get a warmer temperature. If there is no future day for which 
this is possible, keep answer[i] == 0 instead.

Input:
temps = [73,74,75,71,69,72,76,73]

Output: [1,1,4,2,1,1,0,0]

I iterate by index instead of value because I need the index to calculate the number 
of days between the current warmer temperature and the previous unresolved temperatur
"""
temperatures = [73,74,75,71,69,72,76,73]

def dailyTemperatures(temperatures):
     stack = []
     result = [0] * len(temperatures)

     for current_day in range(len(temperatures)):
          while stack and temperatures[current_day] > temperatures[stack[-1]]:
               previous_day = stack.pop()
               result[previous_day] = current_day - previous_day
          stack.append(current_day)
     return result

print(dailyTemperatures(temperatures))

"""
Time Complexity: O(n)
Space Complexity: O(n)
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
