"""
LeetCode: 206
Title: Reverse Linked List
URL: https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy
Primary Pattern:
    Linked List
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Reverse Linked List before coding.

Recognition Clues:
    - The constraints and requested output naturally suggest the linked list pattern.
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
    Time: O(n)
    Space: O(n)

Optimal Approach:
    Apply the linked list pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n)
    Space: O(1)

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
Reverse linkedlist

Input: 1 → 2 → 3 → 4 → 5
Output: 5 → 4 → 3 → 2 → 1

Clarifying Questions:
* Can the linked list be empty (head = None)?
* Can it contain only one node?
* Can node values be duplicated?
* Can values be negative?

⭐ The Interview Trick

Why do we need next_node?
Because once I reverse current.next, I lose access to the remainder of the list. 
I first save current.next into next_node, then reverse the pointer, then 
continue traversal using the saved pointer.
"""

# Definition for singly-linked list.
1 → 2 → 3 → 4 → 5
class ListNode:
     def __init__(self, val=0, next=None):
          self.val = val
          self.next = next

class Solution:
     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
          prev = None
          current = head

          while current:
               next_node = current.next
               current.next = prev
               prev = current
               current = next_node
          return prev

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""


# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n)
    Space: O(1)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
