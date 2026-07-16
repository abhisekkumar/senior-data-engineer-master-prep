from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any

import streamlit as st

from tracker.database import ROOT
from tracker.roadmap import (
    ROADMAP_ITEM_TYPES,
    ROADMAP_STATUSES,
    RoadmapError,
    active_program,
    archive_phase,
    assign_question_to_module,
    create_item,
    create_module,
    create_phase,
    create_snapshot,
    delete_item,
    export_roadmap_json,
    export_roadmap_markdown,
    filter_roadmap_items,
    find_item,
    find_module,
    find_phase,
    import_roadmap_json,
    list_snapshots,
    maybe_advance_phase,
    move_item,
    move_module,
    move_phase,
    phase_progress,
    program_progress,
    relocate_roadmap,
    restore_snapshot,
    roadmap_path,
    save_roadmap,
    set_active_phase,
    unassigned_questions,
    unresolved_question_links,
    update_item,
    update_item_status,
    update_module,
    update_phase,
)
from tracker.roadmap_models import Module, RoadmapDocument, RoadmapItem


def humanize(value: str) -> str:
    return value.replace("_", " ").replace("-", " ").strip().capitalize()


def _commit(
    document: RoadmapDocument,
    action: Callable[[], Any],
    message: str,
    *,
    destructive: bool = False,
) -> None:
    try:
        action()
        maybe_advance_phase(document)
        save_roadmap(document, destructive=destructive)
    except (RoadmapError, TypeError, ValueError) as exc:
        st.error(str(exc), icon=":material/error:")
        return
    st.toast(message, icon=":material/check_circle:")
    st.rerun()


def _phase_options(document: RoadmapDocument, *, include_archived: bool = True) -> list[Any]:
    phases = sorted(active_program(document).phases, key=lambda phase: phase.order)
    return phases if include_archived else [phase for phase in phases if not phase.archived]


def _module_options(document: RoadmapDocument, phase_id: str | None = None) -> list[Module]:
    modules = [
        module
        for phase in _phase_options(document)
        if phase_id is None or phase.id == phase_id
        for module in sorted(phase.modules, key=lambda value: value.order)
    ]
    return modules


def _question_labels(questions: list[dict[str, Any]]) -> dict[str, str]:
    return {
        question["id"]: f"{question['title']} ({question['id']})" for question in questions
    }


def _resource_labels(resources: list[dict[str, str]]) -> dict[str, str]:
    return {
        resource["file_path"]: f"{resource['title']} — {resource['file_path']}"
        for resource in resources
    }


def _phase_summary(document: RoadmapDocument, questions: list[dict[str, Any]]) -> None:
    program = active_program(document)
    summary = program_progress(document, questions)
    current = (
        find_phase(document, document.settings.active_phase_id)
        if document.settings.active_phase_id
        else None
    )
    st.markdown(f"### :material/route: {program.name}")
    st.caption(program.description)
    columns = st.columns(4)
    columns[0].metric("Current phase", current.short_name if current else "Not selected", border=True)
    columns[1].metric("Overall completion", f"{summary['overall_completion']:.1f}%", border=True)
    columns[2].metric(
        "Interview ready", f"{summary['interview_ready_percentage']:.1f}%", border=True
    )
    columns[3].metric("Mastered", f"{summary['mastered_percentage']:.1f}%", border=True)
    columns = st.columns(3)
    columns[0].metric("Required items", summary["required_items"], border=True)
    columns[1].metric("Overdue linked reviews", summary["overdue_linked_reviews"], border=True)
    columns[2].metric(
        "Unassigned questions", len(unassigned_questions(document, questions)), border=True
    )


