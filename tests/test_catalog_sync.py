import json
from pathlib import Path

from tracker.catalog import discover_catalog, sync_catalog


def test_discovers_python_sql_and_custom_exercises(tmp_path: Path) -> None:
    python_dir = tmp_path / "leetcode_python" / "arrays_hashing"
    custom_dir = tmp_path / "leetcode_python" / "data_engineering_coding"
    sql_dir = tmp_path / "sql" / "window_functions"
    python_dir.mkdir(parents=True)
    custom_dir.mkdir(parents=True)
    sql_dir.mkdir(parents=True)
    (python_dir / "0001_two_sum.py").write_text(
        '"""\nTitle: Two Sum\nDifficulty: Easy\nPrimary Pattern: Hash map\n"""\n',
        encoding="utf-8",
    )
    (custom_dir / "deduplicate_events.py").write_text("def solve(): pass\n", encoding="utf-8")
    (sql_dir / "running_total.sql").write_text(
        "-- Title: Running total\n-- Difficulty: Hard\nSELECT 1;\n",
        encoding="utf-8",
    )

    records = {record["source"]: record for record in discover_catalog(tmp_path)}

    assert records["leetcode"]["id"] == "leetcode-0001"
    assert records["custom"]["leetcode_number"] is None
    assert records["sql"]["category"] == "sql_window_functions"
    assert records["sql"]["difficulty"] == "hard"


def test_sync_adds_new_files_and_preserves_existing_state(tmp_path: Path) -> None:
    python_dir = tmp_path / "leetcode_python" / "arrays_hashing"
    sql_dir = tmp_path / "sql" / "analytics"
    tracker_dir = tmp_path / "tracker"
    python_dir.mkdir(parents=True)
    sql_dir.mkdir(parents=True)
    tracker_dir.mkdir()
    python_path = python_dir / "0001_two_sum.py"
    python_path.write_text("# solution\n", encoding="utf-8")
    (sql_dir / "daily_active_users.sql").write_text("SELECT 1;\n", encoding="utf-8")
    questions_path = tracker_dir / "questions.json"
    questions_path.write_text(
        json.dumps(
            [
                {
                    "id": "leetcode-0001",
                    "file_path": "leetcode_python/arrays_hashing/0001_two_sum.py",
                    "status": "completed",
                }
            ]
        ),
        encoding="utf-8",
    )

    result = sync_catalog(tmp_path, questions_path)
    saved = json.loads(questions_path.read_text(encoding="utf-8"))

    assert [question["id"] for question in result["added"]] == ["sql-analytics-daily-active-users"]
    assert saved[0]["status"] == "completed"
    assert len(saved) == 2
