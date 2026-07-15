import pytest

from tracker.database import load_questions
from tracker.models import Question


def test_catalog_models_are_valid() -> None:
    questions = [Question.from_dict(item) for item in load_questions()]
    assert len(questions) == 80
    assert len({item.id for item in questions}) == len(questions)


def test_invalid_confidence_is_rejected() -> None:
    raw = load_questions()[0] | {"confidence": 6}
    with pytest.raises(ValueError):
        Question.from_dict(raw)
