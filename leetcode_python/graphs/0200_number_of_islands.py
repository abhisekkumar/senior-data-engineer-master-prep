"""
LeetCode: 200
Title: Number of Islands
URL: https://leetcode.com/problems/number-of-islands/
Difficulty: Medium
Primary Pattern:
    Grid Traversal
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Number of Islands before coding.

Recognition Clues:
    - The constraints and requested output naturally suggest the grid traversal pattern.
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
    Time: O(mn)
    Space: O(mn)

Optimal Approach:
    Apply the grid traversal pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(mn)
    Space: O(mn)

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
grid = [
    ["1","1","0","0"],
    ["1","0","0","1"],
    ["0","0","1","1"],
    ["1","0","0","0"]
] 
# 1 is land, 0 is water

class Solution:
     def numIslands(self, grid):
          rows = len(grid)
          cols = len(grid[0])

          visited = set()
          islands = 0

          def dfs(r, c):
               if (
                    r < 0 or 
                    r >= rows or 
                    c < 0 or
                    c >= cols or
                    grid[r][c] == "0" or
                    (r,c) in visited
               ):

                    return 
               visited.add((r,c))

               dfs(r+1, c)
               dfs(r-1, c)
               dfs(r, c+1)
               dfs(r, c-1)

          for r in range(rows):
               for c in range(cols):
                    if grid[r][c] == "1" and (r,c) not in visited:
                         islands += 1
                         dfs(r,c)
          return islands

sol = Solution()
print(sol.numIslands(grid))


"""
Time Complexity: O(m x n)
Space Complexity: O(m x n)
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(mn)
    Space: O(mn)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
