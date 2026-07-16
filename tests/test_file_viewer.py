from pathlib import Path

import pytest

from dashboard.file_viewer import (
    RepositoryFileError,
    load_repository_file,
    resolve_repository_file,
)


def test_load_repository_file_returns_safe_highlighted_preview(tmp_path: Path) -> None:
    root = tmp_path / "repository"
    source = root / "solutions/example.py"
    source.parent.mkdir(parents=True)
    source.write_text("def solve():\n    return 42\n", encoding="utf-8")

    preview = load_repository_file("solutions/example.py", root=root)

    assert preview.path == source.resolve()
    assert preview.relative_path == "solutions/example.py"
    assert preview.content == "def solve():\n    return 42\n"
    assert preview.language == "python"
    assert not preview.truncated


def test_load_repository_file_truncates_only_the_preview(tmp_path: Path) -> None:
    root = tmp_path / "repository"
    source = root / "guide.md"
    root.mkdir()
    source.write_text("abcdefghij", encoding="utf-8")

    preview = load_repository_file("guide.md", root=root, max_characters=4)

    assert preview.content == "abcd"
    assert preview.truncated
    assert source.read_text(encoding="utf-8") == "abcdefghij"


@pytest.mark.parametrize("requested", ["../private.txt", "/tmp/private.txt"])
def test_resolve_repository_file_rejects_paths_outside_root(
    tmp_path: Path, requested: str
) -> None:
    root = tmp_path / "repository"
    root.mkdir()

    with pytest.raises(RepositoryFileError, match="outside the public repository"):
        resolve_repository_file(requested, root=root)


def test_resolve_repository_file_reports_missing_file(tmp_path: Path) -> None:
    root = tmp_path / "repository"
    root.mkdir()

    with pytest.raises(RepositoryFileError, match="not found"):
        resolve_repository_file("missing.sql", root=root)
