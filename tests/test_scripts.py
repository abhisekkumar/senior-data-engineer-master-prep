import argparse

import pytest

from scripts.add_question import slugify
from scripts.log_practice import score


@pytest.mark.parametrize(
    "title,expected",
    [
        ("Top K Frequent Elements", "top_k_frequent_elements"),
        ("3Sum", "3sum"),
        ("  Merge Sorted Array!  ", "merge_sorted_array"),
    ],
)
def test_slugify(title: str, expected: str) -> None:
    assert slugify(title) == expected


@pytest.mark.parametrize("value", ["0", "3", "5"])
def test_score_accepts_rubric_range(value: str) -> None:
    assert score(value) == int(value)


@pytest.mark.parametrize("value", ["-1", "6"])
def test_score_rejects_values_outside_rubric(value: str) -> None:
    with pytest.raises(argparse.ArgumentTypeError):
        score(value)
