from streamlit.testing.v1 import AppTest


def roadmap_app() -> None:
    from dashboard.roadmap_ui import render_roadmap
    from tracker.roadmap import seed_roadmap

    render_roadmap(
        {
            "roadmap": seed_roadmap(),
            "questions": [],
            "resources": [],
        }
    )


def test_module_card_edit_button_selects_that_module() -> None:
    app = AppTest.from_function(roadmap_app).run()
    assert not app.exception

    module_b_button = app.button(key="module-edit-module-b-two-pointers-sorted-data")
    module_b_button.click().run()

    assert not app.exception
    assert (
        app.selectbox(key="roadmap-module-editor-select").value
        == "module-b-two-pointers-sorted-data"
    )
    assert "Edit module" in [button.label for button in app.button]
