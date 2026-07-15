"""
LeetCode: 155
Title: Min Stack
URL: https://leetcode.com/problems/min-stack/
Difficulty: Medium
Primary Pattern:
    Stack
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Min Stack before coding.

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
    Time: O(n) per min
    Space: O(n)

Optimal Approach:
    Apply the stack pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(1) per operation
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
1. Can I assume the operations are always valid?
    * For example, will pop(), top(), or getMin() ever be called on an empty stack?
2. Do all four operations need to be O(1)?
3. Can there be duplicate values?


We need two stacks because the main stack must preserve normal LIFO behavior, 
while the second stack tracks the minimum after every push. That lets getMin() 
return the top of min_stack in O(1), and when we pop, we pop from both stacks 
so their states stay synchronized.
"""

class MinStack:

     def __init__(self):
        self.stack = []
        self.min_stack = []
     
     def push(self, value):
          self.stack.append(value)

          if not self.min_stack:
               self.min_stack.append(value)
          else:
               self.min_stack.append(min(val, self.min_stack[-1]))
     
     def pop(self):
          self.stack.pop()
          self.min_stack.pop()
     
     def top(self):
          return self.stack[-1]

     def getMin(self):
          return self.min_stack[-1]


"""
Time Complexity: O(1)
Space Complexity: O(n)

We duplicate the current minimum so both stacks stay aligned:

stack:     [5, 2, 8]
min_stack: [5, 2, 2]

Each index in min_stack represents the minimum for the corresponding state of stack.

When we pop 8:

stack:     [5, 2]
min_stack: [5, 2]

The new minimum is immediately available at:

self.min_stack[-1]

Without duplication, the two stacks could fall out of sync and we would need extra logic to determine when an old minimum becomes active again.

“I store the current minimum for every stack state. This keeps both stacks synchronized, so popping from both automatically restores the previous minimum in O(1).”
"""


# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(1) per operation
    Space: O(n)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
