"""Calculator core functions.

This module provides a tiny set of functions with clear behavior and simple
error handling so students can extend and write tests around them.
"""
from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """Return a minus b."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b."""
    return a * b

def divide(a: Number, b: Number) -> Number:
    """Return a divided by b.

    Raises:
        ZeroDivisionError: if b == 0
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
