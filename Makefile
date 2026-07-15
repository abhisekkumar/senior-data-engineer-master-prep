.PHONY: install test lint format validate dashboard daily weekly export docs
install:
	pip install -r requirements.txt
test:
	pytest -q
lint:
	ruff check .
format:
	ruff format .
validate:
	python3 scripts/validate_questions.py
dashboard:
	streamlit run dashboard/app.py
daily:
	python3 scripts/generate_daily_plan.py
weekly:
	python3 scripts/generate_weekly_review.py
export:
	python3 scripts/export_progress.py
docs:
	python3 scripts/migrate_text_notes.py
	python3 scripts/enrich_markdown_diagrams.py