def _roadmap_filters(
    document: RoadmapDocument, questions: list[dict[str, Any]]
) -> set[str] | None:
    phases = _phase_options(document)
    with st.container(border=True):
        st.markdown("#### :material/filter_alt: Focus the roadmap")
        first, second, third, fourth = st.columns(4)
        phase_choice = first.selectbox(
            "Phase",
            [None, *[phase.id for phase in phases]],
            format_func=lambda value: "All phases"
            if value is None
            else find_phase(document, value).name,
            key="roadmap-filter-phase",
        )
        modules = _module_options(document, phase_choice)
        module_choice = second.selectbox(
            "Module",
            [None, *[module.id for module in modules]],
            format_func=lambda value: "All modules"
            if value is None
            else find_module(document, value).name,
            key="roadmap-filter-module",
        )
        status_choice = third.selectbox(
            "Status",
            [None, *ROADMAP_STATUSES],
            format_func=lambda value: "All statuses" if value is None else humanize(value),
            key="roadmap-filter-status",
        )
        type_choice = fourth.selectbox(
            "Item type",
            [None, *ROADMAP_ITEM_TYPES],
            format_func=lambda value: "All types" if value is None else humanize(value),
            key="roadmap-filter-type",
        )
        first, second, third, fourth = st.columns(4)
        requirement = first.selectbox(
            "Requirement", ["All", "Required", "Optional"], key="roadmap-filter-required"
        )
        association = second.selectbox(
            "Question link", ["All", "Linked", "Unlinked"], key="roadmap-filter-linked"
        )
        confidence_value = third.selectbox(
            "Linked confidence", ["All", "1", "2", "3", "4", "5"]
        )
        overdue = fourth.checkbox("Overdue linked reviews only")
        query = st.text_input(
            "Search roadmap", placeholder="item, module, phase, note, or keyword"
        )
    filters_active = any(
        [
            phase_choice,
            module_choice,
            status_choice,
            type_choice,
            requirement != "All",
            association != "All",
            confidence_value != "All",
            overdue,
            query.strip(),
        ]
    )
    if not filters_active:
        return None
    matches = filter_roadmap_items(
        document,
        questions,
        phase_id=phase_choice,
        module_id=module_choice,
        status=status_choice,
        item_type=type_choice,
        required={"Required": True, "Optional": False}.get(requirement),
        linked={"Linked": True, "Unlinked": False}.get(association),
        overdue_only=overdue,
        confidence=int(confidence_value) if confidence_value != "All" else None,
        query=query,
    )
    st.caption(f"{len(matches)} roadmap items match the active filters.")
    return {item.id for item in matches}


def _item_card(
    document: RoadmapDocument,
    item: RoadmapItem,
    questions: list[dict[str, Any]],
    unresolved: dict[str, list[str]],
) -> None:
    question_map = {question["id"]: question for question in questions}
    linked = [question_map[qid] for qid in item.linked_question_ids if qid in question_map]
    with st.container(border=True):
        title_column, status_column, save_column = st.columns([4, 2, 1])
        requirement = "Required" if item.required else "Optional"
        title_column.markdown(f"**{item.title}**")
        title_column.caption(f"{humanize(item.item_type)} · {requirement}")
        selected = status_column.selectbox(
            "Roadmap status",
            ROADMAP_STATUSES,
            index=ROADMAP_STATUSES.index(item.status),
            format_func=humanize,
            key=f"roadmap-status-{item.id}",
            label_visibility="collapsed",
        )
        if save_column.button(
            "Save",
            key=f"roadmap-status-save-{item.id}",
            icon=":material/save:",
        ):
            _commit(
                document,
                lambda: update_item_status(document, item.id, selected),
                f"Updated {item.title}.",
            )
        if item.description:
            st.caption(item.description)
        if linked:
            for question in linked:
                columns = st.columns([4, 1])
                columns[0].markdown(
                    f":blue-badge[{question['id']}] :green-badge[Confidence "
                    f"{question.get('confidence', 1)}/5]  \n"
                    f"Last practiced: {question.get('last_practiced') or 'Not yet'} · "
                    f"Next review: {question.get('next_review') or 'Unscheduled'}"
                )
                local_path = ROOT / question["file_path"]
                if local_path.is_file():
                    columns[1].link_button(
                        "Open file", local_path.as_uri(), icon=":material/open_in_new:"
                    )
        if item.id in unresolved:
            st.warning(
                "Unresolved question link: " + ", ".join(unresolved[item.id]),
                icon=":material/link_off:",
            )
        if item.linked_resource_paths:
            valid_resources = [path for path in item.linked_resource_paths if (ROOT / path).is_file()]
            if valid_resources:
                st.caption("Resources: " + " · ".join(valid_resources))
                for index, path in enumerate(valid_resources):
                    st.link_button(
                        f"Open {Path(path).name}",
                        (ROOT / path).as_uri(),
                        key=f"item-resource-{item.id}-{index}",
                        icon=":material/article:",
                    )
        if item.real_world_context:
            st.markdown(f"**Scenario:** {item.real_world_context}")
        if item.completion_criteria:
            st.caption(f"Ready when: {item.completion_criteria}")
        if item.notes:
            st.info(item.notes, icon=":material/note:")
        if st.button(
            "Edit item",
            key=f"open-item-editor-{item.id}",
            icon=":material/edit:",
        ):
            st.session_state["roadmap-item-editor-target"] = item.id
            st.rerun()


