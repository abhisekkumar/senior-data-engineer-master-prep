from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

# Streamlit executes this file as a script. Add the repository root so package
# imports work for the documented `streamlit run dashboard/app.py` command.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.components import metric_grid, question_table
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

st.set_page_config(page_title="Senior DE Interview Prep", page_icon="📚", layout="wide")
data = dashboard_data(persist_plan=True)
st.title("Senior Data Engineering Interview Prep")
st.caption("Local-only practice tracking, spaced repetition, and five-item daily planning.")

tabs = st.tabs(["Dashboard", "Today's Five", "Question Library", "Review Queue", "Progress"])

with tabs[0]:
    metric_grid(data["summary"])
    left, right = st.columns(2)
    with left:
        st.subheader("Questions by pattern")
        st.bar_chart(data["summary"]["patterns"])
    with right:
        st.subheader("Questions by difficulty")
        st.bar_chart(data["summary"]["difficulties"])
    st.info("Generate a plan from the command line with `make daily`, or use Today's Five below.")

with tabs[1]:
    st.subheader(f"Study plan for {data['today']['date']}")
    st.write("Complete the five positions in order; due reviews take priority over extra new work.")
    for item in data["today"]["items"]:
        position = item["position"]
        label = item["type"].replace("_", " ").title()
        question = (
            question_by_id(data["questions"], item["question_id"])
            if item.get("question_id")
            else None
        )
        title = question["title"] if question else item.get("topic", "Study task")
        status = item.get("status", "not_started")
        with st.expander(f"{position}. {label}: {title} — {status.replace('_', ' ').title()}"):
            if question:
                path = question_file(question)
                st.write(
                    f"**Pattern:** {question['primary_pattern'].replace('_', ' ').title()}  "
                    f"\n**Difficulty:** {question['difficulty'].title()}  "
                    f"\n**Confidence:** {question['confidence']}/5"
                )
                st.code(question["file_path"], language=None)
                st.markdown(f"[Open the local solution file]({path.as_uri()})")
                if status == "not_started" and st.button(
                    "Mark task started", key=f"start-{data['today']['date']}-{position}"
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
                        format_func=lambda value: value.replace("_", " ").title(),
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
                    submitted = st.form_submit_button("Save completed practice attempt")
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
                            f"{attempt['confidence_after']}/5."
                        )
                        st.rerun()
            else:
                with st.form(f"task-{data['today']['date']}-{position}"):
                    task_status = st.selectbox(
                        "Status",
                        ["not_started", "started", "completed"],
                        index=["not_started", "started", "completed"].index(status),
                        format_func=lambda value: value.replace("_", " ").title(),
                    )
                    minutes = st.number_input("Minutes spent", 0, 300, item.get("minutes_spent", 0))
                    notes = st.text_area("Notes", value=item.get("notes", ""))
                    if st.form_submit_button("Save task"):
                        update_daily_task(
                            plan_date=data["today"]["date"],
                            position=position,
                            status=task_status,
                            minutes_spent=minutes,
                            notes=notes,
                        )
                        st.success("Task updated.")
                        st.rerun()

with tabs[2]:
    st.subheader("Question Library")
    first, second, third, fourth = st.columns(4)
    query = first.text_input("LeetCode number, title, or ID")
    pattern = second.selectbox(
        "Pattern", ["All", *sorted({q["primary_pattern"] for q in data["questions"]})]
    )
    category = third.selectbox(
        "Category", ["All", *sorted({q["category"] for q in data["questions"]})]
    )
    difficulty = fourth.selectbox("Difficulty", ["All", "easy", "medium", "hard"])
    first, second, third, fourth = st.columns(4)
    status = first.selectbox("Status", ["All", *sorted({q["status"] for q in data["questions"]})])
    confidence = second.selectbox("Confidence", ["All", "1", "2", "3", "4", "5"])
    due = third.selectbox("Due date", ["All", "Overdue", "Today", "This week", "Unscheduled"])
    mistake_tag = fourth.text_input("Mistake tag")
    filtered = filter_questions(
        data["questions"],
        query=query,
        pattern=pattern,
        category=category,
        difficulty=difficulty,
        status=status,
        confidence=confidence,
        due=due,
        mistake_tag=mistake_tag,
    )
    st.caption(f"{len(filtered)} matching questions")
    question_table(filtered)

with tabs[3]:
    st.subheader("Review Queue")
    for label, questions in review_queues(data["questions"]).items():
        st.markdown(f"### {label} ({len(questions)})")
        question_table(questions)

with tabs[4]:
    st.subheader("Progress")
    progress = progress_data(data["questions"], data["attempts"])
    # Keep the Progress view usable inside Streamlit's tab panel. A fixed-height
    # native container gets its own vertical scrollbar when the charts exceed it.
    with st.container(height=500, border=False, key="progress-scroll"):
        left, right = st.columns(2)
        with left:
            st.markdown("### Practice attempts over time")
            st.line_chart(progress["attempts_by_day"])
            st.markdown("### Questions completed by category")
            st.bar_chart(progress["completed_by_category"])
            st.markdown("### Mistakes by type")
            st.bar_chart(progress["mistakes"])
        with right:
            st.markdown("### Confidence over time")
            st.line_chart(progress["confidence_by_day"])
            st.markdown("### Average time by category")
            st.bar_chart(progress["average_minutes_by_category"])
