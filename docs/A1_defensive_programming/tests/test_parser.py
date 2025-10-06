import pytest

from docs.A1_defensive_programming.exercises import parser as exercise_parser


def test_simple_add():
    assert exercise_parser.parse_and_eval('2+3') == 5


def test_spaces_and_float():
    assert exercise_parser.parse_and_eval(' 4.5  * 2') == 9.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        exercise_parser.parse_and_eval('1/0')


def test_invalid_chars():
    with pytest.raises(ValueError):
        exercise_parser.parse_and_eval('2 + abc')


def test_empty():
    with pytest.raises(ValueError):
        exercise_parser.parse_and_eval('')
