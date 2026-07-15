"""
LeetCode: 105
Title: Construct Binary Tree from Preorder and Inorder Traversal
URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Difficulty: Medium
Primary Pattern:
    Recursion
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Construct Binary Tree from Preorder and Inorder Traversal before coding.

Recognition Clues:
    - The constraints and requested output naturally suggest the recursion pattern.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. What input guarantees, boundary cases, mutation rules, and output-order requirements apply?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Trace the main state variables through the smallest non-trivial example in the preserved notes.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Use direct enumeration or repeated scans to establish a simple correctness baseline.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(n²)
    Space: O(n)

Optimal Approach:
    Apply the recursion pattern while maintaining its invariant.
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
    - Skipping contract checks or stating complexity without defining the input variables.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
Given:
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Output:
        3
       / \
      9   20
         /  \
        15   7
"""

class Solution:
     def buildTree(self, preorder, inorder):
          if not preorder or not inorder:
               return None

          inorder_map = {
               value:index
               for index, value in enumerate(inorder)
          }
          preorder_index = 0

          def build(left, right):
               nonlocal preorder_index

               if left > right:
                    return None

               root_value = preorder[preorder_index]
               preorder_index += 1

               root = TreeNode(root_value)
               index = inorder_map[root_value]

               root.left = build(left, index-1)
               root.right = build(index+1, right)

               return root
          return build(0, len(inorder) - 1)


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
