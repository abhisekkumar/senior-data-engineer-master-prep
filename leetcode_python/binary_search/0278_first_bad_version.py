"""
LeetCode: 278
Title: First Bad Version
URL: https://leetcode.com/problems/first-bad-version/
Difficulty: Easy
Primary Pattern:
    Binary Search
Secondary Patterns:
    - None recorded
Interview Phase:
    Phase B

Restate the Problem:
    Explain the input, expected output, and objective for First Bad Version before coding.

Recognition Clues:
    - The search space is ordered, or a monotonic condition lets us discard half of the candidates.
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. Is the input sorted or rotated, can duplicates occur, and what should be returned when no match exists?
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    Track `left`, `right`, and `mid`; state which half or answer range is discarded after each comparison.
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    Scan candidates from left to right, or try every feasible answer until the condition is satisfied.
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: O(n)
    Space: O(1)

Optimal Approach:
    Apply the binary search pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: O(log n)
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
    - Using inconsistent interval boundaries or failing to prove that the search range shrinks.
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""

# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---
"""
First Bad Version / First True Boundary Search

Pattern: Binary Search on Boundary
Recognition clue: “Find the first failing / first true / first bad item.”
Platform equivalent: First failed pipeline run, first corrupted batch, first bad deployment.

Imagine Version: 1, 2, 3, 4, 5

At some point, one version becomes bad, and every version after that is also bad.

Example:
1  2  3  4  5
G  G  G  B  B

Answer: 4 because version 4 is the first bad version
You're given an API: isBadVersion(version)

Return true or false.

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
"""

n = 8
first_bad = 4

def isBadVersion(version):
    return version >= first_bad

def firstBadVersion(n):
     left = 1
     right = n
     answer = -1

     while left <= right:
          mid = (left + right) // 2

          if isBadVersion(mid):
               answer = mid

               right = mid - 1
          else:
               left = mid + 1
     return answer

print(firstBadVersion(n))

"""
Time Complexity: O(log n)
Space Complexity: O(1)

🎯 Interview Explanation (the one I want you to memorize)

If an interviewer asks:

“Why is it O(log n)?”

“Each iteration eliminates half of the remaining search space. 
Starting with n versions, the search space becomes n/2, then n/4, then n/8, 
and so on until only one candidate remains. Since the number of times you can 
halve n is log₂(n), the time complexity is O(log n).”





A good mental order for every binary search iteration is:

1. Compute mid.
2. Check the condition at mid.
3. Update left or right.
4. Start the next iteration.
"""
# --- ORIGINAL SOLUTION END ---

"""
Complexity of the Original Implementation:
    Time: O(log n)
    Space: O(1)

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