def _phase_cards(
    document: RoadmapDocument,
    questions: list[dict[str, Any]],
    visible_item_ids: set[str] | None,
) -> None:
    unresolved = unresolved_question_links(document, questions)
    show_archived = document.settings.show_archived_phases
    phases = [
        phase for phase in _phase_options(document) if show_archived or not phase.archived
    ]
    for phase in phases:
        metrics = phase_progress(phase, questions)
        active = " · Current" if phase.id == document.settings.active_phase_id else ""
        archived = " · Archived" if phase.archived else ""
        with st.expander(
            f"{phase.order}. {phase.name}{active}{archived} — "
            f"{metrics['completion_percentage']:.1f}%",
            expanded=phase.id == document.settings.active_phase_id,
            icon=":material/flag:" if phase.id == document.settings.active_phase_id else ":material/map:",
        ):
            top, edit = st.columns([5, 1])
            top.markdown(phase.objective or phase.description or "No objective added yet.")
            if edit.button(
                "Edit phase", key=f"phase-edit-{phase.id}", icon=":material/edit:"
            ):
                st.session_state["roadmap-phase-editor-target"] = phase.id
                st.rerun()
            st.progress(
                float(metrics["completion_percentage"]) / 100,
                text=(
                    f"{metrics['completed_items']} of {metrics['required_items']} required ready · "
                    f"{metrics['modules_completed']} of {metrics['module_count']} modules ready"
                ),
            )
            metric_columns = st.columns(4)
            metric_columns[0].metric("Interview ready", metrics["interview_ready_count"], border=True)
            metric_columns[1].metric("Mastered", metrics["mastered_count"], border=True)
            metric_columns[2].metric(
                "Required remaining", metrics["remaining_required_items"], border=True
            )
            metric_columns[3].metric(
                "Weak linked", metrics["weak_linked_questions"], border=True
            )
            if not phase.modules:
                st.caption("No modules yet. Add one in Edit curriculum below.")
            for module in sorted(phase.modules, key=lambda value: value.order):
                matching = [
                    item
                    for item in sorted(module.items, key=lambda value: value.order)
                    if visible_item_ids is None or item.id in visible_item_ids
                ]
                if visible_item_ids is not None and not matching:
                    continue
                st.markdown(f"#### {module.order}. {module.name}")
                st.caption(module.description or module.completion_criteria)
                if not matching:
                    st.caption("No roadmap items in this module yet.")
                for item in matching:
                    _item_card(document, item, questions, unresolved)


