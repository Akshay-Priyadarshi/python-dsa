from src.helpers.custom_typevars import NumberType


def get_last_occurence(arr: list[NumberType], target: NumberType) -> int:
    """
    This function gets the index of the last occurence of the target in
    the sorted array and return -1 if target is not found.
    Time Complexity: log(n)
    Space Complexity: 1
    """
    low = 0
    high = len(arr) - 1
    res = -1
    while low <= high:
        mid = low + (high - low) // 2
        if target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
