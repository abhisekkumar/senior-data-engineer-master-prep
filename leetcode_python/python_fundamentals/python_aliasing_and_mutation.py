"""Python fundamentals: aliasing, equality, identity, and in-place mutation.

Recognition clues: assignment aliases an object; slicing makes a shallow copy; `==` compares
values while `is` compares identity; `+=` mutates a list but rebinds an immutable value.
Clarifying questions: Is mutation allowed? Must nested values also be copied? Is identity relevant?
Baseline: guess from syntax alone, which is unreliable. Preferred approach: track object references
and whether each operation mutates or creates an object. Most operations shown are O(n) for a list.
Edge cases: nested containers, mutable defaults, and augmented assignment on different types.
Follow-ups: shallow versus deep copy; function argument passing; immutable container members.
"""

from __future__ import annotations

from copy import deepcopy
from typing import TypeVar

T = TypeVar("T")


def shallow_copy(values: list[T]) -> list[T]:
    """Copy the outer list while preserving references to nested values."""
    return values.copy()


def independent_copy(values: list[T]) -> list[T]:
    """Recursively copy values when nested mutation must be isolated."""
    return deepcopy(values)


def append_in_place(values: list[T], value: T) -> None:
    """Demonstrate that list augmented assignment mutates the caller's object."""
    values += [value]
