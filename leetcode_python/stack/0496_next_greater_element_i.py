"""
LeetCode: 496
Title: Next Greater Element I
URL: https://leetcode.com/problems/next-greater-element-i/
Difficulty: Easy
Primary Pattern:
    Monotonic Stack
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Next Greater Element I before coding.

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
    Time: O(nm)
    Space: O(1)

Optimal Approach:
    Apply the monotonic stack pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n+m)
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
For every number in nums1, find the first greater number to its right in nums2.

Input:
nums1 = [4,1,2]
nums2 = [1,3,4,2]

Output:
[-1, 3, -1]
"""

nums1 = [4,1,2]
nums2 = [1,3,4,2]

def nextGreaterElement(nums1, nums2):
     stack = []
     next_greater = {}
     result = []

     for current in nums2:
          while stack and current > stack[-1]:
               smaller = stack.pop()
               next_greater[smaller] = current          
          stack.append(current)

     while stack:
          next_greater[stack.pop()] = -1

     for num in nums1:
          result.append(next_greater[num])

     return result

print(nextGreaterElement(nums1, nums2))

"""
The stack stores unresolved values in decreasing order. 
When a larger value arrives, it becomes the first greater 
value for every smaller value popped from the stack.
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n+m)
    Space: O(n)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
