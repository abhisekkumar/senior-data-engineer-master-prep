"""
LeetCode: 133
Title: Clone Graph
URL: https://leetcode.com/problems/clone-graph/
Difficulty: Medium
Primary Pattern:
    Graph Traversal
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Clone Graph before coding.

Recognition Clues:
    - The input represents connectivity, dependencies, components, or reachability.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Is the graph directed, can it contain cycles, is it connected, and how are nodes represented?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Trace the frontier and visited set, showing when each neighbor is discovered.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Start a fresh traversal for each query without reusing visited or computed state.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(V+E)
    Space: O(V)

Optimal Approach:
    Apply the graph traversal pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(V+E)
    Space: O(V)

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
    - Failing to mark visited nodes or assuming a disconnected graph has one component.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
⭐ Interview trick

Why don't you use a visited set?

A visited set only tells me whether I've seen a node. 
It doesn't give me the cloned node that I need to connect neighbors. 
I need a dictionary mapping each original node to its clone.

"""
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        old_to_new = {}

        def dfs(current):
            if current in old_to_new:
                return old_to_new[current]

            copy = Node(current.val)
            old_to_new[current] = copy

            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)


# Build graph from:
# adjList = [[2,4], [1,3], [2,4], [1,3]]

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

sol = Solution()
cloned_graph = sol.cloneGraph(node1)

print(cloned_graph.val)
print([neighbor.val for neighbor in cloned_graph.neighbors])

"""
Time Complexity: O(V+E)
Space Complexity: O(V)
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(V+E)
    Space: O(V)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
