from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any

ROADMAP_STATUSES = (
    "not_started",
    "learning",
    "practicing",
    "interview_ready",
    "mastered",
    "skipped",
)
ROADMAP_ITEM_TYPES = (
    "coding_question",
    "coding_review",
    "python_fundamentals",
    "sql_question",
    "spark_question",
    "data_engineering",
    "system_design",
    "behavioral",
    "genai",
    "real_world_problem",
    "mock_interview",
    "documentation",
    "custom",
)


def timestamp() -> str:
    return datetime.now().isoformat(timespec="seconds")


def _require_text(value: str, label: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")


def _validate_timestamp(value: str | None, label: str) -> None:
    if value:
        try:
            datetime.fromisoformat(value)
        except ValueError as exc:
            raise ValueError(f"{label} must be an ISO date or datetime") from exc


@dataclass(slots=True)
class RoadmapItem:
    id: str
    module_id: str
    title: str
    item_type: str
    order: int
    description: str = ""
    status: str = "not_started"
    required: bool = True
    confidence: int | None = None
    linked_question_ids: list[str] = field(default_factory=list)
    linked_resource_paths: list[str] = field(default_factory=list)
    recognition_clues: list[str] = field(default_factory=list)
    real_world_context: str = ""
    real_world_details: dict[str, str] = field(default_factory=dict)
    completion_criteria: str = ""
    notes: str = ""
    started_at: str | None = None
    completed_at: str | None = None
    last_practiced: str | None = None
    next_review: str | None = None
    created_at: str = field(default_factory=timestamp)
    updated_at: str = field(default_factory=timestamp)

    def __post_init__(self) -> None:
        _require_text(self.id, "roadmap item id")
        _require_text(self.module_id, "roadmap item module_id")
        _require_text(self.title, "roadmap item title")
        if self.item_type not in ROADMAP_ITEM_TYPES:
            raise ValueError(f"invalid roadmap item type: {self.item_type}")
        if self.status not in ROADMAP_STATUSES:
            raise ValueError(f"invalid roadmap item status: {self.status}")
        if not isinstance(self.order, int) or self.order < 1:
            raise ValueError("roadmap item order must be a positive integer")
        if self.confidence is not None and self.confidence not in range(1, 6):
            raise ValueError("roadmap item confidence must be between 1 and 5")
        for values, label in (
            (self.linked_question_ids, "linked_question_ids"),
            (self.linked_resource_paths, "linked_resource_paths"),
            (self.recognition_clues, "recognition_clues"),
        ):
            if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
                raise ValueError(f"{label} must be a list of strings")
        if not isinstance(self.real_world_details, dict) or not all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in self.real_world_details.items()
        ):
            raise ValueError("real_world_details must map strings to strings")
        for value, label in (
            (self.started_at, "started_at"),
            (self.completed_at, "completed_at"),
            (self.last_practiced, "last_practiced"),
            (self.next_review, "next_review"),
            (self.created_at, "created_at"),
            (self.updated_at, "updated_at"),
        ):
            _validate_timestamp(value, label)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RoadmapItem:
        return cls(**data)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class Module:
    id: str
    phase_id: str
    name: str
    order: int
    description: str = ""
    completion_criteria: str = ""
    items: list[RoadmapItem] = field(default_factory=list)
    created_at: str = field(default_factory=timestamp)
    updated_at: str = field(default_factory=timestamp)

    def __post_init__(self) -> None:
        _require_text(self.id, "module id")
        _require_text(self.phase_id, "module phase_id")
        _require_text(self.name, "module name")
        if not isinstance(self.order, int) or self.order < 1:
            raise ValueError("module order must be a positive integer")
        self.items = [
            item if isinstance(item, RoadmapItem) else RoadmapItem.from_dict(item)
            for item in self.items
        ]
        if any(item.module_id != self.id for item in self.items):
            raise ValueError(f"module {self.id} contains an item with a different module_id")
        _validate_timestamp(self.created_at, "created_at")
        _validate_timestamp(self.updated_at, "updated_at")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Module:
        return cls(**data)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class Phase:
    id: str
    name: str
    short_name: str
    order: int
    description: str = ""
    objective: str = ""
    status: str = "not_started"
    active: bool = False
    archived: bool = False
    target_start_date: str | None = None
    target_end_date: str | None = None
    completion_percentage: float = 0.0
    modules: list[Module] = field(default_factory=list)
    created_at: str = field(default_factory=timestamp)
    updated_at: str = field(default_factory=timestamp)

    def __post_init__(self) -> None:
        _require_text(self.id, "phase id")
        _require_text(self.name, "phase name")
        _require_text(self.short_name, "phase short_name")
        if not isinstance(self.order, int) or self.order < 1:
            raise ValueError("phase order must be a positive integer")
        if self.status not in ROADMAP_STATUSES:
            raise ValueError(f"invalid phase status: {self.status}")
        if not 0 <= self.completion_percentage <= 100:
            raise ValueError("phase completion_percentage must be between 0 and 100")
        self.modules = [
            module if isinstance(module, Module) else Module.from_dict(module)
            for module in self.modules
        ]
        if any(module.phase_id != self.id for module in self.modules):
            raise ValueError(f"phase {self.id} contains a module with a different phase_id")
        for value, label in (
            (self.target_start_date, "target_start_date"),
            (self.target_end_date, "target_end_date"),
            (self.created_at, "created_at"),
            (self.updated_at, "updated_at"),
        ):
            _validate_timestamp(value, label)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Phase:
        return cls(**data)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class Program:
    id: str
    name: str
    description: str = ""
    active: bool = True
    phases: list[Phase] = field(default_factory=list)
    created_at: str = field(default_factory=timestamp)
    updated_at: str = field(default_factory=timestamp)

    def __post_init__(self) -> None:
        _require_text(self.id, "program id")
        _require_text(self.name, "program name")
        self.phases = [
            phase if isinstance(phase, Phase) else Phase.from_dict(phase)
            for phase in self.phases
        ]
        _validate_timestamp(self.created_at, "created_at")
        _validate_timestamp(self.updated_at, "updated_at")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Program:
        return cls(**data)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class RoadmapSettings:
    active_program_id: str = "senior-data-engineering-master-prep"
    active_phase_id: str | None = "phase-a"
    active_module_id: str | None = "phase-a-duplicate-detection"
    automatic_advancement: bool = False
    manual_phase_mode: bool = True
    default_success_status: str = "interview_ready"
    show_archived_phases: bool = False
    local_data_directory: str = ".local"

    def __post_init__(self) -> None:
        _require_text(self.active_program_id, "active_program_id")
        if self.default_success_status not in ROADMAP_STATUSES:
            raise ValueError("invalid default_success_status")
        _require_text(self.local_data_directory, "local_data_directory")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RoadmapSettings:
        return cls(**data)


