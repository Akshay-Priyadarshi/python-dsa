from src.helpers.custom_typevars import NumberType
from stack.implementation import Stack


def next_greater(arr: list[NumberType]) -> list[NumberType]:
    s = Stack[NumberType](size=len(arr))
    s.push(arr[-1])
    next_greaters: list[NumberType] = [-1]
    for i in range(len(arr) - 2, -1, -1):
        while s.is_empty() is False and s.peek() <= arr[i]:
            s.pop()
        next_greaters.insert(0, -1 if s.is_empty() else s.peek())
        s.push(arr[i])
    return next_greaters
