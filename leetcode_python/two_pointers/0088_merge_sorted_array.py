"""
LeetCode: 88
Title: Merge Sorted Array
URL: https://leetcode.com/problems/merge-sorted-array/
Difficulty: Easy
Primary Pattern:
    Two Pointers
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Merge Sorted Array before coding.

Recognition Clues:
    - The input is ordered or the answer depends on a pair/range whose boundaries can move monotonically.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Is the input sorted, must indices or values be returned, and may the input be modified?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Show both pointer positions, evaluate the current state, and justify which pointer moves next.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Evaluate every valid pair or range and retain the best or matching result.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(m + n)
    Space: O(m + n)

Optimal Approach:
    Apply the two pointers pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(m + n)
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
    - Moving the wrong pointer without using the ordering or objective to justify it.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
Pattern:Reverse Two Pointers
Give two sorted arrays:

Input: 
nums1 = [1,2,3,0,0,0]    nums2 = [2,5,6]
m = 3                    n = 3

Output:
Your goal is to modify nums1 so that it becomes
[1,2,2,3,5,6]

The last three zeroes in nums1 are not values.
They are just empty spaces.
"""

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

def merge(nums1, m, nums2, n):
     p1 = m-1
     p2 = n-1
     write = m+n-1

     while p2 >= 0:
          if p1 >= 0 and nums1[p1] > nums2[p2]:
               nums1[write] = nums1[p1]
               p1 -=1
          else:
               nums1[write] = nums2[p2]
               p2 -=1
          write -=1
     return nums1

print(merge(nums1, m, nums2, n))

"""
Time Complexity: O(m + n)
Space Complexity: O(1)

Key interview sentence:
I merge from the back because nums1 has empty space at the end. 
This avoids shifting elements and lets me fill the array in-place.

"""

"""
⭐ Interview Follow-up

Imagine the interviewer says:
“Okay, your algorithm assumes nums1 has extra space.”

You can respond:
If nums1 didn't have the reserved space, I'd have two options. If additional memory were allowed, 
I'd allocate a new result array and merge in O(m+n) time. If the merge had to be done in-place with 
no extra memory, I'd need to shift elements when inserting, which degrades to O(mxn) in the worst case. 
In production systems with very large datasets, I'd use a merge operation such as a 
SQL MERGE or Delta Lake MERGE INTO rather than manipulating arrays in memory.”
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(m + n)
    Space: O(1)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
