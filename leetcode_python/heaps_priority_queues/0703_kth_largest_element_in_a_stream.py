"""
LeetCode: 703
Title: Kth Largest Element in a Stream
URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Difficulty: Easy
Primary Pattern:
    Heap
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Kth Largest Element in a Stream before coding.

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
    Time: O(n log n) per add
    Space: O(n)

Optimal Approach:
    Apply the heap pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(log k) per add
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
k = 3
nums = [4, 5, 8, 2]



Good clarifying questions:
* Can values be duplicated?
* Can values be negative?
* Can the initial nums array be empty?
* Is k guaranteed to be at least 1?
* Can k be greater than len(nums) initially?
* Is each add() call guaranteed to bring the total count to at least k before a return is required?
"""


import heapq

class KthLargest:
     def __init__(self, k, nums):
          self.k = k
          self.heap = []
          
          for num in nums:
               heapq.heappush(self.heap, num)

               if len(self.heap) > self.k:
                    heapq.heappop(self.heap)

     def add(self, val):
          heapq.heappush(self.heap, val)
          if len(self.heap) > self.k:
               heapq.heappop(self.heap)
          return(self.heap[0])

"""
* Each add() call: time O(log k), space remains O(k).
* Initialization with n starting values: time O(n log k), space O(k).

Why add() is O(log k):
heapq.heappush(self.heap, val)  # O(log k)
heapq.heappop(self.heap)        # O(log k), when needed

The heap never exceeds roughly k + 1 elements, so operations depend on k, not all values seen.

Interview answer:
Initialization takes O(n log k) time. Each subsequent add() takes O(log k) time, 
and the class uses O(k) auxiliary space because it stores only the largest k values.
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(log k) per add
    Space: O(k)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
