import pytest

from scripts.enrich_markdown_diagrams import DIAGRAMS, END, START
from scripts.migrate_text_notes import (
    MAPPINGS,
    ROOT,
    SENSITIVE_METRIC,
    SENSITIVE_MONEY,
    SENSITIVE_PERCENTAGE,
    SENSITIVE_WORD_RECORD_VOLUME,
    SENSITIVE_WORD_SCALE,
    SOURCE,
    markdown_body,
    sanitize,
)


def test_every_legacy_text_note_is_mapped() -> None:
    if not SOURCE.is_dir():
        pytest.skip("private local migration sources are intentionally absent from public clones")
    source_notes = {
        path.relative_to(SOURCE).as_posix() for path in SOURCE.rglob("*.txt") if path.is_file()
    }
    assert source_notes == set(MAPPINGS)


def test_all_migrated_notes_and_fast_recognition_are_included() -> None:
    adonis_notes = {name for name in MAPPINGS if name.startswith("Companies/Adonis/")}
    assert len(adonis_notes) == 19
    source_name = "Companies/Adonis/FastRecognitionSummary.txt"
    destination = ROOT / MAPPINGS[source_name]
    migrated = destination.read_text(encoding="utf-8")
    assert destination == ROOT / "docs/pattern_recognition/FAST_RECOGNITION_SUMMARY.md"
    if SOURCE.is_dir():
        source_body = markdown_body(
            sanitize((SOURCE / source_name).read_text(encoding="utf-8"), source_name)
        )
        assert migrated.endswith(source_body)
    else:
        assert len(migrated.splitlines()) > 1_000
    assert "[Fast recognition summary](FAST_RECOGNITION_SUMMARY.md)" in (
        ROOT / "docs/pattern_recognition/README.md"
    ).read_text(encoding="utf-8")


def test_company_notes_remove_exact_personal_metrics() -> None:
    company_markdown = "\n".join(
        (ROOT / destination).read_text(encoding="utf-8")
        for source, destination in MAPPINGS.items()
        if source.startswith("Companies/Adonis/")
    )
    assert not SENSITIVE_MONEY.search(company_markdown)
    assert not SENSITIVE_PERCENTAGE.search(company_markdown)
    assert not SENSITIVE_METRIC.search(company_markdown)
    assert not SENSITIVE_WORD_RECORD_VOLUME.search(company_markdown)
    assert not SENSITIVE_WORD_SCALE.search(company_markdown)
    assert "You worked extensively" not in company_markdown
    assert "not claims about the maintainer's employment" in company_markdown


def test_company_sanitizer_does_not_remove_domain_terms() -> None:
    source_name = "Companies/Adonis/Cultural_Behavioral/HealtcareIntegration.txt"
    generic = "Claims data is useful. Eligibility determines whether a patient has coverage."
    assert sanitize(generic, source_name) == generic
    assert "[illustrative scale]" in sanitize("seven years and 2500 users", source_name)


def test_every_text_note_has_a_markdown_destination() -> None:
    assert len(MAPPINGS) == 35
    for destination in MAPPINGS.values():
        content = (ROOT / destination).read_text(encoding="utf-8")
        assert content.startswith("# ")
        assert "Publication note:" in content


def test_company_and_documentation_indexes_exist() -> None:
    expected = [
        "docs/README.md",
        "docs/dsa/README.md",
        "docs/pattern_recognition/README.md",
        "docs/python/README.md",
        "docs/sql/README.md",
        "docs/system_design/README.md",
        "companies/README.md",
        "companies/adonis/README.md",
        "companies/adonis/behavioral/README.md",
        "companies/adonis/platform_coding/README.md",
        "companies/adonis/system_design/README.md",
    ]
    assert all((ROOT / path).is_file() for path in expected)


def test_architecture_documents_have_one_complete_mermaid_block() -> None:
    assert len(DIAGRAMS) == 17
    for relative in DIAGRAMS:
        content = (ROOT / relative).read_text(encoding="utf-8")
        assert content.count(START) == 1
        assert content.count(END) == 1
        assert content.count("```mermaid") == 1
        assert "### Interview framing" in content
        assert "> **Key trade-off:**" in content
