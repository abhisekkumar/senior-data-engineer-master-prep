"""Custom debugging exercise: count records by a required grouping key.

The original bug incremented an absent dictionary entry. Use Counter or `dict.get(key, 0)`.
Brute force rescans records per distinct key: O(nk). Optimal counts once: O(n) time, O(k) space.
Clarify missing keys, whether null is a group, and input size. Follow-up: distributed group-by.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Mapping
from typing import Any


def brute_force_solution(records: list[Mapping[str, Any]], key: str) -> dict[Hashable, int]:
    values = {record[key] for record in records}
    return {value: sum(record[key] == value for record in records) for value in values}


def optimal_solution(records: list[Mapping[str, Any]], key: str) -> dict[Hashable, int]:
    return dict(Counter(record[key] for record in records))
