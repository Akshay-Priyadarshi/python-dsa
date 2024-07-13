from src.helpers.custom_typevars import NumberType


def linear_search(arr: list[NumberType], target: NumberType) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