def _phase_editor(document: RoadmapDocument) -> None:
    st.markdown("#### Phases")
    with st.form("create-roadmap-phase", clear_on_submit=True):
        name = st.text_input("New phase name", placeholder="Phase W — Custom focus")
        short_name = st.text_input("Short name", placeholder="Phase W")
        objective = st.text_area("Objective")
        description = st.text_area("Description")
        if st.form_submit_button("Create phase", icon=":material/add:"):
            _commit(
                document,
                lambda: create_phase(
                    document,
                    name=name,
                    short_name=short_name,
                    objective=objective,
                    description=description,
                ),
                "Phase created.",
            )

    phases = _phase_options(document)
    if not phases:
        st.caption("Create the first phase with the form above.")
        return
    default_id = st.session_state.get("roadmap-phase-editor-target")
    default_index = next(
        (index for index, phase in enumerate(phases) if phase.id == default_id), 0
    )
    phase_id = st.selectbox(
        "Edit phase",
        [phase.id for phase in phases],
        index=default_index,
        format_func=lambda value: find_phase(document, value).name,
        key="roadmap-phase-editor-select",
    )
    phase = find_phase(document, phase_id)
    with st.form(f"edit-roadmap-phase-{phase.id}"):
        name = st.text_input("Phase name", value=phase.name)
        short_name = st.text_input("Phase short name", value=phase.short_name)
        objective = st.text_area("Phase objective", value=phase.objective)
        description = st.text_area("Phase description", value=phase.description)
        first, second = st.columns(2)
        start_date = first.text_input(
            "Target start date (YYYY-MM-DD)", value=phase.target_start_date or ""
        )
        end_date = second.text_input(
            "Target end date (YYYY-MM-DD)", value=phase.target_end_date or ""
        )
        if st.form_submit_button("Save phase", icon=":material/save:"):
            _commit(
                document,
                lambda: update_phase(
                    document,
                    phase.id,
                    name=name,
                    short_name=short_name,
                    objective=objective,
                    description=description,
                    target_start_date=start_date or None,
                    target_end_date=end_date or None,
                ),
                "Phase updated.",
            )
    first, second, third = st.columns(3)
    if first.button("Move phase up", icon=":material/arrow_upward:"):
        _commit(document, lambda: move_phase(document, phase.id, -1), "Phase moved.")
    if second.button("Move phase down", icon=":material/arrow_downward:"):
        _commit(document, lambda: move_phase(document, phase.id, 1), "Phase moved.")
    confirm_archive = third.checkbox(
        "Confirm archive/restore", key=f"confirm-phase-archive-{phase.id}"
    )
    label = "Restore phase" if phase.archived else "Archive phase"
    if st.button(label, icon=":material/archive:" if not phase.archived else ":material/unarchive:"):
        if not confirm_archive:
            st.warning("Confirm this change first.", icon=":material/warning:")
        else:
            _commit(
                document,
                lambda: archive_phase(document, phase.id, archived=not phase.archived),
                f"{label} complete.",
                destructive=True,
            )


def _module_editor(document: RoadmapDocument) -> None:
    st.markdown("#### Modules")
    phases = _phase_options(document, include_archived=False)
    if not phases:
        st.warning("Restore or create an active phase before adding modules.")
        return
    with st.form("create-roadmap-module", clear_on_submit=True):
        phase_id = st.selectbox(
            "Phase for new module",
            [phase.id for phase in phases],
            format_func=lambda value: find_phase(document, value).name,
        )
        name = st.text_input("New module name")
        description = st.text_area("Module description")
        criteria = st.text_area("Module completion criteria")
        if st.form_submit_button("Create module", icon=":material/add:"):
            _commit(
                document,
                lambda: create_module(
                    document,
                    phase_id,
                    name=name,
                    description=description,
                    completion_criteria=criteria,
                ),
                "Module created.",
            )
    modules = _module_options(document)
    if not modules:
        st.caption("Create a module before editing modules or items.")
        return
    module_id = st.selectbox(
        "Edit module",
        [module.id for module in modules],
        format_func=lambda value: (
            f"{find_phase(document, find_module(document, value).phase_id).short_name} — "
            f"{find_module(document, value).name}"
        ),
    )
    module = find_module(document, module_id)
    with st.form(f"edit-roadmap-module-{module.id}"):
        name = st.text_input("Module name", value=module.name)
        description = st.text_area("Description", value=module.description)
        criteria = st.text_area("Completion criteria", value=module.completion_criteria)
        target_phase = st.selectbox(
            "Move to phase",
            [phase.id for phase in phases],
            index=next(
                index for index, phase in enumerate(phases) if phase.id == module.phase_id
            ),
            format_func=lambda value: find_phase(document, value).name,
        )
        if st.form_submit_button("Save module", icon=":material/save:"):
            def save_module() -> None:
                update_module(
                    document,
                    module.id,
                    name=name,
                    description=description,
                    completion_criteria=criteria,
                )
                if target_phase != module.phase_id:
                    move_module(document, module.id, target_phase_id=target_phase)

            _commit(document, save_module, "Module updated.")
    first, second = st.columns(2)
    if first.button("Move module up", icon=":material/arrow_upward:"):
        _commit(
            document,
            lambda: move_module(document, module.id, direction=-1),
            "Module moved.",
        )
    if second.button("Move module down", icon=":material/arrow_downward:"):
        _commit(
            document,
            lambda: move_module(document, module.id, direction=1),
            "Module moved.",
        )


