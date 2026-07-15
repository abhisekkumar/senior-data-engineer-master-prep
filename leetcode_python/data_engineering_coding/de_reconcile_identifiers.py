"""Custom DE exercise: reconcile identifier sets between source and target.

Brute force uses repeated list membership: O(nm) time, O(n+m) output.
Optimal builds sets and subtracts them: O(n+m) average time and O(n+m) space.
Clarify duplicate meaning, null identifiers, snapshot time, filters, and desired ordering.
Recognition: bidirectional existence checks suggest set difference or a full outer join.
Edges: empty sides, duplicates, nulls. Follow-up: distributed join, late data, and backfills.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable


def brute_force_solution(
    source: list[Hashable], target: list[Hashable]
) -> dict[str, list[Hashable]]:
    return {
        "missing_in_target": sorted(value for value in source if value not in target),
        "extra_in_target": sorted(value for value in target if value not in source),
    }


def optimal_solution(
    source: Iterable[Hashable], target: Iterable[Hashable]
) -> dict[str, list[Hashable]]:
    source_values, target_values = set(source), set(target)
    return {
        "missing_in_target": sorted(source_values - target_values),
        "extra_in_target": sorted(target_values - source_values),
    }
