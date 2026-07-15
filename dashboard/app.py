from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

# Streamlit executes this file as a script. Add the repository root so package
# imports work for the documented `streamlit run dashboard/app.py` command.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.components import metric_grid, question_table, resource_table
from dashboard.services import (
    dashboard_data,
    filter_questions,
    log_practice_attempt,
    progress_data,
    question_by_id,
    question_file,
    review_queues,
    update_daily_task,
)

st.set_page_config(
    page_title="Senior Data Engineering Interview Prep",
    page_icon=":material/school:",
    layout="wide",
    initial_sidebar_state="expanded",
)
data = dashboard_data(persist_plan=True)


def humanize(value: str) -> str:
    return value.replace("_", " ").replace("-", " ").strip().capitalize()


def chart_values(values: dict[str, float | int]) -> dict[str, float | int]:
    return {humanize(label): value for label, value in values.items()}


def render_chart(values: dict[str, float | int], chart_type: str) -> None:
    if not values:
        st.caption("No practice data yet. Complete an attempt to populate this chart.")
    elif chart_type == "line":
        st.line_chart(chart_values(values))
    else:
        st.bar_chart(chart_values(values))


with st.sidebar:
    st.markdown("## :material/school: Study hub")
    st.caption("A local-first workspace for focused senior data engineering preparation.")
    st.markdown(
        f":blue-badge[{data['summary']['total_questions']} exercises] "
        f":green-badge[{len(data['resources'])} study resources]"
    )
    st.markdown("**Automatic catalog**")
    st.caption(
        "Python files under `leetcode_python/` and SQL files under `sql/` are synchronized "
        "when the app opens. Existing progress is never overwritten."
    )
    st.markdown("**Quick commands**")
    st.code("make sync\nmake daily\nmake dashboard", language="bash")
    st.caption("All tracker data stays in local JSON files under `tracker/`.")

st.title(":material/database: Senior Data Engineering Interview Prep")
st.caption(
    "Practice Python, SQL, system design, and senior-level communication with a clear daily loop."
)
st.markdown(
    ":blue-badge[Python & DSA] :violet-badge[SQL] "
    ":green-badge[Data engineering] :orange-badge[System design]"
)

if data["catalog_sync"]["added"]:
    st.toast(
        f"Added {len(data['catalog_sync']['added'])} new exercises to the tracker.",
        icon=":material/sync:",
    )
if data["catalog_sync"]["conflicts"]:
    st.warning(
        "Some new files have duplicate tracker identifiers. Run `make sync` for details.",
        icon=":material/warning:",
    )

tabs = st.tabs(
    [
        ":material/dashboard: Overview",
        ":material/today: Today's five",
        ":material/code: Question library",
        ":material/event_repeat: Review queue",
        ":material/library_books: Study library",
        ":material/monitoring: Progress",
    ]
)

with tabs[0]:
    metric_grid(data["summary"])
    left, right = st.columns(2)
    with left:
        with st.container(border=True):
            st.subheader(":material/hub: Exercises by pattern")
            st.bar_chart(chart_values(data["summary"]["patterns"]))
    with right:
        with st.container(border=True):
            st.subheader(":material/source: Exercises by source")
            st.bar_chart(chart_values(data["summary"]["sources"]))
    plan_completed = sum(item.get("status") == "completed" for item in data["today"]["items"])
    left, right = st.columns([2, 1])
    with left:
        with st.container(border=True):
            st.subheader(":material/rocket_launch: Today's momentum")
            st.progress(plan_completed / 5, text=f"{plan_completed} of 5 study tasks completed")
            st.caption("Open Today's five to continue the plan or record a practice attempt.")
    with right:
        with st.container(border=True):
            st.subheader(":material/signal_cellular_alt: Difficulty mix")
            st.bar_chart(chart_values(data["summary"]["difficulties"]))

