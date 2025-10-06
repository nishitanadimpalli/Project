"""Reference solution for parse_and_eval exercise."""
from typing import Union

Number = Union[int, float]


def parse_and_eval(expr: str) -> float:
    s = expr.strip()
    if not s:
        raise ValueError("empty expression")

    # only allow digits, whitespace, dot, and the operators
    allowed = set("0123456789.+-*/ ")
    if any(ch not in allowed for ch in s):
        raise ValueError("invalid characters in expression")

    # try to find a single operator
    for op in ['+', '-', '*', '/']:
        if op in s:
            parts = s.split(op)
            if len(parts) != 2:
                raise ValueError("invalid expression format")
            left, right = parts
            try:
                a = float(left)
                b = float(right)
            except ValueError:
                raise ValueError("non-numeric operands")

            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
            if op == '/':
                if b == 0:
                    raise ZeroDivisionError("division by zero")
                return a / b

    raise ValueError("no operator found")
