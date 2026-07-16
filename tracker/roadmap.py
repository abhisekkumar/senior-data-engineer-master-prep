from __future__ import annotations

import json
import re
import shutil
from collections.abc import Iterable
from datetime import date, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

from tracker.database import ROOT, atomic_write_json
from tracker.roadmap_models import (
    ROADMAP_ITEM_TYPES,
    ROADMAP_STATUSES,
    Module,
    Phase,
    Program,
    RoadmapDocument,
    RoadmapItem,
    RoadmapSettings,
    timestamp,
)

DEFAULT_LOCAL_DIRECTORY = ".local"
ROADMAP_LOCATION_PATH = ROOT / ".local/roadmap_location.json"
STATUS_WEIGHTS = {
    "not_started": 0.0,
    "learning": 0.25,
    "practicing": 0.50,
    "interview_ready": 0.85,
    "mastered": 1.0,
}
READY_STATUSES = {"interview_ready", "mastered"}


class RoadmapError(ValueError):
    """A friendly validation or roadmap-operation error."""


def _safe_directory(directory: str | Path) -> Path:
    value = Path(directory).expanduser()
    return value if value.is_absolute() else ROOT / value


def current_local_directory() -> Path:
    if not ROADMAP_LOCATION_PATH.exists():
        return ROOT / DEFAULT_LOCAL_DIRECTORY
    try:
        value = json.loads(ROADMAP_LOCATION_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RoadmapError(f"Invalid roadmap location file: {exc}") from exc
    directory = value.get("directory") if isinstance(value, dict) else None
    if not isinstance(directory, str) or not directory.strip():
        raise RoadmapError("Roadmap location file must contain a non-empty directory")
    return _safe_directory(directory)


def roadmap_path() -> Path:
    return current_local_directory() / "roadmap.json"


def history_directory(path: Path | None = None) -> Path:
    base = (path or roadmap_path()).parent
    return base / "history/roadmap"


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return slug or "roadmap"


def stable_new_id(prefix: str, title: str) -> str:
    return f"{prefix}-{_slug(title)[:40]}-{uuid4().hex[:8]}"


def _phase_names() -> list[tuple[str, str, str]]:
    return [
        ("A", "Arrays and Hashing", "Build fast lookup, set, frequency, and grouping instincts."),
        ("B", "Two Pointers and Sorted Data", "Reason about ordered data with bounded state."),
        ("C", "Sliding Window and Time Windows", "Recognize fixed and variable window problems."),
        ("D", "Prefix Sum and Cumulative Analysis", "Use cumulative state for range analysis."),
        ("E", "Intervals and Scheduling", "Model overlap, merging, availability, and scheduling."),
        ("F", "Binary Search and Search on Answer", "Apply boundary invariants and monotonic search."),
        ("G", "Stack and Monotonic Structures", "Use stacks for nested and next-greater relationships."),
        ("H", "Heaps and Top-K Processing", "Select and stream ranked elements efficiently."),
        ("I", "Linked Lists and Streaming Pointers", "Manipulate pointer state and streaming cursors."),
        ("J", "Trees and Hierarchical Data", "Traverse and reason about hierarchical structures."),
        ("K", "Graphs, DAGs, and Data Lineage", "Model dependencies, reachability, and lineage."),
        ("L", "Greedy and Optimization", "Identify safe local choices and defend correctness."),
        ("M", "Dynamic Programming", "Define state, transitions, and reusable subproblems."),
        ("N", "Python Language Mastery", "Communicate Python semantics and write reliable code."),
        ("O", "Advanced SQL", "Solve analytical, reconciliation, and data-quality SQL."),
        ("P", "Spark and Distributed Processing", "Reason about partitions, shuffles, skew, and scale."),
        ("Q", "Data Engineering Architecture", "Design reliable batch and streaming data platforms."),
        ("R", "System Design", "Clarify requirements and defend scalable design trade-offs."),
        ("S", "GenAI and LLM Systems", "Design and evaluate responsible data-aware LLM systems."),
        ("T", "Behavioral and Resume Stories", "Deliver concise, evidence-based senior-level stories."),
        ("U", "Real-World Data Engineering Problems", "Translate patterns into production constraints."),
        ("V", "Mixed Mock Interviews", "Practice complete interview loops under realistic timing."),
    ]


def _seed_item(
    module_id: str,
    order: int,
    title: str,
    item_type: str,
    *,
    question_id: str | None = None,
    available_question_ids: set[str],
    required: bool = True,
    context: str = "",
    criteria: str = "",
    resources: list[str] | None = None,
) -> RoadmapItem:
    linked = [question_id] if question_id and question_id in available_question_ids else []
    return RoadmapItem(
        id=f"{module_id}-item-{order:02d}",
        module_id=module_id,
        title=title,
        item_type=item_type,
        order=order,
        linked_question_ids=linked,
        linked_resource_paths=resources or [],
        required=required,
        real_world_context=context,
        completion_criteria=criteria,
    )


def _phase_a_modules(available_question_ids: set[str]) -> list[Module]:
    definitions: list[tuple[str, str, str, list[dict[str, Any]]]] = [
        (
            "duplicate-detection",
            "Duplicate detection and sets",
            "Recognize membership, uniqueness, and cycle-detection problems.",
            [
                {"title": "Contains Duplicate", "type": "coding_question", "qid": "leetcode-0217"},
                {
                    "title": "Find the Difference of Two Arrays",
                    "type": "coding_question",
                    "qid": "leetcode-2215",
                },
                {"title": "Happy Number", "type": "coding_question", "qid": "leetcode-0202"},
                {
                    "title": "Detect duplicate member IDs before a warehouse load",
                    "type": "real_world_problem",
                    "context": "Reject or quarantine repeated synthetic business keys before loading curated tables.",
                },
                {
                    "title": "Deduplicate retry events using event IDs",
                    "type": "real_world_problem",
                    "context": "Design idempotent event processing without using real production identifiers.",
                },
            ],
        ),
        (
            "hash-map-lookup",
            "Hash-map lookup",
            "Use complement and state lookup while explaining memory trade-offs.",
            [
                {"title": "Two Sum", "type": "coding_question", "qid": "leetcode-0001"},
                {
                    "title": "Match two transactions to a target reconciliation amount",
                    "type": "real_world_problem",
                    "context": "Match synthetic debit and credit amounts while preserving duplicate records.",
                },
            ],
        ),
        (
            "frequency-counting",
            "Frequency counting",
            "Build counts, rank results, and explain deterministic tie handling.",
            [
                {"title": "Valid Anagram", "type": "coding_question", "qid": "leetcode-0242"},
                {
                    "title": "Top K Frequent Elements",
                    "type": "coding_question",
                    "qid": "leetcode-0347",
                },
            ],
        ),
        (
            "grouping-normalization",
            "Grouping and normalization",
            "Create canonical keys and group equivalent records.",
            [
                {"title": "Group Anagrams", "type": "coding_question", "qid": "leetcode-0049"},
                {
                    "title": "Group normalized customer identifiers",
                    "type": "real_world_problem",
                    "context": "Normalize and group synthetic identifiers with explicit collision rules.",
                },
            ],
        ),
        (
            "sequence-detection",
            "Sequence detection",
            "Use set membership to find starts and extend consecutive runs.",
            [
                {
                    "title": "Longest Consecutive Sequence",
                    "type": "coding_question",
                    "qid": "leetcode-0128",
                },
                {
                    "title": "Find the longest consecutive sequence of loaded partitions",
                    "type": "real_world_problem",
                    "context": "Detect the longest gap-free run of synthetic partition dates.",
                },
            ],
        ),
        (
            "production-extensions",
            "Real-world production extensions",
            "Compare local, SQL, distributed, and probabilistic implementations.",
            [
                {
                    "title": "Explain duplicate detection when data does not fit in memory",
                    "type": "real_world_problem",
                    "context": "Compare bounded-memory options and their correctness guarantees.",
                },
                {"title": "Implement SQL duplicate-key detection", "type": "sql_question"},
                {"title": "Implement Spark distributed deduplication", "type": "spark_question"},
                {
                    "title": "Compare sets, external sorting, and Bloom filters",
                    "type": "real_world_problem",
                    "context": "Explain memory, I/O, false-positive, and exactness trade-offs.",
                },
            ],
        ),
    ]
    modules: list[Module] = []
    for module_order, (slug, name, description, item_defs) in enumerate(definitions, start=1):
        module_id = f"phase-a-{slug}"
        items = [
            _seed_item(
                module_id,
                item_order,
                definition["title"],
                definition["type"],
                question_id=definition.get("qid"),
                available_question_ids=available_question_ids,
                context=definition.get("context", ""),
                criteria="Explain the approach, trade-offs, complexity, and production follow-ups.",
                resources=(
                    ["docs/REAL_WORLD_PROBLEM_TEMPLATE.md"]
                    if definition["type"] == "real_world_problem"
                    else []
                ),
            )
            for item_order, definition in enumerate(item_defs, start=1)
        ]
        modules.append(
            Module(
                id=module_id,
                phase_id="phase-a",
                name=name,
                description=description,
                order=module_order,
                completion_criteria="All required items are at least interview ready.",
                items=items,
            )
        )
    return modules


def seed_roadmap(question_ids: Iterable[str] = ()) -> RoadmapDocument:
    available = set(question_ids)
    phases = [
        Phase(
            id=f"phase-{letter.casefold()}",
            name=f"Phase {letter} — {name}",
            short_name=f"Phase {letter}",
            description=objective,
            objective=objective,
            order=order,
            active=letter == "A",
            modules=_phase_a_modules(available) if letter == "A" else [],
        )
        for order, (letter, name, objective) in enumerate(_phase_names(), start=1)
    ]
    return RoadmapDocument(
        programs=[
            Program(
                id="senior-data-engineering-master-prep",
                name="Senior Data Engineering Master Prep",
                description="An editable, local-first curriculum for senior data engineering interviews.",
                phases=phases,
            )
        ],
        settings=RoadmapSettings(),
    )


def load_roadmap(
    path: Path | None = None,
    *,
    seed_question_ids: Iterable[str] = (),
    seed_if_missing: bool = True,
) -> RoadmapDocument:
    target = path or roadmap_path()
    if not target.exists():
        if not seed_if_missing:
            return RoadmapDocument(programs=[], settings=RoadmapSettings())
        document = seed_roadmap(seed_question_ids)
        save_roadmap(document, target)
        return document
    try:
        raw = json.loads(target.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RoadmapError(f"Invalid JSON in {target}: {exc}") from exc
    try:
        return RoadmapDocument.from_dict(raw)
    except (TypeError, ValueError) as exc:
        raise RoadmapError(f"Roadmap validation failed for {target}: {exc}") from exc


def create_snapshot(path: Path | None = None) -> Path:
    target = path or roadmap_path()
    if not target.exists():
        raise RoadmapError(f"Cannot snapshot missing roadmap: {target}")
    destination = history_directory(target) / (
        f"roadmap-{datetime.now().strftime('%Y%m%d-%H%M%S-%f')}.json"
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(target, destination)
    return destination


def save_roadmap(
    document: RoadmapDocument,
    path: Path | None = None,
    *,
    destructive: bool = False,
) -> None:
    target = path or roadmap_path()
    refresh_completion(document)
    document.updated_at = timestamp()
    try:
        validated = RoadmapDocument.from_dict(document.to_dict())
    except (TypeError, ValueError) as exc:
        raise RoadmapError(f"Roadmap validation failed before save: {exc}") from exc
    if destructive and target.exists():
        create_snapshot(target)
    atomic_write_json(target, validated.to_dict())


def relocate_roadmap(document: RoadmapDocument, directory: str) -> Path:
    destination_dir = _safe_directory(directory)
    destination = destination_dir / "roadmap.json"
    current = roadmap_path()
    if destination.resolve() != current.resolve() and destination.exists():
        raise RoadmapError(f"Refusing to overwrite an existing roadmap at {destination}")
    if current.exists():
        create_snapshot(current)
    document.settings.local_data_directory = directory
    save_roadmap(document, destination)
    atomic_write_json(ROADMAP_LOCATION_PATH, {"directory": directory})
    return destination


def list_snapshots(path: Path | None = None) -> list[Path]:
    directory = history_directory(path)
    return sorted(directory.glob("roadmap-*.json"), reverse=True) if directory.exists() else []


def restore_snapshot(snapshot: Path, path: Path | None = None) -> RoadmapDocument:
    target = path or roadmap_path()
    if snapshot not in list_snapshots(target):
        raise RoadmapError("Selected roadmap snapshot is not in the local snapshot directory")
    restored = load_roadmap(snapshot, seed_if_missing=False)
    if target.exists():
        create_snapshot(target)
    save_roadmap(restored, target)
    return restored


def import_roadmap_json(raw: str | bytes, path: Path | None = None) -> RoadmapDocument:
    try:
        decoded = raw.decode("utf-8") if isinstance(raw, bytes) else raw
        value = json.loads(decoded)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RoadmapError(f"Roadmap import is not valid UTF-8 JSON: {exc}") from exc
    try:
        document = RoadmapDocument.from_dict(value)
    except (TypeError, ValueError) as exc:
        raise RoadmapError(f"Roadmap import failed validation: {exc}") from exc
    if not document.programs:
        raise RoadmapError("Roadmap import must contain at least one program")
    save_roadmap(document, path, destructive=True)
    return document


def export_roadmap_json(document: RoadmapDocument) -> str:
    return json.dumps(document.to_dict(), indent=2) + "\n"


def export_roadmap_markdown(document: RoadmapDocument) -> str:
    lines = ["# Preparation Roadmap", ""]
    for program in document.programs:
        lines.extend([f"## {program.name}", "", program.description, ""])
        for phase in sorted(program.phases, key=lambda value: value.order):
            metrics = phase_progress(phase)
            archived = " (archived)" if phase.archived else ""
            lines.extend(
                [
                    f"### {phase.order}. {phase.name}{archived}",
                    "",
                    phase.objective,
                    "",
                    f"Progress: **{metrics['completion_percentage']:.1f}%**",
                    "",
                ]
            )
            for module in sorted(phase.modules, key=lambda value: value.order):
                lines.extend([f"#### {module.name}", ""])
                for item in sorted(module.items, key=lambda value: value.order):
                    marker = "x" if item.status in READY_STATUSES else " "
                    optional = " (optional)" if not item.required else ""
                    links = (
                        f" — questions: {', '.join(item.linked_question_ids)}"
                        if item.linked_question_ids
                        else ""
                    )
                    lines.append(
                        f"- [{marker}] {item.title}{optional} — {item.status}{links}"
                    )
                lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def active_program(document: RoadmapDocument) -> Program:
    program = next(
        (
            value
            for value in document.programs
            if value.id == document.settings.active_program_id
        ),
        None,
    )
    if program is None:
        raise RoadmapError("The active roadmap program is missing")
    return program


def find_phase(document: RoadmapDocument, phase_id: str) -> Phase:
    for program in document.programs:
        for phase in program.phases:
            if phase.id == phase_id:
                return phase
    raise RoadmapError(f"Unknown phase id: {phase_id}")


def find_module(document: RoadmapDocument, module_id: str) -> Module:
    for program in document.programs:
        for phase in program.phases:
            for module in phase.modules:
                if module.id == module_id:
                    return module
    raise RoadmapError(f"Unknown module id: {module_id}")


def find_item(document: RoadmapDocument, item_id: str) -> RoadmapItem:
    for module in iter_modules(document):
        for item in module.items:
            if item.id == item_id:
                return item
    raise RoadmapError(f"Unknown roadmap item id: {item_id}")


def iter_modules(document: RoadmapDocument) -> Iterable[Module]:
    for program in document.programs:
        for phase in program.phases:
            yield from phase.modules


def iter_items(document: RoadmapDocument) -> Iterable[RoadmapItem]:
    for module in iter_modules(document):
        yield from module.items


def _normalize_order(values: list[Any]) -> None:
    values.sort(key=lambda value: value.order)
    _renumber(values)


def _renumber(values: list[Any]) -> None:
    for order, value in enumerate(values, start=1):
        value.order = order


def create_phase(
    document: RoadmapDocument,
    *,
    name: str,
    short_name: str,
    description: str = "",
    objective: str = "",
) -> Phase:
    program = active_program(document)
    phase = Phase(
        id=stable_new_id("phase", name),
        name=name,
        short_name=short_name,
        description=description,
        objective=objective,
        order=len(program.phases) + 1,
    )
    program.phases.append(phase)
    program.updated_at = timestamp()
    return phase


def update_phase(document: RoadmapDocument, phase_id: str, **changes: Any) -> Phase:
    phase = find_phase(document, phase_id)
    allowed = {
        "name",
        "short_name",
        "description",
        "objective",
        "target_start_date",
        "target_end_date",
    }
    unknown = set(changes) - allowed
    if unknown:
        raise RoadmapError(f"Unsupported phase fields: {', '.join(sorted(unknown))}")
    for key, value in changes.items():
        setattr(phase, key, value)
    phase.updated_at = timestamp()
    Phase.from_dict(phase.to_dict())
    return phase


def move_phase(document: RoadmapDocument, phase_id: str, direction: int) -> None:
    if direction not in {-1, 1}:
        raise RoadmapError("phase direction must be -1 or 1")
    phases = active_program(document).phases
    _normalize_order(phases)
    index = next((index for index, phase in enumerate(phases) if phase.id == phase_id), None)
    if index is None:
        raise RoadmapError(f"Unknown phase id: {phase_id}")
    destination = index + direction
    if 0 <= destination < len(phases):
        phases[index], phases[destination] = phases[destination], phases[index]
        _renumber(phases)


def archive_phase(document: RoadmapDocument, phase_id: str, archived: bool = True) -> None:
    phase = find_phase(document, phase_id)
    phase.archived = archived
    phase.active = False if archived else phase.active
    phase.updated_at = timestamp()
    if archived and document.settings.active_phase_id == phase_id:
        replacement = next(
            (candidate for candidate in active_program(document).phases if not candidate.archived),
            None,
        )
        document.settings.active_phase_id = replacement.id if replacement else None
        document.settings.active_module_id = (
            replacement.modules[0].id if replacement and replacement.modules else None
        )
        for candidate in active_program(document).phases:
            candidate.active = replacement is not None and candidate.id == replacement.id


def create_module(
    document: RoadmapDocument,
    phase_id: str,
    *,
    name: str,
    description: str = "",
    completion_criteria: str = "",
) -> Module:
    phase = find_phase(document, phase_id)
    module = Module(
        id=stable_new_id("module", name),
        phase_id=phase_id,
        name=name,
        description=description,
        completion_criteria=completion_criteria,
        order=len(phase.modules) + 1,
    )
    phase.modules.append(module)
    phase.updated_at = timestamp()
    return module


def update_module(document: RoadmapDocument, module_id: str, **changes: Any) -> Module:
    module = find_module(document, module_id)
    allowed = {"name", "description", "completion_criteria"}
    unknown = set(changes) - allowed
    if unknown:
        raise RoadmapError(f"Unsupported module fields: {', '.join(sorted(unknown))}")
    for key, value in changes.items():
        setattr(module, key, value)
    module.updated_at = timestamp()
    Module.from_dict(module.to_dict())
    return module


def move_module(
    document: RoadmapDocument,
    module_id: str,
    *,
    direction: int | None = None,
    target_phase_id: str | None = None,
) -> None:
    module = find_module(document, module_id)
    source_phase = find_phase(document, module.phase_id)
    if target_phase_id and target_phase_id != source_phase.id:
        target_phase = find_phase(document, target_phase_id)
        source_phase.modules.remove(module)
        module.phase_id = target_phase.id
        module.order = len(target_phase.modules) + 1
        for item in module.items:
            item.module_id = module.id
        target_phase.modules.append(module)
        _normalize_order(source_phase.modules)
        return
    if direction not in {-1, 1}:
        raise RoadmapError("module direction must be -1 or 1")
    _normalize_order(source_phase.modules)
    index = source_phase.modules.index(module)
    destination = index + direction
    if 0 <= destination < len(source_phase.modules):
        source_phase.modules[index], source_phase.modules[destination] = (
            source_phase.modules[destination],
            source_phase.modules[index],
        )
        _renumber(source_phase.modules)


def create_item(
    document: RoadmapDocument,
    module_id: str,
    *,
    title: str,
    item_type: str,
    **values: Any,
) -> RoadmapItem:
    module = find_module(document, module_id)
    item = RoadmapItem(
        id=stable_new_id("item", title),
        module_id=module_id,
        title=title,
        item_type=item_type,
        order=len(module.items) + 1,
        **values,
    )
    module.items.append(item)
    module.updated_at = timestamp()
    return item


def update_item(document: RoadmapDocument, item_id: str, **changes: Any) -> RoadmapItem:
    item = find_item(document, item_id)
    allowed = {
        "title",
        "item_type",
        "description",
        "required",
        "confidence",
        "linked_question_ids",
        "linked_resource_paths",
        "recognition_clues",
        "real_world_context",
        "real_world_details",
        "completion_criteria",
        "notes",
        "last_practiced",
        "next_review",
    }
    unknown = set(changes) - allowed
    if unknown:
        raise RoadmapError(f"Unsupported roadmap item fields: {', '.join(sorted(unknown))}")
    for key, value in changes.items():
        setattr(item, key, value)
    item.updated_at = timestamp()
    RoadmapItem.from_dict(item.to_dict())
    return item


def move_item(
    document: RoadmapDocument,
    item_id: str,
    *,
    direction: int | None = None,
    target_module_id: str | None = None,
) -> None:
    item = find_item(document, item_id)
    source = find_module(document, item.module_id)
    if target_module_id and target_module_id != source.id:
        target = find_module(document, target_module_id)
        source.items.remove(item)
        item.module_id = target.id
        item.order = len(target.items) + 1
        target.items.append(item)
        _normalize_order(source.items)
        return
    if direction not in {-1, 1}:
        raise RoadmapError("item direction must be -1 or 1")
    _normalize_order(source.items)
    index = source.items.index(item)
    destination = index + direction
    if 0 <= destination < len(source.items):
        source.items[index], source.items[destination] = (
            source.items[destination],
            source.items[index],
        )
        _renumber(source.items)


def delete_item(document: RoadmapDocument, item_id: str, *, confirmed: bool) -> None:
    if not confirmed:
        raise RoadmapError("Item deletion requires confirmation")
    item = find_item(document, item_id)
    module = find_module(document, item.module_id)
    module.items.remove(item)
    _normalize_order(module.items)


def update_item_status(document: RoadmapDocument, item_id: str, status: str) -> RoadmapItem:
    if status not in ROADMAP_STATUSES:
        raise RoadmapError(f"Invalid roadmap status: {status}")
    item = find_item(document, item_id)
    now = timestamp()
    if status != "not_started" and item.started_at is None:
        item.started_at = now
    item.completed_at = now if status in READY_STATUSES else None
    item.status = status
    item.updated_at = now
    refresh_completion(document)
    return item


def assign_question_to_module(
    document: RoadmapDocument,
    module_id: str,
    question: dict[str, Any],
) -> RoadmapItem:
    question_id = question.get("id")
    if not question_id:
        raise RoadmapError("Question must have a stable id")
    existing = next(
        (item for item in iter_items(document) if question_id in item.linked_question_ids),
        None,
    )
    if existing:
        return existing
    return create_item(
        document,
        module_id,
        title=question.get("title", question_id),
        item_type="coding_question" if question.get("source") != "sql" else "sql_question",
        linked_question_ids=[question_id],
        confidence=question.get("confidence"),
    )


def unresolved_question_links(
    document: RoadmapDocument, questions: list[dict[str, Any]]
) -> dict[str, list[str]]:
    available = {question["id"] for question in questions}
    return {
        item.id: [question_id for question_id in item.linked_question_ids if question_id not in available]
        for item in iter_items(document)
        if any(question_id not in available for question_id in item.linked_question_ids)
    }


def unassigned_questions(
    document: RoadmapDocument, questions: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    assigned = {
        question_id for item in iter_items(document) for question_id in item.linked_question_ids
    }
    return [question for question in questions if question["id"] not in assigned]


def phase_progress(
    phase: Phase,
    questions: list[dict[str, Any]] | None = None,
    *,
    target: date | None = None,
) -> dict[str, int | float]:
    items = [item for module in phase.modules for item in module.items]
    required = [item for item in items if item.required and item.status != "skipped"]
    completed = [item for item in required if item.status in READY_STATUSES]
    readiness = [item for item in required if item.status in READY_STATUSES]
    mastered = [item for item in required if item.status == "mastered"]
    completion = (
        sum(STATUS_WEIGHTS[item.status] for item in required) / len(required) * 100
        if required
        else 0.0
    )
    modules_completed = sum(
        bool(module.items)
        and all(
            item.status in READY_STATUSES or not item.required or item.status == "skipped"
            for item in module.items
        )
        for module in phase.modules
    )
    question_map = {question["id"]: question for question in questions or []}
    linked_map = {
        question_id: question_map[question_id]
        for item in items
        for question_id in item.linked_question_ids
        if question_id in question_map
    }
    linked = list(linked_map.values())
    today = target or date.today()
    overdue = sum(
        bool(question.get("next_review"))
        and date.fromisoformat(question["next_review"]) < today
        for question in linked
    )
    return {
        "completed_items": len(completed),
        "required_items": len(required),
        "remaining_required_items": len(required) - len(completed),
        "completion_percentage": round(completion, 1),
        "modules_completed": modules_completed,
        "module_count": len(phase.modules),
        "interview_ready_count": len(readiness),
        "interview_ready_percentage": round(len(readiness) / len(required) * 100, 1)
        if required
        else 0.0,
        "mastered_count": len(mastered),
        "mastered_percentage": round(len(mastered) / len(required) * 100, 1)
        if required
        else 0.0,
        "weak_linked_questions": len(
            {question["id"] for question in linked if question.get("confidence", 1) <= 2}
        ),
        "overdue_linked_reviews": overdue,
    }


def program_progress(
    document: RoadmapDocument, questions: list[dict[str, Any]] | None = None
) -> dict[str, int | float]:
    program = active_program(document)
    visible = [phase for phase in program.phases if not phase.archived]
    items = [item for phase in visible for module in phase.modules for item in module.items]
    required = [item for item in items if item.required and item.status != "skipped"]
    weighted = sum(STATUS_WEIGHTS[item.status] for item in required)
    question_map = {question["id"]: question for question in questions or []}
    linked_map = {
        question_id: question_map[question_id]
        for item in items
        for question_id in item.linked_question_ids
        if question_id in question_map
    }
    linked = list(linked_map.values())
    return {
        "overall_completion": round(weighted / len(required) * 100, 1) if required else 0.0,
        "interview_ready_percentage": round(
            sum(item.status in READY_STATUSES for item in required) / len(required) * 100, 1
        )
        if required
        else 0.0,
        "mastered_percentage": round(
            sum(item.status == "mastered" for item in required) / len(required) * 100, 1
        )
        if required
        else 0.0,
        "required_items": len(required),
        "overdue_linked_reviews": sum(
            bool(question.get("next_review"))
            and date.fromisoformat(question["next_review"]) < date.today()
            for question in linked
        ),
    }


def refresh_completion(document: RoadmapDocument) -> None:
    for program in document.programs:
        for phase in program.phases:
            phase.completion_percentage = float(phase_progress(phase)["completion_percentage"])
            required = [
                item
                for module in phase.modules
                for item in module.items
                if item.required and item.status != "skipped"
            ]
            if required and all(item.status == "mastered" for item in required):
                phase.status = "mastered"
            elif required and all(item.status in READY_STATUSES for item in required):
                phase.status = "interview_ready"
            elif any(item.status == "practicing" for item in required):
                phase.status = "practicing"
            elif any(item.status == "learning" for item in required):
                phase.status = "learning"
            else:
                phase.status = "not_started"


def phase_is_interview_ready(phase: Phase) -> bool:
    required = [
        item
        for module in phase.modules
        for item in module.items
        if item.required and item.status != "skipped"
    ]
    return bool(required) and all(item.status in READY_STATUSES for item in required)


def set_active_phase(
    document: RoadmapDocument,
    phase_id: str,
    *,
    module_id: str | None = None,
    override: bool = False,
) -> None:
    phase = find_phase(document, phase_id)
    if phase.archived:
        raise RoadmapError("An archived phase cannot be active")
    current_id = document.settings.active_phase_id
    if current_id and current_id != phase_id and not override:
        current = find_phase(document, current_id)
        if not phase_is_interview_ready(current):
            raise RoadmapError(
                "The current phase still has required items below interview ready. "
                "Use the explicit override to advance manually."
            )
    for candidate in active_program(document).phases:
        candidate.active = candidate.id == phase_id
    document.settings.active_phase_id = phase_id
    if module_id:
        module = find_module(document, module_id)
        if module.phase_id != phase_id:
            raise RoadmapError("The active module must belong to the active phase")
        document.settings.active_module_id = module_id
    else:
        document.settings.active_module_id = phase.modules[0].id if phase.modules else None


def maybe_advance_phase(document: RoadmapDocument) -> bool:
    settings = document.settings
    if not settings.automatic_advancement or settings.manual_phase_mode:
        return False
    if not settings.active_phase_id:
        return False
    program = active_program(document)
    phases = sorted((phase for phase in program.phases if not phase.archived), key=lambda p: p.order)
    current = find_phase(document, settings.active_phase_id)
    if not phase_is_interview_ready(current):
        return False
    index = phases.index(current)
    if index + 1 >= len(phases):
        return False
    set_active_phase(document, phases[index + 1].id, override=True)
    return True


def filter_roadmap_items(
    document: RoadmapDocument,
    questions: list[dict[str, Any]],
    *,
    phase_id: str | None = None,
    module_id: str | None = None,
    status: str | None = None,
    item_type: str | None = None,
    required: bool | None = None,
    linked: bool | None = None,
    overdue_only: bool = False,
    confidence: int | None = None,
    query: str = "",
) -> list[RoadmapItem]:
    question_map = {question["id"]: question for question in questions}
    query = query.casefold().strip()
    results: list[RoadmapItem] = []
    for program in document.programs:
        for phase in program.phases:
            if phase_id and phase.id != phase_id:
                continue
            for module in phase.modules:
                if module_id and module.id != module_id:
                    continue
                for item in module.items:
                    linked_questions = [
                        question_map[qid]
                        for qid in item.linked_question_ids
                        if qid in question_map
                    ]
                    is_overdue = any(
                        question.get("next_review")
                        and date.fromisoformat(question["next_review"]) < date.today()
                        for question in linked_questions
                    )
                    linked_confidences = [
                        question.get("confidence") for question in linked_questions
                    ]
                    if status and item.status != status:
                        continue
                    if item_type and item.item_type != item_type:
                        continue
                    if required is not None and item.required != required:
                        continue
                    if linked is not None and bool(item.linked_question_ids) != linked:
                        continue
                    if overdue_only and not is_overdue:
                        continue
                    if confidence is not None and confidence not in linked_confidences:
                        continue
                    if query and query not in " ".join(
                        [item.title, item.description, item.notes, module.name, phase.name]
                    ).casefold():
                        continue
                    results.append(item)
    return results


def roadmap_daily_slots(
    document: RoadmapDocument,
    questions: list[dict[str, Any]],
    target: date,
) -> dict[int, dict[str, Any]]:
    if not document.programs or not document.settings.active_phase_id:
        return {}
    phase = find_phase(document, document.settings.active_phase_id)
    question_map = {question["id"]: question for question in questions}
    modules = sorted(phase.modules, key=lambda module: module.order)
    if document.settings.active_module_id:
        modules.sort(key=lambda module: module.id != document.settings.active_module_id)
    items = [item for module in modules for item in sorted(module.items, key=lambda item: item.order)]
    all_items = [
        item
        for candidate_phase in sorted(
            active_program(document).phases,
            key=lambda value: (value.id != phase.id, value.order),
        )
        if not candidate_phase.archived
        for module in sorted(candidate_phase.modules, key=lambda value: value.order)
        for item in sorted(module.items, key=lambda value: value.order)
    ]
    used: set[str] = set()

    def choose(predicate: Any, candidates: list[RoadmapItem] = items) -> RoadmapItem | None:
        candidate = next(
            (item for item in candidates if item.id not in used and predicate(item)), None
        )
        if candidate:
            used.add(candidate.id)
        return candidate

    overdue = choose(
        lambda item: any(
            (question := question_map.get(question_id))
            and question.get("next_review")
            and date.fromisoformat(question["next_review"]) < target
            for question_id in item.linked_question_ids
        ),
        all_items,
    )
    coding_review = choose(
        lambda item: item.item_type in {"coding_question", "coding_review"}
        and bool(item.linked_question_ids)
        and any(
            question_map.get(question_id, {}).get("status") == "completed"
            for question_id in item.linked_question_ids
        )
    )
    learning = choose(
        lambda item: item.status in {"not_started", "learning", "practicing"}
        and item.item_type in {"coding_question", "coding_review"}
    )
    technical = choose(
        lambda item: item.status not in READY_STATUSES | {"skipped"}
        and item.item_type
        in {
            "sql_question",
            "python_fundamentals",
            "spark_question",
            "data_engineering",
            "system_design",
            "documentation",
        }
    )
    communication = choose(
        lambda item: item.status not in READY_STATUSES | {"skipped"}
        and item.item_type
        in {"real_world_problem", "behavioral", "genai", "mock_interview", "custom"}
    )
    selected = {1: overdue, 2: coding_review, 3: learning, 4: technical, 5: communication}
    slots: dict[int, dict[str, Any]] = {}
    for position, item in selected.items():
        if item is None:
            continue
        question_id = next(
            (qid for qid in item.linked_question_ids if qid in question_map), None
        )
        slots[position] = {
            "position": position,
            "type": item.item_type,
            "roadmap_item_id": item.id,
            "roadmap_status": item.status,
            "question_id": question_id,
            "topic": item.title,
            "area": item.item_type,
        }
    return slots


__all__ = [
    "ROADMAP_ITEM_TYPES",
    "ROADMAP_STATUSES",
    "RoadmapError",
    "archive_phase",
    "assign_question_to_module",
    "create_item",
    "create_module",
    "create_phase",
    "create_snapshot",
    "delete_item",
    "export_roadmap_json",
    "export_roadmap_markdown",
    "filter_roadmap_items",
    "find_item",
    "find_module",
    "find_phase",
    "import_roadmap_json",
    "list_snapshots",
    "load_roadmap",
    "maybe_advance_phase",
    "move_item",
    "move_module",
    "move_phase",
    "phase_progress",
    "program_progress",
    "relocate_roadmap",
    "restore_snapshot",
    "roadmap_daily_slots",
    "roadmap_path",
    "save_roadmap",
    "seed_roadmap",
    "set_active_phase",
    "unassigned_questions",
    "unresolved_question_links",
    "update_item",
    "update_item_status",
    "update_module",
    "update_phase",
]
