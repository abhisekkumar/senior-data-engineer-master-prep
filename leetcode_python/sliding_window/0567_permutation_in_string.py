"""
LeetCode: 567
Title: Permutation in String
URL: https://leetcode.com/problems/permutation-in-string/
Difficulty: Medium
Primary Pattern:
    Sliding Window
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for Permutation in String before coding.

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
    Time: O(nm log m)
    Space: O(m)

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
Recognition Clue: permutation, same characters, same frequency, substring

That means: Fixed-size sliding window, because any permutation of s1 must have length len(s1).

Every slide is always these three steps:
Current Window
↓
1. Add the new right character
↓
2. Remove the old left character
↓
3. Compare dictionaries
"""

s1 = "ab"
s2 = "eidbaooo"

def checkInclusion(s1, s2):
     k = len(s1)
     if len(s2) < k:
          return False
     
     need = {}
     window = {}

     for char in s1:
          if char in need:
               need[char] += 1
          else:
               need[char] = 1
     for i in range(k):
          char = s2[i]
          if char in window:
               window[char] += 1
          else:
               window[char] = 1
     
     if window == need:
          return True
     
     for right in range(k, len(s2)):
          right_char = s2[right]
          left_char = s2[right - k]
          if right_char in window:
               window[right_char] += 1
          else:
               window[right_char] = 1
          window[left_char] -= 1
          if window[left_char] == 0:
               del window[left_char]
          if window == need:
               return True
     return False

               
print(checkInclusion(s1, s2))


"""
Time Complexity: O(n x k)
Space Complexity: O(1)
"""

"""
I'll implement the frequency-map sliding window version first. 
If the character set is fixed lowercase English letters, dictionary comparison is effectively O(n). 
If we need strict O(n) for a large character set, I can optimize using a matches counter.
"""
def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    need = [0] * 26
    window = [0] * 26

    for i in range(len(s1)):
        need[ord(s1[i]) - ord('a')] += 1
        window[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        if need[i] == window[i]:
            matches += 1

    left = 0
    for right in range(len(s1), len(s2)):
        if matches == 26:
            return True

        # add right char
        idx = ord(s2[right]) - ord('a')
        window[idx] += 1

        if window[idx] == need[idx]:
            matches += 1
        elif window[idx] == need[idx] + 1:
            matches -= 1

        # remove left char
        idx = ord(s2[left]) - ord('a')
        window[idx] -= 1

        if window[idx] == need[idx]:
            matches += 1
        elif window[idx] == need[idx] - 1:
            matches -= 1

        left += 1

    return matches == 26


      
          


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