REAL_WORLD_FIELDS = {
    "business_scenario": "Business scenario",
    "input_assumptions": "Input assumptions",
    "constraints": "Constraints",
    "clarifying_questions": "Clarifying questions",
    "brute_force_approach": "Brute-force approach",
    "optimal_local_approach": "Optimal local approach",
    "time_complexity": "Time complexity",
    "space_complexity": "Space complexity",
    "sql_interpretation": "SQL interpretation",
    "spark_interpretation": "Spark/distributed interpretation",
    "data_quality": "Data-quality considerations",
    "reliability": "Reliability considerations",
    "scaling_followups": "Scaling follow-ups",
    "interviewer_followups": "Interviewer follow-ups",
    "canonical_patterns": "Linked canonical patterns",
    "completion_notes": "Completion notes",
}


def _item_fields(
    *,
    prefix: str,
    item: RoadmapItem | None,
    questions: list[dict[str, Any]],
    resources: list[dict[str, str]],
) -> dict[str, Any]:
    question_labels = _question_labels(questions)
    resource_labels = _resource_labels(resources)
    current_questions = item.linked_question_ids if item else []
    current_resources = item.linked_resource_paths if item else []
    question_options = sorted(set(question_labels) | set(current_questions))
    resource_options = sorted(set(resource_labels) | set(current_resources))
    title = st.text_input("Item title", value=item.title if item else "", key=f"{prefix}-title")
    first, second = st.columns(2)
    item_type = first.selectbox(
        "Item type",
        ROADMAP_ITEM_TYPES,
        index=ROADMAP_ITEM_TYPES.index(item.item_type) if item else 0,
        format_func=humanize,
        key=f"{prefix}-type",
    )
    required = second.checkbox(
        "Required item", value=item.required if item else True, key=f"{prefix}-required"
    )
    description = st.text_area(
        "Description", value=item.description if item else "", key=f"{prefix}-description"
    )
    linked_question_ids = st.multiselect(
        "Linked catalog questions",
        question_options,
        default=current_questions,
        format_func=lambda value: question_labels.get(value, f"Missing: {value}"),
        key=f"{prefix}-questions",
    )
    linked_resource_paths = st.multiselect(
        "Linked study resources or exercise files",
        resource_options,
        default=current_resources,
        format_func=lambda value: resource_labels.get(value, f"Missing: {value}"),
        key=f"{prefix}-resources",
    )
    recognition = st.text_area(
        "Recognition clues (one per line)",
        value="\n".join(item.recognition_clues) if item else "",
        key=f"{prefix}-clues",
    )
    context = st.text_area(
        "Real-world context", value=item.real_world_context if item else "", key=f"{prefix}-context"
    )
    criteria = st.text_area(
        "Completion criteria",
        value=item.completion_criteria if item else "",
        key=f"{prefix}-criteria",
    )
    notes = st.text_area("Notes", value=item.notes if item else "", key=f"{prefix}-notes")
    details: dict[str, str] = {}
    with st.expander("Real-world problem details (optional)"):
        st.caption(
            "Use any fields that help this draft. The full reusable template is under docs/."
        )
        columns = st.columns(2)
        for index, (field_name, label) in enumerate(REAL_WORLD_FIELDS.items()):
            with columns[index % 2]:
                details[field_name] = st.text_area(
                    label,
                    value=item.real_world_details.get(field_name, "") if item else "",
                    key=f"{prefix}-real-world-{field_name}",
                )
    return {
        "title": title,
        "item_type": item_type,
        "required": required,
        "description": description,
        "linked_question_ids": linked_question_ids,
        "linked_resource_paths": linked_resource_paths,
        "recognition_clues": [value.strip() for value in recognition.splitlines() if value.strip()],
        "real_world_context": context,
        "real_world_details": {key: value for key, value in details.items() if value.strip()},
        "completion_criteria": criteria,
        "notes": notes,
    }


