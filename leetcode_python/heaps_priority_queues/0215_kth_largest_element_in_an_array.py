"""
LeetCode: 215
Title: Kth Largest Element in an Array
URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
Difficulty: Medium
Primary Pattern:
    Heap
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Kth Largest Element in an Array before coding.

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

Input:
nums = [3, 2, 1, 5, 6, 4]
k = 2

Output:
5

⭐ Interview Review
Clarifying Questions ✅

I'd ask:

* Can k be larger than len(nums)?
* Can there be duplicate numbers?
* Can numbers be negative?
* Can the array be empty?
"""

nums = [3, 2, 1, 5, 6, 4]
k=2

import heapq

def findKthLargest(nums, k):
     heap = []

     for num in nums:
          heapq.heappush(heap, num)
          if len(heap) > k:
               heapq.heappop(heap)
     return heap[0]

print(findKthLargest(nums, k))


"""
Time Complexity: O(log k)
Space Complexity: O(k)

Why heap of k size?
Because the problem only asks for the kth largest element, not a fully sorted list. 
Therefore, I only need to keep the largest k elements seen so far. Any element that isn't 
in the top k can be discarded immediately, which is why the heap size never exceeds k.

Instead of always pushing and then popping, I can skip values that are smaller 
than the current kth largest and use heapreplace() only when the new value belongs in the top k.

for num in nums:
     if len(heap) < k:
          heapq.heappush(heap, num)
     elif num > heap[0]:
          heapq.heapreplace(heap, num)
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
