"""
LeetCode: 207
Title: Course Schedule
URL: https://leetcode.com/problems/course-schedule/
Difficulty: Medium
Primary Pattern:
    Topological Sort
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Course Schedule before coding.

Recognition Clues:
    - The constraints and requested output naturally suggest the topological sort pattern.
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
    Time: O(VE)
    Space: O(V)

Optimal Approach:
    Apply the topological sort pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(V+E)
    Space: O(V+E)

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
Input:
numCourses = 4
prerequisites =
[
 [1,0],
 [2,1],
 [3,2]
]

Output:
True

✅ Can prerequisites be empty?
✅ Can there be duplicate prerequisite pairs?
✅ Can there be cycles in the input? 
✅ Is every course ID guaranteed to be between 0 and numCourses - 1?

A node is added to visited only after all its prerequisites have been safely processed.
"""

from collections import defaultdict
# graph = {
#     0: [],
#     1: [0],
#     2: [1],
#     3: [2]
# }

numCourses = 3
prerequisites = [[0,1], [1,2], [2,0]]


class Solution:
     def canFinish(self, numCourses, prerequisites):
          #graph = defaultdict(list)
          graph = {course: [] for course in range(numCourses)}

          for course, prereq in prerequisites:
               graph[course].append(prereq)

          visited = set()
          path = set()
          
          def dfs(course):
               if course in path:
                    return False
               if course in visited:
                    return True
               
               path.add(course)

               for prereq in graph[course]:
                    if not dfs(prereq):
                         return False
               path.remove(course)
               visited.add(course)

               return True
          
          for course in range(numCourses):
               if not dfs(course):
                    return False
          
          return True


numCourses = 3
prerequisites = [[0,1], [1,2], [2,0]]

def canFinish(numCourses, prerequisites):
     graph = {course: [] for course in range(numCourses)}
     #graph = defaultdict(list)
     print(graph)

     for course, prereq in prerequisites:
          graph[course].append(prereq)
     
     visited = set()
     path = set()

     def dfs(course):
          if course in path:
               return False
          if course in visited:
               return True
          path.add(course)

          for prereq in graph[course]:
               if not dfs(prereq):
                    return False
          path.remove(course)
          visited.add(course)

          return True

     for course in range(numCourses):
          if not dfs(course):
               return False
     return True








# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(V+E)
    Space: O(V+E)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
