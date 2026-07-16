from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import streamlit as st

from tracker.database import ROOT

MAX_PREVIEW_CHARACTERS = 200_000
LANGUAGES = {
    ".json": "json",
    ".md": "markdown",
    ".py": "python",
    ".sql": "sql",
    ".toml": "toml",
    ".yaml": "yaml",
    ".yml": "yaml",
}


class RepositoryFileError(ValueError):
    """Raised when a dashboard file request is unsafe or unavailable."""


@dataclass(frozen=True, slots=True)
class RepositoryFile:
    path: Path
    relative_path: str
    content: str
    language: str | None
    truncated: bool


def resolve_repository_file(
    file_path: str | Path, *, root: Path | None = None
) -> tuple[Path, Path]:
    repository_root = (root or ROOT).resolve()
    candidate = Path(file_path)
    candidate = candidate if candidate.is_absolute() else repository_root / candidate
    resolved = candidate.resolve()
    try:
        relative = resolved.relative_to(repository_root)
    except ValueError as exc:
        raise RepositoryFileError("The requested file is outside the public repository.") from exc
    if not resolved.is_file():
        raise RepositoryFileError(f"Repository file not found: {relative.as_posix()}")
    return resolved, relative


def load_repository_file(
    file_path: str | Path,
    *,
    root: Path | None = None,
    max_characters: int = MAX_PREVIEW_CHARACTERS,
) -> RepositoryFile:
    if max_characters < 1:
        raise ValueError("max_characters must be positive")
    resolved, relative = resolve_repository_file(file_path, root=root)
    try:
        content = resolved.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise RepositoryFileError(
            f"The dashboard cannot preview this non-text file: {relative.as_posix()}"
        ) from exc
    truncated = len(content) > max_characters
    return RepositoryFile(
        path=resolved,
        relative_path=relative.as_posix(),
        content=content[:max_characters] if truncated else content,
        language=LANGUAGES.get(resolved.suffix.casefold()),
        truncated=truncated,
    )


@st.dialog("Repository file", width="large", icon=":material/description:")
def show_repository_file(file_path: str | Path, *, title: str | None = None) -> None:
    try:
        preview = load_repository_file(file_path)
    except (OSError, RepositoryFileError, ValueError) as exc:
        st.error(str(exc), icon=":material/error:")
        return

    st.markdown(f"### {title or preview.path.name}")
    st.code(preview.relative_path, language=None)
    if preview.truncated:
        st.warning(
            f"The preview is limited to {MAX_PREVIEW_CHARACTERS:,} characters. "
            "Download the file to view the complete contents.",
            icon=":material/warning:",
        )
    st.code(
        preview.content,
        language=preview.language,
        line_numbers=True,
        wrap_lines=False,
        height=480,
    )
    st.download_button(
        "Download file",
        data=preview.path.read_bytes,
        file_name=preview.path.name,
        mime="text/plain",
        icon=":material/download:",
        on_click="ignore",
    )
