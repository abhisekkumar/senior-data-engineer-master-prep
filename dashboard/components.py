from __future__ import annotations

from typing import Any

import streamlit as st


def metric_grid(values: dict[str, Any]) -> None:
    metrics = [
        ("Total questions", "total_questions", None),
        ("Completed", "completed", None),
        ("Not started", "not_started", None),
        ("Due today", "due_today", None),
        ("Average confidence", "average_confidence", "/ 5"),
        ("Current streak", "streak", "days"),
        ("Practice attempts", "attempts", None),
        ("Average practice time", "average_minutes", "minutes"),
    ]
    for start in range(0, len(metrics), 4):
        columns = st.columns(4)
        for column, (label, key, suffix) in zip(columns, metrics[start : start + 4], strict=True):
            value = values[key]
            column.metric(label, f"{value} {suffix}" if suffix else value)


def question_table(questions: list[dict[str, Any]]) -> None:
    columns = [
        "leetcode_number",
        "title",
        "primary_pattern",
        "category",
        "difficulty",
        "status",
        "confidence",
        "attempts",
        "next_review",
        "mistake_tags",
        "file_path",
    ]
    rows = [{column: question.get(column) for column in columns} for question in questions]
    st.dataframe(rows, width="stretch", hide_index=True)
