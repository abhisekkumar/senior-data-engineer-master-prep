"""
LeetCode: 242
Title: Valid Anagram
URL: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Primary Pattern:
    Frequency Counting
Secondary Patterns:
    - Sorting
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Valid Anagram before coding.

Recognition Clues:
    - The constraints and requested output naturally suggest the frequency counting pattern.
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
    Time: O(n log n)
    Space: O(n)

Optimal Approach:
    Apply the frequency counting pattern while maintaining its invariant.
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
from collections import Counter
s = "anagram"
t = "nagaram"

# With counter

def isAnagram(s, t):
     return Counter(s) == Counter(t)


def isAnagram(s, t):
     if len(s) != len(t):
          return False
     freq = {}

     for ch in s:
          freq[ch] = freq.get(ch, 0) + 1
     
     for ch in t:
          if ch not in freq:
               return False
          freq[ch] -= 1

          if freq[ch] < 0:
               return False:
     return True


"""
⭐ Interview Follow-up

Here comes the Adonis-style follow-up.
Imagine these aren't strings anymore.
They're two files containing 100 million patient IDs.
You need to determine whether both files contain exactly the same IDs with the same frequency.
You cannot load both files into memory.
How would you solve it?


Since the files are too large to fit in memory, I would not build a local dictionary for both files. 
I'd use a distributed approach such as Spark.
For each file, I would group by patient ID and count occurrences:
file_a_counts = patient_id, count_a
file_b_counts = patient_id, count_b

Then I'd full outer join on patient_id and check where counts differ 
or where an ID exists in one file but not the other.

If the result set is empty, both files contain the same IDs with the same frequency.

This handles duplicates correctly, not just presence/absence.




Interview Card #3 — Valid Anagram

| Section             | Answer                                                      |
| ------------------- | ----------------------------------------------------------- |
| Pattern             | Frequency Map                                               |
| Brute Force         | Sort both strings and compare                               |
| Brute Force Time    | O(n log n)                                                  |
| Optimal             | Count characters in `s`, subtract using `t`                 |
| Optimal Time        | O(n)                                                        |
| Space               | O(k), unique characters                                     |
| Common Mistake      | Forgetting length check, not handling negative counts       |
| Platform Equivalent | Compare two datasets for same IDs and counts                |
| Senior Follow-up    | For huge files, aggregate counts per ID and full outer join |

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
