from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tracker.database import ROOT, load_questions

OLD_HEADER_END = (
    "Original Implementation:\n"
    "    The code below is preserved exactly from the original study file.\n"
    '"""\n\n'
)
OLD_FOOTER_START = '\n"""\nComplexity of the Original Implementation:'
ORIGINAL_START = "# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---"
ORIGINAL_END = "# --- ORIGINAL SOLUTION END ---"

PATTERN_GUIDANCE = {
    "binary_search": {
        "recognition": "The search space is ordered, or a monotonic condition lets us discard half of the candidates.",
        "clarify": "Is the input sorted or rotated, can duplicates occur, and what should be returned when no match exists?",
        "brute": "Scan candidates from left to right, or try every feasible answer until the condition is satisfied.",
        "dry_run": "Track `left`, `right`, and `mid`; state which half or answer range is discarded after each comparison.",
        "mistake": "Using inconsistent interval boundaries or failing to prove that the search range shrinks.",
    },
    "binary_search_on_answer": {
        "recognition": "The problem asks for a minimum feasible or maximum valid value and feasibility is monotonic.",
        "clarify": "What are the smallest and largest possible answers, and how is a candidate answer validated?",
        "brute": "Try every candidate answer in the valid range and run the feasibility check for each one.",
        "dry_run": "Choose a candidate midpoint, run the feasibility test, and explain why one half of the answer range is impossible.",
        "mistake": "Binary-searching without first defining a monotonic feasibility predicate.",
    },
    "sliding_window": {
        "recognition": "The result concerns a contiguous substring or subarray whose validity can be maintained as boundaries move.",
        "clarify": "Is the window fixed or variable, are values positive, and what makes a window valid or invalid?",
        "brute": "Enumerate every contiguous range and recompute the required property for each range.",
        "dry_run": "Move the right boundary, update window state, shrink from the left when required, and record the best valid window.",
        "mistake": "Moving a boundary without updating counts or removing the outgoing value.",
    },
    "two_pointers": {
        "recognition": "The input is ordered or the answer depends on a pair/range whose boundaries can move monotonically.",
        "clarify": "Is the input sorted, must indices or values be returned, and may the input be modified?",
        "brute": "Evaluate every valid pair or range and retain the best or matching result.",
        "dry_run": "Show both pointer positions, evaluate the current state, and justify which pointer moves next.",
        "mistake": "Moving the wrong pointer without using the ordering or objective to justify it.",
    },
    "prefix_sum": {
        "recognition": "The question asks about sums or balances over many contiguous ranges, including ranges with signed values.",
        "clarify": "Can values be negative, are empty ranges allowed, and is the task to count, find, or maximize ranges?",
        "brute": "Start at every index and accumulate each possible ending range.",
        "dry_run": "Update the running prefix value, look up the required prior state, and then record the current prefix.",
        "mistake": "Forgetting the initial zero-prefix state or recording the current prefix too early.",
    },
    "stack": {
        "recognition": "The most recent unresolved item must be processed first, or nested structure must be matched.",
        "clarify": "Which tokens or values are valid, are operations guaranteed valid, and what should malformed input return?",
        "brute": "Repeatedly scan for the next resolvable pair or relationship until no work remains.",
        "dry_run": "Show the stack before and after each push or pop and explain what invariant the stack maintains.",
        "mistake": "Popping an empty stack or reversing operand order for a non-commutative operation.",
    },
    "monotonic_stack": {
        "recognition": "Each item needs the next or previous greater/smaller item and unresolved candidates can remain monotonic.",
        "clarify": "Is the comparison strictly greater, how are equal values handled, and are indices or values required?",
        "brute": "For every element, scan forward or backward until the first qualifying value is found.",
        "dry_run": "For each value, pop resolved candidates, record their answers, and push the current index.",
        "mistake": "Storing values when duplicate values require indices, or using the wrong comparison for ties.",
    },
    "heap": {
        "recognition": "Only the largest, smallest, or top `k` items are needed while data is processed incrementally.",
        "clarify": "Is `k` valid, does output order matter, how are ties handled, and can data arrive as a stream?",
        "brute": "Collect and sort all candidates, then select the required ranked items.",
        "dry_run": "Show each heap insertion or replacement and explain why the heap never needs to exceed its intended size.",
        "mistake": "Using the wrong heap direction or returning heap tuples instead of the required values.",
    },
    "intervals": {
        "recognition": "The input contains ranges and the result depends on overlap, ordering, insertion, or merging.",
        "clarify": "Are intervals sorted, can endpoints touch, are they closed or half-open, and may the input be modified?",
        "brute": "Compare intervals repeatedly and merge or report every qualifying overlap.",
        "dry_run": "Compare the current interval with the last merged interval and show whether it is appended or combined.",
        "mistake": "Using the wrong overlap condition or forgetting to sort when ordering is not guaranteed.",
    },
    "dfs": {
        "recognition": "The answer depends on recursively combining information from children, neighbors, or complete paths.",
        "clarify": "Can the structure be empty, can it contain cycles, and what counts as a complete valid path?",
        "brute": "Recompute the required subtree or path information independently for each candidate node.",
        "dry_run": "Trace one recursive path to the base case, then show the value returned and combined at each caller.",
        "mistake": "Missing a base case, confusing node count with edge count, or failing to track visited graph nodes.",
    },
    "bfs": {
        "recognition": "The result is level-based or needs the shortest path in an unweighted graph.",
        "clarify": "Can the structure be empty, are cycles possible, and should output preserve level order?",
        "brute": "Explore paths independently or repeatedly scan for the next level without a queue.",
        "dry_run": "Show the queue at the start of each level and the nodes added for the following level.",
        "mistake": "Marking nodes visited too late or mixing nodes from different levels.",
    },
    "graph_traversal": {
        "recognition": "The input represents connectivity, dependencies, components, or reachability.",
        "clarify": "Is the graph directed, can it contain cycles, is it connected, and how are nodes represented?",
        "brute": "Start a fresh traversal for each query without reusing visited or computed state.",
        "dry_run": "Trace the frontier and visited set, showing when each neighbor is discovered.",
        "mistake": "Failing to mark visited nodes or assuming a disconnected graph has one component.",
    },
    "set": {
        "recognition": "The task requires fast membership, uniqueness, duplicate detection, or set difference.",
        "clarify": "Are duplicates meaningful, does output order matter, and may values be negative or empty?",
        "brute": "Use nested scans to compare each value with the remaining input.",
        "dry_run": "Show the set before each lookup and after a previously unseen value is added.",
        "mistake": "Adding at the wrong time or using a set when occurrence counts are required.",
    },
    "hash_map": {
        "recognition": "The solution needs fast lookup from a value or signature to an index, count, or group.",
        "clarify": "Are duplicates allowed, what exactly should be returned, and can multiple answers exist?",
        "brute": "Use nested scans to compare every relevant pair or group candidate.",
        "dry_run": "Show the key being looked up and the map state after the current item is processed.",
        "mistake": "Overwriting information needed for duplicates or storing the current value before checking its complement.",
    },
}


