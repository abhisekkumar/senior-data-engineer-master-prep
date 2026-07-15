"""
LeetCode: 236
Title: Lowest Common Ancestor of a Binary Tree
URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Difficulty: Medium
Primary Pattern:
    Dfs
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Lowest Common Ancestor of a Binary Tree before coding.

Recognition Clues:
    - The answer depends on recursively combining information from children, neighbors, or complete paths.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Can the structure be empty, can it contain cycles, and what counts as a complete valid path?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Trace one recursive path to the base case, then show the value returned and combined at each caller.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Recompute the required subtree or path information independently for each candidate node.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(n)
    Space: O(h)

Optimal Approach:
    Apply the dfs pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n)
    Space: O(h)

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
    - Missing a base case, confusing node count with edge count, or failing to track visited graph nodes.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
Given:
         3
       /   \
      5     1
     / \   / \
    6   2 0   8
       / \
      7   4

Return: 3

"""

class Solution:
     def lowestCommonAncestor(self, root, p, q):
          if not root or root == p or root == q:
               return root
          
          left = self.lowestCommonAncestor(root.left, p, q)
          right = self.lowestCommonAncestor(root.right, p, q)

          if left and right:
               return root
          return left if left else right

"""
Time Complexity: O(n)
Space Complexity: O(h)
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n)
    Space: O(h)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
