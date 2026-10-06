import pytest

from evaluate import evaluate


@pytest.mark.parametrize("expression, expected", [
    # Examples 
    ("1 + 3", 4),
    ("1 + 3 * 2", 8),
    ("(4 / 2) + 6", 8),
    ("4 + (12 / (1 * 2))", 10),
    # Left to right, no precedence
    ("1 + 3 * 4", 16),
    ("2 * 3 + 4", 10),
    ("10 - 2 - 3", 5),
    ("100 / 10 / 5", 2),
    # Brackets 
    ("1 + (3 * 4)", 13),
    ("(1 + 2) * (3 + 4)", 21),
    ("((7))", 7),
    # Whitespaces
    (" 1 + 3 ", 4),
    ("1+3", 4),
    ("\t(1\n+ 3)*2 ", 8),
    
    # Signed numbers
    ("-5 + 3", -2),
    ("+5", 5),
    ("3 - -2", 5),
    ("(-4 + 1) * 2", -6),
    
    ("7 / 2", 3),
    ("-7 / 2", -3),
    ("7 / -2", -3),
    ("-7 / -2", 3),

    ("0 + 0", 0),
    ("0 * 5 + 1", 1),
])
def test_valid_expressions(expression, expected):
    assert evaluate(expression) == expected


@pytest.mark.parametrize("expression", [
    # Empty / incomplete
    "", " ", "()", "1 +", "* 3", "1 + * 2", "-", "(",
    # Unbalanced brackets
    "(1 + (12 * 2)", "1 + 2)", ")",
    # Two operands with no operator between them
    "1 2", "(1)(2)", "1 (2)",
    # Division by zero
    "1 / 0", "5 / (3 - 3)",
    # Sign rules: must touch the digits; no sign in front of a bracket
    "- 5", "-(1 + 2)",
    # Characters not supported
    "1.5 + 2", "1 + a", "2 ^ 3", "\u0663 + 1",
])
def test_errors_return_none(expression):
    assert evaluate(expression) is None


@pytest.mark.parametrize("value", [None, 123, 1.5, ["1+2"]])
def test_non_string_returns_none(value):
    assert evaluate(value) is None