def guidance(pattern: str) -> dict[str, str]:
    key = pattern.lower()
    for candidate, values in PATTERN_GUIDANCE.items():
        if candidate in key or key in candidate:
            return values
    return {
        "recognition": f"The constraints and requested output naturally suggest the {pattern.replace('_', ' ')} pattern.",
        "clarify": "What input guarantees, boundary cases, mutation rules, and output-order requirements apply?",
        "brute": "Use direct enumeration or repeated scans to establish a simple correctness baseline.",
        "dry_run": "Trace the main state variables through the smallest non-trivial example in the preserved notes.",
        "mistake": "Skipping contract checks or stating complexity without defining the input variables.",
    }


def extract_complexity(content: str, section: str) -> tuple[str, str]:
    match = re.search(
        rf"{re.escape(section)}:\n(?:.*\n)*?\s*Time:\s*([^\n]+)\n\s*Space:\s*([^\n]+)",
        content,
    )
    return (
        match.groups()
        if match
        else ("Documented in the preserved notes", "Documented in the preserved notes")
    )


def extract_original(content: str) -> str:
    if ORIGINAL_START in content and ORIGINAL_END in content:
        return content.split(ORIGINAL_START + "\n", 1)[1].split("\n" + ORIGINAL_END, 1)[0]
    if OLD_HEADER_END not in content or OLD_FOOTER_START not in content:
        raise ValueError("preservation boundaries were not found")
    return content.split(OLD_HEADER_END, 1)[1].rsplit(OLD_FOOTER_START, 1)[0]