with tabs[1]:
    st.subheader(f":material/checklist: Study plan for {data['today']['date']}")
    st.caption("Complete the five positions in order; due reviews take priority over new work.")
    st.progress(plan_completed / 5, text=f"Daily plan: {plan_completed} of 5 complete")
    for item in data["today"]["items"]:
        position = item["position"]
        label = humanize(item["type"])
        question = (
            question_by_id(data["questions"], item["question_id"])
            if item.get("question_id")
            else None
        )
        title = question["title"] if question else item.get("topic", "Study task")
        status = item.get("status", "not_started")
        expander_icon = ":material/task_alt:" if status == "completed" else ":material/pending:"
        with st.expander(
            f"{position}. {label}: {title} — {humanize(status)}",
            icon=expander_icon,
        ):
            if question:
                path = question_file(question)
                st.markdown(
                    f":blue-badge[{humanize(question['source'])}] "
                    f":violet-badge[{humanize(question['primary_pattern'])}] "
                    f":orange-badge[{humanize(question['difficulty'])}] "
                    f":green-badge[Confidence {question['confidence']}/5]"
                )
                st.code(question["file_path"], language=None)
                st.markdown(f"[Open the local solution file]({path.as_uri()})")
                if status == "not_started" and st.button(
                    "Mark task started",
                    key=f"start-{data['today']['date']}-{position}",
                    icon=":material/play_arrow:",
                ):
                    update_daily_task(
                        plan_date=data["today"]["date"],
                        position=position,
                        status="started",
                    )
                    st.rerun()

                with st.form(f"practice-{data['today']['date']}-{position}"):
                    result = st.selectbox(
                        "Result",
                        ["completed", "completed_with_hint", "incorrect"],
                        format_func=humanize,
                    )
                    first, second, third = st.columns(3)
                    confidence_before = first.slider("Confidence before", 1, 5, 3)
                    confidence_after = second.slider("Confidence after", 1, 5, 3)
                    minutes = third.number_input("Minutes spent", 0, 300, 25)
                    hints = st.number_input("Hints used", 0, 20, 0)
                    mistakes_text = st.text_input(
                        "Mistake tags",
                        placeholder="heap_direction, boundary_condition",
                    )
                    notes = st.text_area("Practice notes")
                    st.markdown("**Interview skill scores (0–5)**")
                    score_columns = st.columns(3)
                    clarification = score_columns[0].slider("Clarifying questions", 0, 5, 3)
                    brute_force = score_columns[1].slider("Brute force", 0, 5, 3)
                    optimal = score_columns[2].slider("Optimal approach", 0, 5, 3)
                    score_columns = st.columns(3)
                    coding = score_columns[0].slider("Coding", 0, 5, 3)
                    complexity = score_columns[1].slider("Complexity", 0, 5, 3)
                    communication = score_columns[2].slider("Communication", 0, 5, 3)
                    submitted = st.form_submit_button(
                        "Save completed practice attempt", icon=":material/save:"
                    )
                    if submitted:
                        mistakes = [
                            value.strip() for value in mistakes_text.split(",") if value.strip()
                        ]
                        attempt = log_practice_attempt(
                            question_id=question["id"],
                            result=result,
                            confidence_before=confidence_before,
                            confidence_after=confidence_after,
                            minutes_spent=minutes,
                            hints_used=hints,
                            mistakes=mistakes,
                            notes=notes,
                            clarifying_questions_score=clarification,
                            brute_force_score=brute_force,
                            optimal_approach_score=optimal,
                            coding_score=coding,
                            complexity_score=complexity,
                            communication_score=communication,
                        )
                        update_daily_task(
                            plan_date=data["today"]["date"],
                            position=position,
                            status="completed",
                            minutes_spent=minutes,
                            notes=notes,
                        )
                        st.success(
                            f"Saved {attempt['attempt_id']} with confidence "
                            f"{attempt['confidence_after']}/5.",
                            icon=":material/check_circle:",
                        )
                        st.rerun()
            else:
                with st.form(f"task-{data['today']['date']}-{position}"):
                    task_status = st.selectbox(
                        "Status",
                        ["not_started", "started", "completed"],
                        index=["not_started", "started", "completed"].index(status),
                        format_func=humanize,
                    )
                    minutes = st.number_input("Minutes spent", 0, 300, item.get("minutes_spent", 0))
                    notes = st.text_area("Notes", value=item.get("notes", ""))
                    if st.form_submit_button("Save task", icon=":material/save:"):
                        update_daily_task(
                            plan_date=data["today"]["date"],
                            position=position,
                            status=task_status,
                            minutes_spent=minutes,
                            notes=notes,
                        )
                        st.success("Task updated.", icon=":material/check_circle:")
                        st.rerun()

