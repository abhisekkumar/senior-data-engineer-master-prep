from dashboard.services import (
    dashboard_data,
    filter_questions,
    progress_data,
    review_queues,
    study_resources,
)


def test_dashboard_data_loads_without_streamlit_runtime() -> None:
    data = dashboard_data()
    assert data["summary"]["total_questions"] == 80
    assert len(data["today"]["items"]) == 5
    assert data["summary"]["sources"]["sql"] == 6


def test_filter_questions() -> None:
    questions = dashboard_data()["questions"]
    assert {q["id"] for q in filter_questions(questions, query="two sum")} == {
        "leetcode-0001",
        "leetcode-0167",
    }


def test_filter_questions_supports_tracker_fields() -> None:
    questions = dashboard_data()["questions"]
    filtered = filter_questions(
        questions,
        category="binary_search",
        difficulty="medium",
        confidence="3",
        due="Unscheduled",
    )
    assert filtered
    assert all(question["category"] == "binary_search" for question in filtered)
    assert all(question["difficulty"] == "medium" for question in filtered)


def test_filter_questions_supports_sql_source() -> None:
    questions = dashboard_data()["questions"]
    filtered = filter_questions(questions, source="sql")
    assert len(filtered) == 6
    assert all(question["file_path"].endswith(".sql") for question in filtered)


def test_review_and_progress_views_return_all_sections() -> None:
    data = dashboard_data()
    queues = review_queues(data["questions"])
    assert set(queues) == {
        "Overdue",
        "Due today",
        "Due this week",
        "Lowest confidence",
        "Frequently missed",
    }
    progress = progress_data(data["questions"], data["attempts"])
    assert set(progress) == {
        "attempts_by_day",
        "confidence_by_day",
        "completed_by_category",
        "average_minutes_by_category",
        "mistakes",
    }


def test_study_resources_include_guides_and_sql() -> None:
    resources = study_resources()
    assert any(item["collection"] == "Interview guides" for item in resources)
    assert any(item["format"] == "SQL" for item in resources)
    assert all(not item["file_path"].startswith("Senior Data Engineer") for item in resources)
