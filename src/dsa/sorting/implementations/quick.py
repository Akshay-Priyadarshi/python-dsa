from src.helpers.custom_typevars import NumberType


def partition(arr: list[NumberType], pivot: int) -> list[NumberType]:
    # Adjustment to the pivot when its not the last element
    arr[pivot], arr[len(arr) - 1] = arr[len(arr) - 1], arr[pivot]
    pivot = len(arr) - 1
    # Normal partition
    print(arr)
    pivot_value = arr[pivot]
    i = -1
    for j in range(len(arr)):
        if arr[j] < pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[pivot] = arr[pivot], arr[i]
    return arr
