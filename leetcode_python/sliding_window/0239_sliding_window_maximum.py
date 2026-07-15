"""
LeetCode: 239
Title: Sliding Window Maximum
URL: https://leetcode.com/problems/sliding-window-maximum/
Difficulty: Hard
Primary Pattern:
    Monotonic Deque
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Sliding Window Maximum before coding.

Recognition Clues:
    - The constraints and requested output naturally suggest the monotonic deque pattern.
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
    Time: O(nk)
    Space: O(k)

Optimal Approach:
    Apply the monotonic deque pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n)
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
    - Skipping contract checks or stating complexity without defining the input variables.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
"""

nums = [1,3,-1,-3,5,3,6,7]
k = 3

from collections import deque
def maxSlidingWindow(nums, k):
     q = deque()
     result = []

     for right in range(len(nums)):
          while q and q[0] < right - k + 1:
               q.popleft()
          while q and nums[q[-1]] < nums[right]:
               q.pop()
          q.append(right)
          
          if right >= k - 1:
               result.append(nums[q[0]])

     return result

print(maxSlidingWindow(nums, k))

"""
Time Complexity: O(n)
Space Complexity: O(k)

The deque maintains indices whose values are in decreasing order, 
so the front always points to the maximum value of the current window.

Each index is inserted into the deque at most once and removed at most once. 
Although there are nested while loops, the total number of deque operations 
across the entire algorithm is linear.



Explain your algorithm.

Block 1: while q and q[0] < right -k + 1:
Remove indices that have gone out of the current window.

Block 2: while q and nums[q[-1]] < nums[right]:
Remove smaller elements from the back because they can never become the maximum after a 
larger element arrives.

Block 3: q.append(right)
Add the current index as a new candidate.

Block 4: if right >= k -1:
Once a complete window exists, the front of the deque represents 
the maximum value, so append it to the result.
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n)
    Space: O(k)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
