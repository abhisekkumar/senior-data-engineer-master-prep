"""
LeetCode: 104
Title: Maximum Depth of Binary Tree
URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy
Primary Pattern:
    Dfs
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Maximum Depth of Binary Tree before coding.

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
Input:
      3
     / \
    9   20
       /  \
      15    7

Output:3

Strong clarifying questions
* Can the tree be empty (root = None)?
* Is it guaranteed to be a binary tree?
* Can node values be duplicated?
* Can node values be negative?
"""
# Recursive Approach
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right
def max_depth(root):
     if not root:
          return 0
     left_depth = max_depth(root.left)
     right_depth = max_depth(root.right)

     return 1 + max(left_depth, right_depth)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(max_depth(root))

"""
Time Complexity: O(n)
Space Complexity: O(h)
"""

# Iterative Approach

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right
def max_depth(root):
     if not root:
          return 0
     
     stack = [(root, 1)]
     max_depth = 0

     while stack:
          node, depth = stack.pop()
          max_depth = max(max_depth, depth)

          if node.left:
               stack.append((node.left, depth + 1))
          if node.right:
               stack.append((node.right, depth + 1))
     return max_depth

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(max_depth(root))
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
