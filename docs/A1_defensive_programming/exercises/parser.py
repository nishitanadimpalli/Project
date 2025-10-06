"""Exercise: defensive parser for simple arithmetic expressions.

Students: implement `parse_and_eval(expr: str) -> float` which accepts a string
like '2 + 3' or '4*5' and safely parses and evaluates only basic operations
(+ - * /). It must raise ValueError for invalid inputs and ZeroDivisionError
for divides by zero.
"""
from typing import Union

Number = Union[int, float]


def parse_and_eval(expr: str) -> float:
    """Parse a simple expression and return its numeric result.

    This function is defensive: it strips whitespace, rejects unknown
    characters, and only allows one binary operator among +, -, *, /.
    """
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
