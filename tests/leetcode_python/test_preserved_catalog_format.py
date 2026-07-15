import pytest

from scripts.normalize_question_headers import extract_original
from tracker.database import ROOT, load_questions

REQUIRED_SECTIONS = (
    "LeetCode:",
    "Title:",
    "URL:",
    "Difficulty:",
    "Primary Pattern:",
    "Secondary Patterns:",
    "Interview Phase:",
    "Restate the Problem:",
    "Recognition Clues:",
    "Clarifying Questions:",
    "Small Example and Dry Run:",
    "Brute-Force Approach:",
    "Brute-Force Complexity:",
    "Optimal Approach:",
    "Optimal Complexity:",
    "Why This Approach:",
    "Important Edge Cases:",
    "Interviewer Follow-Ups:",
    "Common Mistakes:",
    "Original Implementation:",
    "Complexity of the Original Implementation:",
)


def test_numbered_catalog_has_interview_sections() -> None:
    numbered = [record for record in load_questions() if record["leetcode_number"] is not None]
    assert len(numbered) == 68
    for record in numbered:
        content = (ROOT / record["file_path"]).read_text(encoding="utf-8")
        missing = [section for section in REQUIRED_SECTIONS if section not in content]
        assert not missing, f"{record['file_path']} is missing {missing}"
        assert content.count("# --- ORIGINAL SOLUTION START (PRESERVE EXACTLY) ---") == 1
        assert content.count("# --- ORIGINAL SOLUTION END ---") == 1


def test_original_source_directory_stays_gitignored() -> None:
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "Senior Data Engineer Interview Prep/" in gitignore


def test_preserved_blocks_match_a_legacy_source_when_local_sources_exist() -> None:
    source_root = ROOT / "Senior Data Engineer Interview Prep"
    if not source_root.is_dir():
        pytest.skip("private local migration sources are intentionally absent from public clones")
    legacy_sources = [path.read_text(encoding="utf-8") for path in source_root.rglob("*.py")]
    numbered = [record for record in load_questions() if record["leetcode_number"] is not None]
    unmatched: list[str] = []
    for record in numbered:
        content = (ROOT / record["file_path"]).read_text(encoding="utf-8")
        preserved = extract_original(content).strip()
        if not any(preserved in source for source in legacy_sources):
            unmatched.append(record["file_path"])
    assert not unmatched, f"preserved blocks no longer match a local legacy source: {unmatched}"