with tabs[2]:
    st.subheader(":material/code: Question library")
    st.caption("Python, LeetCode, custom data-engineering exercises, and SQL in one tracker.")
    with st.container(border=True):
        first, second, third = st.columns([2, 1, 1])
        query = first.text_input(
            "Search",
            placeholder="LeetCode number, title, tracker ID, or keyword",
        )
        source = second.selectbox(
            "Source", ["All", *sorted({q["source"] for q in data["questions"]})]
        )
        difficulty = third.selectbox("Difficulty", ["All", "easy", "medium", "hard"])
        first, second, third, fourth = st.columns(4)
        pattern = first.selectbox(
            "Pattern", ["All", *sorted({q["primary_pattern"] for q in data["questions"]})]
        )
        category = second.selectbox(
            "Category", ["All", *sorted({q["category"] for q in data["questions"]})]
        )
        status = third.selectbox(
            "Status", ["All", *sorted({q["status"] for q in data["questions"]})]
        )
        confidence = fourth.selectbox("Confidence", ["All", "1", "2", "3", "4", "5"])
        first, second = st.columns(2)
        due = first.selectbox(
            "Due date", ["All", "Overdue", "Today", "This week", "Unscheduled"]
        )
        mistake_tag = second.text_input("Mistake tag", placeholder="boundary condition")
    filtered = filter_questions(
        data["questions"],
        query=query,
        source=source,
        pattern=pattern,
        category=category,
        difficulty=difficulty,
        status=status,
        confidence=confidence,
        due=due,
        mistake_tag=mistake_tag,
    )
    st.caption(f"{len(filtered)} matching exercises")
    question_table(filtered)

with tabs[3]:
    st.subheader(":material/event_repeat: Review queue")
    st.caption("Prioritize due work, low confidence, and recurring mistakes.")
    for label, questions in review_queues(data["questions"]).items():
        with st.expander(
            f"{label} — {len(questions)} exercises",
            icon=":material/schedule:",
            expanded=label in {"Overdue", "Due today"} and bool(questions),
        ):
            if questions:
                question_table(questions)
            else:
                st.caption("Nothing in this queue right now.")

with tabs[4]:
    st.subheader(":material/library_books: Study library")
    st.caption("Browse public guides, SQL examples, system-design notes, and study plans.")
    first, second, third = st.columns([2, 1, 1])
    resource_query = first.text_input("Search resources", placeholder="CDC, Spark, SQL, behavioral")
    resource_collection = second.selectbox(
        "Collection", ["All", *sorted({item["collection"] for item in data["resources"]})]
    )
    resource_format = third.segmented_control(
        "Format", ["All", "Guide", "SQL"], default="All"
    )
    resource_query = resource_query.casefold().strip()
    filtered_resources = [
        item
        for item in data["resources"]
        if (
            not resource_query
            or resource_query in item["title"].casefold()
            or resource_query in item["topic"].casefold()
            or resource_query in item["file_path"].casefold()
        )
        and (resource_collection == "All" or item["collection"] == resource_collection)
        and (resource_format == "All" or item["format"] == resource_format)
    ]
    st.caption(f"{len(filtered_resources)} matching resources")
    resource_table(filtered_resources)

with tabs[5]:
    st.subheader(":material/monitoring: Progress")
    st.caption("Track practice consistency, confidence, timing, completion, and recurring mistakes.")
    progress = progress_data(data["questions"], data["attempts"])
    # Keep the Progress view usable inside Streamlit's tab panel. A fixed-height
    # native container gets its own vertical scrollbar when the charts exceed it.
    with st.container(height=500, border=False, key="progress-scroll"):
        left, right = st.columns(2)
        with left:
            with st.container(border=True):
                st.markdown("### Practice attempts over time")
                render_chart(progress["attempts_by_day"], "line")
            with st.container(border=True):
                st.markdown("### Exercises completed by category")
                render_chart(progress["completed_by_category"], "bar")
            with st.container(border=True):
                st.markdown("### Mistakes by type")
                render_chart(progress["mistakes"], "bar")
        with right:
            with st.container(border=True):
                st.markdown("### Confidence over time")
                render_chart(progress["confidence_by_day"], "line")
            with st.container(border=True):
                st.markdown("### Average time by category")
                render_chart(progress["average_minutes_by_category"], "bar")
