"""
LeetCode: 3
Title: Longest Substring Without Repeating Characters
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium
Primary Pattern:
    Sliding Window
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Longest Substring Without Repeating Characters before coding.

Recognition Clues:
    - The result concerns a contiguous substring or subarray whose validity can be maintained as boundaries move.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Is the window fixed or variable, are values positive, and what makes a window valid or invalid?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Move the right boundary, update window state, shrink from the left when required, and record the best valid window.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Enumerate every contiguous range and recompute the required property for each range.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(n²)
    Space: O(k)

Optimal Approach:
    Apply the sliding window pattern while maintaining its invariant.
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
    - Moving a boundary without updating counts or removing the outgoing value.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
Given a string s, find the length of the longest substring without repeating characters.

Input:
s = "abcabcbb"
Output: 
3 why? cuz: abc
"""

s = "abcabcbb"
def length_of_longest_substring(s):

     seen = set()
     left = 0
     max_len = 0

     for right in range(len(s)):
          char = s[right]

          while char in seen:
               seen.remove(s[left])
               left += 1
          seen.add(char)
          max_len = max(max_len, right - left + 1)
     return max_len

print(length_of_longest_substring(s))

"""
Time Complexity: O(n)
Space Complexity: O(1)
I use a sliding window where the right pointer expands the window 
and the left pointer shrinks it whenever a duplicate appears. 
The set tracks characters currently inside the window, not all characters ever seen.
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
