from leetcode_python.data_engineering_coding.de_count_records_by_key import (
    optimal_solution as count,
)
from leetcode_python.data_engineering_coding.de_deduplicate_records import (
    optimal_solution as deduplicate,
)
from leetcode_python.data_engineering_coding.de_enrich_records_from_reference import (
    optimal_solution as enrich,
)
from leetcode_python.data_engineering_coding.de_reconcile_identifiers import (
    optimal_solution as reconcile,
)
from leetcode_python.python_fundamentals.custom_validate_required_fields import (
    optimal_solution as invalid,
)
from leetcode_python.python_fundamentals.python_aliasing_and_mutation import (
    append_in_place,
    shallow_copy,
)


def test_data_engineering_exercises() -> None:
    records = [{"id": 1, "value": "a"}, {"id": 1, "value": "b"}, {"id": 2, "value": "c"}]
    assert deduplicate(records, "id") == [records[0], records[2]]
    assert reconcile([1, 2, 3], [2, 3, 4]) == {"missing_in_target": [1], "extra_in_target": [4]}
    assert count([{"group": "a"}, {"group": "a"}, {"group": "b"}], "group") == {"a": 2, "b": 1}
    assert enrich([{"key": 1}, {"key": 9}], {1: "known"}, key="key", output_field="label") == [
        {"key": 1, "label": "known"},
        {"key": 9, "label": None},
    ]


def test_python_debugging_and_mutation() -> None:
    rows = [{"id": 1, "name": "ok"}, {"id": 2}, {"id": None, "name": "bad"}]
    assert invalid(rows, ["id", "name"]) == rows[1:]
    original = [[1]]
    copied = shallow_copy(original)
    assert copied is not original and copied[0] is original[0]
    values = [1, 2]
    append_in_place(values, 3)
    assert values == [1, 2, 3]
