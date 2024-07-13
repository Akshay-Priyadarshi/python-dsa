from stack.implementation import Stack


def is_parenthesis_balanced(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    checker = Stack[str](len(s))
    mappings = {"]": "[", ")": "(", "}": "{"}
    if len(s) == 0:
        return False
    for ch in s:
        try:
            last_ch_in_checker = checker.peek()
        except Exception:
            last_ch_in_checker = None
        if last_ch_in_checker == mappings.get(ch) is not None:
            checker.pop()
        else:
            checker.push(ch)
    if checker.is_empty():
        return True
    return False
