from src.helpers.custom_typevars import NumberType
from stack.implementation import Stack


def naive_stock_span(arr: list[NumberType]) -> list[NumberType]:
    """
    Time Complexity - n^2
    """
    spans: list[NumberType] = []
    for i, el in enumerate(arr):
        span = 0
        for j in range(i, 0 - 1, -1):
            if arr[j] > arr[i]:
                break
            span += 1
        spans.append(span)
    return spans


def efficient_stock_span(arr: list[NumberType]) -> list[NumberType]:
    spans: list[NumberType] = []
    s = Stack[int](size=len(arr))
    s.push(0)
    spans.append(1)
    for i in range(1, len(arr)):
        while s.is_empty() is False and arr[s.peek()] <= arr[i]:
            s.pop()
        spans.append(i + 1 if s.is_empty() else i - s.peek())
        s.push(i)
    return spans
