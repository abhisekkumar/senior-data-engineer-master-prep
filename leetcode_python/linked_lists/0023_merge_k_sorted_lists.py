"""
LeetCode: 23
Title: Merge k Sorted Lists
URL: https://leetcode.com/problems/merge-k-sorted-lists/
Difficulty: Hard
Primary Pattern:
    Heap
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Merge k Sorted Lists before coding.

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
    Time: O(Nk)
    Space: O(1)

Optimal Approach:
    Apply the heap pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(N log k)
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
You're given multiple sorted linked lists and must merge them into one sorted linked list.

Input:
lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

Output: 
[1, 1, 2, 3, 4, 4, 5, 6]

* node.val lets the min heap prioritize the smallest current value.
* list_index acts as a tie-breaker when two nodes have the same value.
* node lets us attach that actual node and then push node.next.
"""
lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

import heapq
from typing import List, Optional


class Solution:
     def mergeKLists(
          self,
          lists: List[Optional[ListNode]]
     ) -> Optional[ListNode]:

          heap = []
          dummy = ListNode(0)
          current = dummy

          # Add the first node from every non-empty list.
          for list_index, node in enumerate(lists):
               if node:
                    heapq.heappush(
                         heap,
                         (node.val, list_index, node)
                    )

          while heap:
               value, list_index, node = heapq.heappop(heap)

               # Attach the smallest available node.
               current.next = node
               current = current.next

               # Add the next node from the same source list.
               if node.next:
                    heapq.heappush(
                         heap,
                         (node.next.val, list_index, node.next)
                    )

          return dummy.next
#print(mergeKLists(lists))

"""
Time Complexity: O(N log k)
Space Complexity: O(k)

N = total number of nodes across all lists
k = number of linked lists
"""

# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(N log k)
    Space: O(k)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
