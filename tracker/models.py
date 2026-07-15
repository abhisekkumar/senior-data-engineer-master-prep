from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
from typing import Any


@dataclass(slots=True)
class Question:
    id: str
    title: str
    category: str
    primary_pattern: str
    difficulty: str
    file_path: str
    source: str = "leetcode"
    leetcode_number: int | None = None
    slug: str = ""
    secondary_patterns: list[str] = field(default_factory=list)
    phase: str = "Phase A"
    status: str = "not_started"
    confidence: int = 1
    attempts: int = 0
    completed_without_help: bool = False
    last_practiced: str | None = None
    next_review: str | None = None
    average_minutes: float = 0
    best_minutes: int | None = None
    mistake_tags: list[str] = field(default_factory=list)
    notes: str = ""
    created_at: str = field(default_factory=lambda: date.today().isoformat())
    updated_at: str = field(default_factory=lambda: date.today().isoformat())

    def __post_init__(self) -> None:
        if not 1 <= self.confidence <= 5:
            raise ValueError("confidence must be between 1 and 5")
        if self.difficulty not in {"easy", "medium", "hard"}:
            raise ValueError("difficulty must be easy, medium, or hard")
        for value in (self.last_practiced, self.next_review, self.created_at, self.updated_at):
            if value:
                date.fromisoformat(value)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Question:
        return cls(**data)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