def _item_editor(
    document: RoadmapDocument,
    questions: list[dict[str, Any]],
    resources: list[dict[str, str]],
) -> None:
    st.markdown("#### Roadmap items")
    modules = _module_options(document)
    if not modules:
        st.caption("Create a module before adding roadmap items.")
        return
    with st.form("create-roadmap-item", clear_on_submit=False):
        module_id = st.selectbox(
            "Module for new item",
            [module.id for module in modules],
            format_func=lambda value: find_module(document, value).name,
            key="create-item-module",
        )
        values = _item_fields(
            prefix="create-item", item=None, questions=questions, resources=resources
        )
        if st.form_submit_button("Create roadmap item", icon=":material/add:"):
            _commit(
                document,
                lambda: create_item(document, module_id, **values),
                "Roadmap item created.",
            )

    items = [item for module in modules for item in sorted(module.items, key=lambda value: value.order)]
    if not items:
        return
    default_id = st.session_state.get("roadmap-item-editor-target")
    default_index = next((index for index, item in enumerate(items) if item.id == default_id), 0)
    item_id = st.selectbox(
        "Edit roadmap item",
        [item.id for item in items],
        index=default_index,
        format_func=lambda value: find_item(document, value).title,
        key="roadmap-item-editor-select",
    )
    item = find_item(document, item_id)
    with st.form(f"edit-roadmap-item-{item.id}"):
        target_module_id = st.selectbox(
            "Move item to module",
            [module.id for module in modules],
            index=next(index for index, module in enumerate(modules) if module.id == item.module_id),
            format_func=lambda value: find_module(document, value).name,
            key=f"edit-item-target-{item.id}",
        )
        values = _item_fields(
            prefix=f"edit-item-{item.id}",
            item=item,
            questions=questions,
            resources=resources,
        )
        if st.form_submit_button("Save roadmap item", icon=":material/save:"):
            def save_item() -> None:
                update_item(document, item.id, **values)
                if target_module_id != item.module_id:
                    move_item(document, item.id, target_module_id=target_module_id)

            _commit(document, save_item, "Roadmap item updated.")
    first, second = st.columns(2)
    if first.button("Move item up", icon=":material/arrow_upward:"):
        _commit(document, lambda: move_item(document, item.id, direction=-1), "Item moved.")
    if second.button("Move item down", icon=":material/arrow_downward:"):
        _commit(document, lambda: move_item(document, item.id, direction=1), "Item moved.")
    confirm_delete = st.checkbox(
        "I understand this removes only the roadmap item, not linked question history.",
        key=f"confirm-delete-item-{item.id}",
    )
    if st.button("Delete roadmap item", icon=":material/delete:", type="secondary"):
        _commit(
            document,
            lambda: delete_item(document, item.id, confirmed=confirm_delete),
            "Roadmap item deleted. Question history was preserved.",
            destructive=True,
        )


