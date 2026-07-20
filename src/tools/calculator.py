from langchain_core.tools import tool
from sympy import SympifyError
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

# Supports:
# 2pi -> 2*pi
# 2^10 -> 2**10
TRANSFORMATIONS = (
    standard_transformations
    + (
        implicit_multiplication_application,
        convert_xor,
    )
)


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.

    Supported examples:
    - 2 + 3 * 5
    - (10 + 2) / 4
    - sqrt(25)
    - sin(pi/2)
    - cos(pi)
    - tan(pi/4)
    - log(100, 10)
    - ln(E)
    - factorial(6)
    - 2^10
    - 2pi
    """

    try:
        expr = parse_expr(
            expression,
            transformations=TRANSFORMATIONS,
            evaluate=True,
        )

        result = expr.evalf()

        if result.is_Integer:
            return str(int(result))

        if result == int(result):
            return str(int(result))

        return str(result)

    except (SympifyError, SyntaxError, TypeError, ValueError):
        return "Invalid mathematical expression."

    except Exception as e:
        return f"Calculation error: {e}"