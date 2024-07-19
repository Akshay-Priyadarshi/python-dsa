from src.helpers.custom_typevars import NumberType


def has_pair_with_sum(arr: list[NumberType], target: NumberType) -> bool:
    low = 0
    high = len(arr) - 1
    while low < high:
        temp_sum = arr[low] + arr[high]
        if temp_sum == target:
            return True
        elif temp_sum < target:
            low += 1
        else:
            high -= 1
    return False
