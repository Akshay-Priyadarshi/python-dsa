from typing import List


def move_zeroes_to_end(arr: List[int]):
    non_zero_count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[non_zero_count] = arr[non_zero_count], arr[i]
            non_zero_count += 1
    return arr

