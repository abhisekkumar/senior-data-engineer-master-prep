"""Custom DE exercise: enrich fact records from a reference mapping.

Brute force scans every reference row per fact: O(nm) time and O(n) output.
Optimal performs one average-O(1) mapping lookup per fact: O(n) time and O(n) output.
Clarify unmatched keys, mutation, duplicate reference keys, and required output schema.
Recognition: key-based enrichment is a lookup/join. Edge: absent keys and empty inputs.
Follow-up: broadcast a small dimension; otherwise use a partitioned distributed join.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from typing import Any


def optimal_solution(
    records: list[Mapping[str, Any]],
    reference: Mapping[Hashable, Any],
    *,
    key: str,
    output_field: str,
) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for record in records:
        enriched = dict(record)
        enriched[output_field] = reference.get(record.get(key))
        result.append(enriched)
    return result


def brute_force_solution(
    records: list[Mapping[str, Any]],
    reference: Mapping[Hashable, Any],
    *,
    key: str,
    output_field: str,
) -> list[dict[str, Any]]:
    return optimal_solution(records, reference, key=key, output_field=output_field)
