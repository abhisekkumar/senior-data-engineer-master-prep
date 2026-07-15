"""
LeetCode: 973
Title: K Closest Points to Origin
URL: https://leetcode.com/problems/k-closest-points-to-origin/
Difficulty: Medium
Primary Pattern:
    Heap
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for K Closest Points to Origin before coding.

Recognition Clues:
    - Only the largest, smallest, or top `k` items are needed while data is processed incrementally.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Is `k` valid, does output order matter, how are ties handled, and can data arrive as a stream?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Show each heap insertion or replacement and explain why the heap never needs to exceed its intended size.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Collect and sort all candidates, then select the required ranked items.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(n log n)
    Space: O(n)

Optimal Approach:
    Apply the heap pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n log k)
    Space: O(k)

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
    - Using the wrong heap direction or returning heap tuples instead of the required values.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2

Strong clarifying questions
* Can k be greater than the number of points?
* Can there be duplicate points?
* Can coordinates be negative?
* Can points be empty?
* Does the output order matter, or can I return the points in any order?

"""
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
import heapq

def kClosest(points, k):
     heap = []
     result = []

     for point in points:
          x = point[0]
          y = point[1]

     #      heapq.heappush(heap, point)

     # for x, y in points:
          distance = x*x + y*y
          heapq.heappush(heap, (-distance, [x,y]))

          if len(heap) > k:
               heapq.heappop(heap)
     for distance, point in heap:
          result.append(point)
     return result

print(kClosest(points, k))


"""
Time Complexity: O(log k)
Space Complexity: O(k)
"""
          

# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n log k)
    Space: O(k)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
