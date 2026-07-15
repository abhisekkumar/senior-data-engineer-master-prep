"""
LeetCode: 102
Title: Binary Tree Level Order Traversal
URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
Difficulty: Medium
Primary Pattern:
    Bfs
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Binary Tree Level Order Traversal before coding.

Recognition Clues:
    - The result is level-based or needs the shortest path in an unweighted graph.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Can the structure be empty, are cycles possible, and should output preserve level order?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Show the queue at the start of each level and the nodes added for the following level.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Explore paths independently or repeatedly scan for the next level without a queue.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(n)
    Space: O(n)

Optimal Approach:
    Apply the bfs pattern while maintaining its invariant.
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
    - Marking nodes visited too late or mixing nodes from different levels.
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
        15   7

Output:
[
  [3],
  [9,20],
  [15,7]
]
"""

from collections import deque

class Solution:
     def levelOrder(self, root):
          if not root:
               return []
          queue = deque([root])
          result = []

          while queue:
               level = []
               level_size = len(queue)

               for _ in range(level_size):
                    node = queue.popleft()
                    level.append(node.val)

                    if node.left:
                         queue.append(node.left)
                    if node.right:
                         queue.append(node.right)

               result.append(level)
          return result

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
