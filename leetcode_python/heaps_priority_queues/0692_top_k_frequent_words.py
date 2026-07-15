"""
LeetCode: 692
Title: Top K Frequent Words
URL: https://leetcode.com/problems/top-k-frequent-words/
Difficulty: Medium
Primary Pattern:
    Frequency Counting
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Top K Frequent Words before coding.

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
    Time: O(n + m log m)
    Space: O(m)

Optimal Approach:
    Apply the frequency counting pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n + m log k)
    Space: O(m + k)

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
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. 
Sort the words with the same frequency by their lexicographical order.

Input: 
words = ["i","love","leetcode","i","love","coding"]
k = 2

Output: 
["i","love"]
"""
words = ["i","love","leetcode","i","love","coding"]
k = 3
from collections import Counter

def top_k_frequent_words(words, k):
     counts = Counter(words)
     print(counts)
     sorted_words = sorted(counts.keys(), key=lambda word:(-counts[word], word))
     print(sorted_words)
     return sorted_words[:k]

print(top_k_frequent_words(words, k))



"""
Time Complexity: O(n + u log u + k log u)
Space Complexity: O(u)

where n = total words, u = unique words.
"""


"""
I can solve this with sorting more simply, but heap is useful if k is much smaller than 
the number of unique words. Here, because of lexicographical tie-breaking, 
I'd push (-count, word) into the heap.
"""

def top_k_frequent_words(words, k):
     counts = Counter(words)
     heap = []

     for word, count in count.items():
          heapq.heappush(heap, (-count, word))

     result = []

     for _ in range(k):
          count, word = heapq.heappop(heap)
          result.append(word)
     return result


# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n + m log k)
    Space: O(m + k)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
