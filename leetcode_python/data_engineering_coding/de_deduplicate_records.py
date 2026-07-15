"""Custom DE exercise: preserve the first record for each business key.

Brute force compares each record with prior output: O(n^2) time, O(n) output.
Optimal tracks observed keys in a set: O(n) average time, O(n) space.
Clarify missing keys, first-versus-latest winner, ordering, and conflicting duplicates.
Recognition: uniqueness by a stable key suggests set membership or a distributed window.
Edges: empty input, missing key, repeated identical records. Follow-up: Spark at large scale.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from typing import Any


def brute_force_solution(records: list[Mapping[str, Any]], key: str) -> list[Mapping[str, Any]]:
    result: list[Mapping[str, Any]] = []
    for record in records:
        if not any(existing[key] == record[key] for existing in result):
            result.append(record)
    return result


def optimal_solution(records: list[Mapping[str, Any]], key: str) -> list[Mapping[str, Any]]:
    seen: set[Hashable] = set()
    result: list[Mapping[str, Any]] = []
    for record in records:
        value = record[key]
        if value not in seen:
            seen.add(value)
            result.append(record)
    return result