def header_for(record: dict[str, Any], brute: tuple[str, str], optimal: tuple[str, str]) -> str:
    details = guidance(record["primary_pattern"])
    secondary = record.get("secondary_patterns") or []
    secondary_text = "\n".join(f"    - {item.replace('_', ' ').title()}" for item in secondary)
    if not secondary_text:
        secondary_text = "    - None recorded"
    return f'''"""
LeetCode: {record["leetcode_number"]}
Title: {record["title"]}
URL: https://leetcode.com/problems/{record["slug"]}/
Difficulty: {record["difficulty"].title()}
Primary Pattern:
    {record["primary_pattern"].replace("_", " ").title()}
Secondary Patterns:
{secondary_text}
Interview Phase:
    {record["phase"]}

Restate the Problem:
    Explain the input, expected output, and objective for {record["title"]} before coding.

Recognition Clues:
    - {details["recognition"]}
    - Identify the invariant or state that prevents repeated work.
    - Use the input constraints to confirm that the target complexity is appropriate.

Clarifying Questions:
    1. {details["clarify"]}
    2. What are the maximum input sizes and memory constraints?
    3. Are multiple answers valid, and does output order matter?

Small Example and Dry Run:
    {details["dry_run"]}
    Use the concrete example already present in the preserved solution notes and verify the final output.

Brute-Force Approach:
    {details["brute"]}
    This baseline is useful for explaining correctness but repeats work and may not scale.

Brute-Force Complexity:
    Time: {brute[0]}
    Space: {brute[1]}

Optimal Approach:
    Apply the {record["primary_pattern"].replace("_", " ")} pattern while maintaining its invariant.
    Process each state only as often as required and preserve the problem's return contract.

Optimal Complexity:
    Time: {optimal[0]}
    Space: {optimal[1]}

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
    - {details["mistake"]}
    - Giving a complexity without defining the variables
    - Changing the input or return shape without confirming the contract

Original Implementation:
    The solution between the preservation markers is the author's original code.
    Documentation tooling must never rewrite, reformat, or silently correct that block.
"""
'''


def footer_for(optimal: tuple[str, str]) -> str:
    return f'''"""
Complexity of the Original Implementation:
    Time: {optimal[0]}
    Space: {optimal[1]}

Practice Tracking:
    Record confidence, attempts, hints, coding time, explanation quality, complexity accuracy,
    mistakes, last-practiced date, and next-review date in the tracker.

Preservation Note:
    The original solution block above is unchanged. Draft syntax, naming, output, or correctness
    issues are recorded for author review rather than silently rewritten.
"""
'''


def normalize() -> None:
    normalized = 0
    for record in load_questions():
        if record.get("leetcode_number") is None:
            continue
        path = ROOT / record["file_path"]
        content = path.read_text(encoding="utf-8")
        original = extract_original(content)
        original_hash = hashlib.sha256(original.encode()).hexdigest()
        brute = extract_complexity(content, "Brute-Force Complexity")
        optimal = extract_complexity(content, "Complexity of the Original Implementation")
        updated = (
            header_for(record, brute, optimal)
            + "\n"
            + ORIGINAL_START
            + "\n"
            + original
            + "\n"
            + ORIGINAL_END
            + "\n\n"
            + footer_for(optimal)
        )
        if hashlib.sha256(extract_original(updated).encode()).hexdigest() != original_hash:
            raise RuntimeError(f"Original solution changed while normalizing {path}")
        path.write_text(updated, encoding="utf-8")
        normalized += 1
    print(f"Normalized {normalized} numbered question headers without changing solution bodies.")


if __name__ == "__main__":
    normalize()