def _unassigned_editor(
    document: RoadmapDocument, questions: list[dict[str, Any]]
) -> None:
    unassigned = unassigned_questions(document, questions)
    with st.expander(
        f"Unassigned questions — {len(unassigned)}",
        icon=":material/playlist_add:",
    ):
        st.caption(
            "New catalog discoveries stay unassigned until you choose a module. Assignment never "
            "duplicates or changes the question record."
        )
        if not unassigned:
            st.success("Every catalog question is linked to the roadmap.")
            return
        modules = _module_options(document)
        if not modules:
            st.warning("Create a module before assigning questions.")
            return
        labels = _question_labels(unassigned)
        with st.form("assign-unassigned-question"):
            question_id = st.selectbox(
                "Question",
                [question["id"] for question in unassigned],
                format_func=lambda value: labels[value],
            )
            module_id = st.selectbox(
                "Destination module",
                [module.id for module in modules],
                format_func=lambda value: (
                    f"{find_phase(document, find_module(document, value).phase_id).short_name} — "
                    f"{find_module(document, value).name}"
                ),
            )
            if st.form_submit_button("Assign question", icon=":material/link:"):
                question = next(value for value in unassigned if value["id"] == question_id)
                _commit(
                    document,
                    lambda: assign_question_to_module(document, module_id, question),
                    "Question assigned to the roadmap.",
                )


def render_roadmap(data: dict[str, Any]) -> None:
    document: RoadmapDocument = data["roadmap"]
    questions = data["questions"]
    st.subheader(":material/route: Preparation Roadmap")
    st.caption(
        "Track interview readiness separately from catalog completion and confidence. "
        "Everything here is editable and saved locally."
    )
    _phase_summary(document, questions)
    unresolved = unresolved_question_links(document, questions)
    if unresolved:
        st.warning(
            f"{sum(map(len, unresolved.values()))} linked question references are unresolved. "
            "The roadmap items were preserved for repair in the editor.",
            icon=":material/link_off:",
        )
    visible_item_ids = _roadmap_filters(document, questions)
    _phase_cards(document, questions, visible_item_ids)
    _unassigned_editor(document, questions)
    with st.expander("Edit curriculum", icon=":material/edit_note:"):
        st.caption(
            "Changes take effect immediately. Archive and delete operations create a local snapshot."
        )
        phase_tab, module_tab, item_tab = st.tabs(["Phases", "Modules", "Items"])
        with phase_tab:
            _phase_editor(document)
        with module_tab:
            _module_editor(document)
        with item_tab:
            _item_editor(document, questions, data["resources"])


