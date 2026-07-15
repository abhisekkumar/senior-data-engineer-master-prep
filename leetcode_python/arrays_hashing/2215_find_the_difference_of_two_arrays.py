"""
LeetCode: 2215
Title: Find the Difference of Two Arrays
URL: https://leetcode.com/problems/find-the-difference-of-two-arrays/
Difficulty: Easy
Primary Pattern:
    Set
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase A

Restate the Problem:
    Explain the input, expected output, and objective for Find the Difference of Two Arrays before coding.

Recognition Clues:
    - The task requires fast membership, uniqueness, duplicate detection, or set difference.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Are duplicates meaningful, does output order matter, and may values be negative or empty?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Show the set before each lookup and after a previously unseen value is added.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Use nested scans to compare each value with the remaining input.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(nm)
    Space: O(n + m)

Optimal Approach:
    Apply the set pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(n + m)
    Space: O(n + m)

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
    - Adding at the wrong time or using a set when occurrence counts are required.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
def find_differences(source, target):
     source_set = set()
     target_set = set()

     for i in source:
          if i not in source_set:
               source_set.add(i)
     for i in target:
          if i not in target_set:
               target_set.add(i)
     return [list(source_set - target_set),  list(target_set - source_set)]

# Time Complexity: O(n + m)


"""
⭐ Interview Follow-up
Imagine: 
Source: 100 Million IDs
Target: 120 Million IDs

The two datasets don't fit in memory. What would you do?

I would first determine where the data resides. If both datasets are already in a database or 
data warehouse, I'd avoid moving them into Python entirely and perform the 
reconciliation using SQL joins or set operations.

If the data is stored in distributed storage, I'd use Spark. I'd partition both 
datasets by the same key so matching IDs are processed together, 
then perform a distributed left anti-join and right anti-join (or equivalent set difference) 
to identify missing IDs.

If the data consists of flat files that exceed memory, I'd process them in chunks or use external 
sorting and merge techniques rather than loading everything into memory.

"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(n + m)
    Space: O(n + m)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
