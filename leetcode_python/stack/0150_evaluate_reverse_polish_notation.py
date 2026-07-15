"""
LeetCode: 150
Title: Evaluate Reverse Polish Notation
URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Difficulty: Medium
Primary Pattern:
    Stack
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Evaluate Reverse Polish Notation before coding.

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
    Time: O(n)
    Space: O(n)

Optimal Approach:
    Apply the stack pattern while maintaining its invariant.
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
You are given an array of strings tokens that represents an arithmetic expression in 
a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Clarifying Questions:
* Can tokens contain negative integers such as "-11"?
* Can the token list be empty?
* Which operators are allowed: +, -, *, /?
* Is the expression guaranteed to be valid?
* For division, should the result truncate toward zero? In this problem, yes.
"""

tokens = ["2","1","+","3","*"]

def evalRPN(tokens):
     stack = []

     for token in tokens:
          if token in {"+", "-", "*", "/"}: 
               right = stack.pop()
               left = stack.pop()
               if token == "+":
                    stack.append(left+right)
               elif token == "-":
                    stack.append(left-right)
               elif token == "*":
                    stack.append(left*right)
               else:
                    stack.append(int(left/right))
          else:
               stack.append(int(token))
     return stack[-1]

print(evalRPN(tokens))

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
