"""
LeetCode: 340
Title: Longest Substring with At Most K Distinct Characters
URL: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
Difficulty: Medium
Primary Pattern:
    Sliding Window
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Longest Substring with At Most K Distinct Characters before coding.

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
Given a string s and an integer k, return the length of the longest substring that 
contains at most k distinct characters.

Input: 
s = "eceba"
k = 2

Output: 
3
"""

s = "eceba"
k = 2

def lengthOfLongestSubstringKDistinct(s, k):
    left = 0
    window = {}
    max_len = 0

    for right in range(len(s)):
        char = s[right]

        if char in window:
            window[char] += 1
        else:
            window[char] = 1

        while len(window) > k:
            left_char = s[left]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print(lengthOfLongestSubstringKDistinct(s, k))

"""
Time Complexity: O(n)
Space Complexity: O(1)

The time complexity is O(n) because both pointers, left and right, only move 
forward through the string. The right pointer visits each character exactly once, 
and although the while loop can run multiple times, the left pointer also advances 
at most n times over the entire algorithm. Since neither pointer ever moves backward, 
the total number of pointer movements is at most 2n, which simplifies to O(n).
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
