"""
LeetCode: 19
Title: Remove Nth Node From End of List
URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Difficulty: Medium
Primary Pattern:
    Fast Slow Pointers
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Remove Nth Node From End of List before coding.

Recognition Clues:
    - The constraints and requested output naturally suggest the fast slow pointers pattern.
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
    Time: O(n) two pass
    Space: O(1)

Optimal Approach:
    Apply the fast slow pointers pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n) one pass
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
Input:
1 → 2 → 3 → 4 → 5
n = 2

Output: 
1 → 2 → 3 → 5

The strongest clarifying questions are:
* Can the list be empty?
* Is n guaranteed to be valid, meaning 1 <= n <= length of list?
* Can the list contain only one node?
* Can values be duplicated?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
          dummy = ListNode(0)
          dummy.next = head

          slow = dummy
          fast = dummy

          for _ in range(n+1):
               fast = fast.next

          while fast:
               slow = slow.next
               fast = fast.next
          
          slow.next = slow.next.next
          
          return dummy.next

"""
We move fast n + 1 steps ahead so that when fast reaches the end of the list, 
slow is positioned exactly one node before the node we want to delete. 
We need slow to be on the previous node because deletion in a singly linked 
list is done by updating the previous node's next pointer: slow.next = slow.next.next. 
If slow were on the target node itself, we wouldn't have a reference to the previous 
node needed to bypass it.
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n) one pass
    Space: O(1)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
