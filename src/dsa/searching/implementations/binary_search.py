from src.helpers.custom_typevars import NumberType


def binary_search(arr: list[NumberType], target: NumberType) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1