@dataclass(slots=True)
class RoadmapDocument:
    schema_version: int = 1
    programs: list[Program] = field(default_factory=list)
    settings: RoadmapSettings = field(default_factory=RoadmapSettings)
    created_at: str = field(default_factory=timestamp)
    updated_at: str = field(default_factory=timestamp)

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise ValueError(f"unsupported roadmap schema_version: {self.schema_version}")
        self.programs = [
            program if isinstance(program, Program) else Program.from_dict(program)
            for program in self.programs
        ]
        if not isinstance(self.settings, RoadmapSettings):
            self.settings = RoadmapSettings.from_dict(self.settings)
        _validate_timestamp(self.created_at, "created_at")
        _validate_timestamp(self.updated_at, "updated_at")
        self._validate_identity_graph()

    def _validate_identity_graph(self) -> None:
        ids: set[str] = set()
        phase_ids: set[str] = set()
        module_ids: set[str] = set()
        module_phase_ids: dict[str, str] = {}
        for program in self.programs:
            for entity_id in [program.id]:
                if entity_id in ids:
                    raise ValueError(f"duplicate roadmap id: {entity_id}")
                ids.add(entity_id)
            if len({phase.order for phase in program.phases}) != len(program.phases):
                raise ValueError(f"program {program.id} contains duplicate phase orders")
            for phase in program.phases:
                if phase.id in ids:
                    raise ValueError(f"duplicate roadmap id: {phase.id}")
                ids.add(phase.id)
                phase_ids.add(phase.id)
                if len({module.order for module in phase.modules}) != len(phase.modules):
                    raise ValueError(f"phase {phase.id} contains duplicate module orders")
                for module in phase.modules:
                    if module.id in ids:
                        raise ValueError(f"duplicate roadmap id: {module.id}")
                    ids.add(module.id)
                    module_ids.add(module.id)
                    module_phase_ids[module.id] = phase.id
                    if len({item.order for item in module.items}) != len(module.items):
                        raise ValueError(f"module {module.id} contains duplicate item orders")
                    for item in module.items:
                        if item.id in ids:
                            raise ValueError(f"duplicate roadmap id: {item.id}")
                        ids.add(item.id)
        if self.programs and not any(
            program.id == self.settings.active_program_id for program in self.programs
        ):
            raise ValueError("active_program_id does not reference a program")
        if (
            self.programs
            and self.settings.active_phase_id is not None
            and self.settings.active_phase_id not in phase_ids
        ):
            raise ValueError("active_phase_id does not reference a phase")
        if self.programs and self.settings.active_module_id is not None:
            if self.settings.active_module_id not in module_ids:
                raise ValueError("active_module_id does not reference a module")
            if (
                self.settings.active_phase_id
                and module_phase_ids[self.settings.active_module_id]
                != self.settings.active_phase_id
            ):
                raise ValueError("active_module_id does not belong to active_phase_id")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RoadmapDocument:
        if not isinstance(data, dict):
            raise ValueError("roadmap data must be a JSON object")
        try:
            return cls(**data)
        except TypeError as exc:
            raise ValueError(f"invalid roadmap fields: {exc}") from exc

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
