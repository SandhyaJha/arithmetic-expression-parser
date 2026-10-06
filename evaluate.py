from typing import Optional

OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: int(a/b),

}


def skip(s: str, pos: int) ->int:
    while pos < len(s) and s[pos].isspace():
        pos += 1
    return pos

def operand(s: str, pos: int):
    pos = skip(s, pos)
    if s[pos: pos+1] =="(":
        value, pos = expr(s, pos+1)
        pos = skip(s, pos)
        if value is None or s[pos: pos+1] != ")":
            return None, pos
        return value, pos+1
    start = pos
    if s[pos:pos+1] in ("+", "-"):
        pos += 1
    digits = pos
    while pos <len(s) and s[pos] in "0123456789":
        pos += 1
    return (int(s[start:pos]) if pos > digits else None ), pos

def expr(s: str, pos:int):
    value, pos = operand(s, pos)
    while value is not None:
        pos = skip(s, pos)
        op = s[pos: pos+1]
        if op not in OPERATIONS:
            break
        right, pos = operand(s, pos +1)
        value = None if right is None else OPERATIONS[op](value, right)
    return value, pos 
        
        
def evaluate(expression: str) -> Optional[int]:
    """Returns the result, or None if there was an error."""
    if not isinstance(expression, str):
        return None
    try:
        result, pos = expr(expression, 0)
        return result if skip(expression, pos) == len(expression) else None
    except :
        return None