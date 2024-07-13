from src.helpers.custom_typevars import NumberType


def search_sorted_rotated_array(arr: list[NumberType], target: NumberType) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        low_el = arr[low]
        high_el = arr[high]
        mid_el = arr[mid]
        if target == arr[mid]:
            return mid
        if mid_el >= low_el:
            # Left is sorted so we check on the left
            if target >= low_el and target < mid_el:
                # On left
                high = mid - 1
            else:
                # On right
                low = mid + 1
        else:
            # Right is sorted so we check on right
            if target <= high_el and target > mid_el:
                low = mid + 1
            else:
                high = mid - 1
    return -1
