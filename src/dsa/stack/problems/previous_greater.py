from src.helpers.custom_typevars import NumberType
from stack.implementation import Stack


def previous_greater(arr: list[NumberType]) -> list[NumberType]:
    s = Stack[NumberType](size=len(arr))
    s.push(arr[0])
    prev_greaters: list[NumberType] = [-1]
    for i in range(1, len(arr)):
        while s.is_empty() is False and s.peek() <= arr[i]:
            s.pop()
        prev_greaters.append(-1 if s.is_empty() else s.peek())
        s.push(arr[i])
    return prev_greaters
