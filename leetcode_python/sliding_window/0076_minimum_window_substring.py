"""
LeetCode: 76
Title: Minimum Window Substring
URL: https://leetcode.com/problems/minimum-window-substring/
Difficulty: Hard
Primary Pattern:
    Sliding Window
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Minimum Window Substring before coding.

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
    Time: O(n²m)
    Space: O(m)

Optimal Approach:
    Apply the sliding window pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n+m)
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
Recognition Clue: Variable Window + Frequency Map
minimum window,
substring,
contains all characters

Input:
s = "ADOBECODEBANC"
t = "ABC"

Output: "BANC"
"""

s = "ADOBECODEBANC"
t = "ABC"

s = "aa"
t = "aa"

def minWindow(s, t):
    need = {}

    for char in t:
        if char in need:
            need[char] += 1
        else:
            need[char] = 1

    window = {}
    left = 0
    formed = 0
    required = len(need)

    min_len = float("inf")
    min_start = 0

    for right in range(len(s)):
        char = s[right]

        if char in window:
            window[char] += 1
        else:
            window[char] = 1

        if char in need and window[char] == need[char]:
            formed += 1

        while formed == required:
            current_len = right - left + 1

            if current_len < min_len:
                min_len = current_len
                min_start = left

            left_char = s[left]
            window[left_char] -= 1

            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1

            left += 1

    if min_len == float("inf"):
        return ""

    return s[min_start:min_start + min_len]

print(minWindow(s, t))


"""
Time Complexity: O(n+m)
Space Complexity: O(m)
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n+m)
    Space: O(k)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