def render_settings(data: dict[str, Any]) -> None:
    document: RoadmapDocument = data["roadmap"]
    st.subheader(":material/settings: Settings")
    st.caption("Choose the current focus and manage local roadmap versions.")

    with st.container(border=True):
        st.markdown("#### Active study focus")
        selected_program_id = st.selectbox(
            "Active program",
            [program.id for program in document.programs],
            index=next(
                (
                    index
                    for index, program in enumerate(document.programs)
                    if program.id == document.settings.active_program_id
                ),
                0,
            ),
            format_func=lambda value: next(
                program.name for program in document.programs if program.id == value
            ),
        )
        selected_program = next(
            program for program in document.programs if program.id == selected_program_id
        )
        selectable_phases = sorted(
            (phase for phase in selected_program.phases if not phase.archived),
            key=lambda phase: phase.order,
        )
        phases = selectable_phases or sorted(
            selected_program.phases, key=lambda phase: phase.order
        )
        if not selectable_phases:
            st.warning(
                "Every phase is archived. Restore a phase from Roadmap → Edit curriculum before "
                "saving a new active focus.",
                icon=":material/archive:",
            )
        selected_phase_id = st.selectbox(
            "Active phase",
            [phase.id for phase in phases],
            index=next(
                (
                    index
                    for index, phase in enumerate(phases)
                    if phase.id == document.settings.active_phase_id
                ),
                0,
            ),
            format_func=lambda value: find_phase(document, value).name,
        )
        modules = _module_options(document, selected_phase_id) if selected_phase_id else []
        selected_module_id = st.selectbox(
            "Active module",
            [None, *[module.id for module in modules]],
            index=next(
                (
                    index + 1
                    for index, module in enumerate(modules)
                    if module.id == document.settings.active_module_id
                ),
                0,
            ),
            format_func=lambda value: "No active module"
            if value is None
            else find_module(document, value).name,
        )
        first, second = st.columns(2)
        automatic = first.toggle(
            "Automatic phase advancement", value=document.settings.automatic_advancement
        )
        manual = second.toggle("Manual phase mode", value=document.settings.manual_phase_mode)
        default_status = st.selectbox(
            "Default roadmap status after successful independent completion",
            ROADMAP_STATUSES,
            index=ROADMAP_STATUSES.index(document.settings.default_success_status),
            format_func=humanize,
        )
        show_archived = st.checkbox(
            "Show archived phases", value=document.settings.show_archived_phases
        )
        override = st.checkbox(
            "Explicitly allow switching before all required items are interview ready"
        )
        if st.button(
            "Save study focus",
            icon=":material/save:",
            type="primary",
            disabled=not selectable_phases,
        ):
            def save_focus() -> None:
                document.settings.active_program_id = selected_program_id
                for candidate in document.programs:
                    candidate.active = candidate.id == selected_program_id
                set_active_phase(
                    document,
                    selected_phase_id,
                    module_id=selected_module_id,
                    override=override,
                )
                document.settings.automatic_advancement = automatic
                document.settings.manual_phase_mode = manual
                document.settings.default_success_status = default_status
                document.settings.show_archived_phases = show_archived

            _commit(document, save_focus, "Roadmap settings saved.")

    with st.container(border=True):
        st.markdown("#### Local data and versions")
        st.caption(f"Current roadmap file: `{roadmap_path()}`")
        local_directory = st.text_input(
            "Local-data directory", value=document.settings.local_data_directory
        )
        if st.button("Move roadmap storage", icon=":material/drive_file_move:"):
            try:
                destination = relocate_roadmap(document, local_directory)
            except (RoadmapError, OSError, ValueError) as exc:
                st.error(str(exc), icon=":material/error:")
            else:
                st.success(f"Roadmap is now stored at {destination}.")
                st.rerun()

        json_export = export_roadmap_json(document)
        markdown_export = export_roadmap_markdown(document)
        first, second = st.columns(2)
        first.download_button(
            "Export roadmap JSON",
            data=json_export,
            file_name="preparation-roadmap.json",
            mime="application/json",
            icon=":material/download:",
        )
        second.download_button(
            "Export readable Markdown",
            data=markdown_export,
            file_name="preparation-roadmap.md",
            mime="text/markdown",
            icon=":material/download:",
        )
        uploaded = st.file_uploader("Import roadmap JSON", type=["json"])
        confirm_import = st.checkbox(
            "Validate, snapshot, and replace the current roadmap with this import"
        )
        if st.button("Import roadmap", icon=":material/upload:"):
            if uploaded is None or not confirm_import:
                st.warning("Choose a JSON file and confirm the import first.")
            else:
                try:
                    import_roadmap_json(uploaded.getvalue())
                except (RoadmapError, OSError, ValueError) as exc:
                    st.error(str(exc), icon=":material/error:")
                else:
                    st.success("Roadmap imported and the previous version was snapshotted.")
                    st.rerun()

        if st.button("Create roadmap snapshot", icon=":material/backup:"):
            try:
                snapshot = create_snapshot()
            except (RoadmapError, OSError) as exc:
                st.error(str(exc), icon=":material/error:")
            else:
                st.success(f"Created {snapshot.name}.")
                st.rerun()
        snapshots = list_snapshots()
        if snapshots:
            selected_snapshot = st.selectbox(
                "Restore snapshot",
                snapshots,
                format_func=lambda value: value.name,
            )
            confirm_restore = st.checkbox("Confirm snapshot restore")
            if st.button("Restore selected snapshot", icon=":material/restore:"):
                if not confirm_restore:
                    st.warning("Confirm the restore first.")
                else:
                    try:
                        restore_snapshot(selected_snapshot)
                    except (RoadmapError, OSError, ValueError) as exc:
                        st.error(str(exc), icon=":material/error:")
                    else:
                        st.success("Roadmap restored. The replaced version was also snapshotted.")
                        st.rerun()
        else:
            st.caption("No roadmap snapshots yet.")
