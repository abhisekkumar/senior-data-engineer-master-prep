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
            column.metric(label, f"{value} {suffix}" if suffix else value, border=True)


def question_table(questions: list[dict[str, Any]]) -> None:
    columns = [
        "source",
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
    st.dataframe(
        rows,
        width="stretch",
        hide_index=True,
        column_config={
            "source": st.column_config.TextColumn("Source", pinned=True),
            "leetcode_number": st.column_config.NumberColumn("LeetCode", format="%d"),
            "title": st.column_config.TextColumn("Question", pinned=True),
            "primary_pattern": st.column_config.TextColumn("Pattern"),
            "category": st.column_config.TextColumn("Category"),
            "difficulty": st.column_config.TextColumn("Difficulty"),
            "status": st.column_config.TextColumn("Status"),
            "confidence": st.column_config.ProgressColumn(
                "Confidence", min_value=0, max_value=5, format="%d / 5"
            ),
            "attempts": st.column_config.NumberColumn("Attempts", format="%d"),
            "next_review": st.column_config.DateColumn("Next review", format="MMM D, YYYY"),
            "mistake_tags": st.column_config.ListColumn("Mistakes"),
            "file_path": st.column_config.TextColumn("Local file"),
        },
    )


def resource_table(resources: list[dict[str, str]]) -> None:
    st.dataframe(
        resources,
        width="stretch",
        hide_index=True,
        column_config={
            "title": st.column_config.TextColumn("Resource", pinned=True),
            "collection": st.column_config.TextColumn("Collection"),
            "topic": st.column_config.TextColumn("Topic"),
            "format": st.column_config.TextColumn("Format"),
            "file_path": st.column_config.TextColumn("Local file"),
        },
    )
