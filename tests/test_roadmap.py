import copy
import json
from pathlib import Path

import pytest

from tracker.roadmap import (
    RoadmapError,
    archive_phase,
    assign_question_to_module,
    create_item,
    create_module,
    create_phase,
    create_snapshot,
    delete_item,
    export_roadmap_json,
    export_roadmap_markdown,
    import_roadmap_json,
    list_snapshots,
    load_roadmap,
    move_item,
    move_module,
    move_phase,
    phase_progress,
    restore_snapshot,
    save_roadmap,
    seed_roadmap,
    unassigned_questions,
    unresolved_question_links,
    update_item,
    update_item_status,
    update_module,
    update_phase,
)
from tracker.roadmap_models import RoadmapDocument, RoadmapItem


def test_roadmap_model_validation_rejects_invalid_values() -> None:
    with pytest.raises(ValueError, match="invalid roadmap item status"):
        RoadmapItem(
            id="item-1",
            module_id="module-1",
            title="Invalid",
            item_type="custom",
            order=1,
            status="done",
        )
    with pytest.raises(ValueError, match="invalid roadmap item type"):
        RoadmapItem(
            id="item-1",
            module_id="module-1",
            title="Invalid",
            item_type="project",
            order=1,
        )


def test_loading_missing_roadmap_can_return_empty_document(tmp_path: Path) -> None:
    document = load_roadmap(tmp_path / "roadmap.json", seed_if_missing=False)
    assert isinstance(document, RoadmapDocument)
    assert document.programs == []


def test_loading_missing_roadmap_seeds_once_without_overwrite(tmp_path: Path) -> None:
    path = tmp_path / "roadmap.json"
    document = load_roadmap(path, seed_question_ids=["leetcode-0001", "leetcode-0217"])
    assert len(document.programs[0].phases) == 22
    assert document.programs[0].phases[0].modules
    assert "leetcode-0001" in {
        question_id
        for module in document.programs[0].phases[0].modules
        for item in module.items
        for question_id in item.linked_question_ids
    }
    document.programs[0].name = "My edited roadmap"
    save_roadmap(document, path)
    loaded = load_roadmap(path, seed_question_ids=[])
    assert loaded.programs[0].name == "My edited roadmap"


def test_atomic_save_leaves_only_valid_destination(tmp_path: Path) -> None:
    path = tmp_path / "roadmap.json"
    save_roadmap(seed_roadmap(), path)
    assert json.loads(path.read_text(encoding="utf-8"))["schema_version"] == 1
    assert not list(tmp_path.glob(".roadmap.json.*"))


def test_phase_crud_reorder_archive_and_restore() -> None:
    document = seed_roadmap()
    created = create_phase(
        document,
        name="Phase W — Custom",
        short_name="Phase W",
        objective="Practice a custom topic.",
    )
    update_phase(document, created.id, name="Phase W — Edited", description="Edited")
    move_phase(document, created.id, -1)
    assert created.name == "Phase W — Edited"
    assert created.order == 22
    archive_phase(document, created.id)
    assert created.archived
    archive_phase(document, created.id, archived=False)
    assert not created.archived


def test_module_and_item_crud_and_moves() -> None:
    document = seed_roadmap()
    phase_a = document.programs[0].phases[0]
    phase_b = document.programs[0].phases[1]
    module = create_module(
        document,
        phase_b.id,
        name="Custom module",
        completion_criteria="Explain it.",
    )
    update_module(document, module.id, name="Edited module")
    move_module(document, module.id, target_phase_id=phase_a.id)
    assert module.phase_id == phase_a.id
    assert module.name == "Edited module"

    item = create_item(
        document,
        module.id,
        title="Custom item",
        item_type="custom",
        notes="Draft",
    )
    update_item(document, item.id, title="Edited item", required=False)
    move_item(document, item.id, direction=-1)
    update_item_status(document, item.id, "practicing")
    assert item.title == "Edited item"
    assert item.status == "practicing"
    assert item.started_at
    delete_item(document, item.id, confirmed=True)
    assert item not in module.items


def test_delete_item_requires_confirmation() -> None:
    document = seed_roadmap()
    item = document.programs[0].phases[0].modules[0].items[0]
    with pytest.raises(RoadmapError, match="requires confirmation"):
        delete_item(document, item.id, confirmed=False)


def test_question_association_unassigned_and_missing_links() -> None:
    document = seed_roadmap(["leetcode-0001"])
    questions = [
        {"id": "leetcode-0001", "title": "Two Sum", "source": "leetcode", "confidence": 3},
        {"id": "custom-new", "title": "New exercise", "source": "custom", "confidence": 1},
    ]
    original_questions = copy.deepcopy(questions)
    assert [question["id"] for question in unassigned_questions(document, questions)] == [
        "custom-new"
    ]
    module_id = document.programs[0].phases[0].modules[0].id
    assigned = assign_question_to_module(document, module_id, questions[1])
    assert assigned.linked_question_ids == ["custom-new"]
    assigned.linked_question_ids.append("removed-question")
    assert unresolved_question_links(document, questions)[assigned.id] == ["removed-question"]
    assert questions == original_questions


def test_phase_progress_weights_optional_and_skipped_items() -> None:
    document = seed_roadmap()
    phase = document.programs[0].phases[0]
    for module in phase.modules:
        module.items.clear()
    module = phase.modules[0]
    required = create_item(document, module.id, title="Required", item_type="custom")
    optional = create_item(
        document, module.id, title="Optional", item_type="custom", required=False
    )
    skipped = create_item(document, module.id, title="Skipped", item_type="custom")
    update_item_status(document, required.id, "practicing")
    update_item_status(document, optional.id, "mastered")
    update_item_status(document, skipped.id, "skipped")
    metrics = phase_progress(phase)
    assert metrics["required_items"] == 1
    assert metrics["completion_percentage"] == 50.0
    assert metrics["mastered_percentage"] == 0.0


def test_export_import_snapshots_and_restore(tmp_path: Path) -> None:
    path = tmp_path / "roadmap.json"
    document = seed_roadmap(["leetcode-0001"])
    save_roadmap(document, path)
    snapshot = create_snapshot(path)
    assert snapshot in list_snapshots(path)
    document.programs[0].name = "Changed"
    save_roadmap(document, path)
    restored = restore_snapshot(snapshot, path)
    assert restored.programs[0].name == "Senior Data Engineering Master Prep"

    exported = export_roadmap_json(restored)
    assert "Senior Data Engineering Master Prep" in exported
    assert "# Preparation Roadmap" in export_roadmap_markdown(restored)
    imported = import_roadmap_json(exported, path)
    assert imported.schema_version == 1


def test_invalid_json_and_invalid_import_do_not_overwrite(tmp_path: Path) -> None:
    path = tmp_path / "roadmap.json"
    path.write_text("{invalid", encoding="utf-8")
    with pytest.raises(RoadmapError, match="Invalid JSON"):
        load_roadmap(path)

    save_roadmap(seed_roadmap(), path)
    original = path.read_text(encoding="utf-8")
    with pytest.raises(RoadmapError, match="failed validation"):
        import_roadmap_json('{"schema_version": 99}', path)
    assert path.read_text(encoding="utf-8") == original
