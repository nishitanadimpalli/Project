import pytest

from calculator import add, subtract, multiply, divide


def test_add_simple():
    assert add(2, 3) == 5


def test_subtract_simple():
    assert subtract(5, 3) == 2


def test_multiply_simple():
    assert multiply(4, 3) == 12


def test_divide_simple():
    assert divide(10, 2) == 5


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_numbers_float():
    assert add(0.1, 0.2) == pytest.approx(0.3)
