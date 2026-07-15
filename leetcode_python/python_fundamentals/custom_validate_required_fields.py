"""Custom debugging exercise: validate required mapping fields without crashing.

Brute force: index every required key and catch KeyError per record; O(nk) time, O(n) output.
Optimal: use `dict.get` and report rows with missing or null fields; O(nk) time, O(n) output.
Recognition: unreliable input boundaries require explicit validation rather than assumptions.
Clarify empty input, empty strings versus null, required fields, and quarantine behavior.
Edges: absent keys, explicit None, extra fields, empty records. Follow-up: return error reasons.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any


def brute_force_solution(
    records: list[Mapping[str, Any]], required: Sequence[str]
) -> list[Mapping[str, Any]]:
    return [record for record in records if any(record.get(field) is None for field in required)]


def optimal_solution(
    records: list[Mapping[str, Any]], required: Sequence[str]
) -> list[Mapping[str, Any]]:
    return brute_force_solution(records, required)
