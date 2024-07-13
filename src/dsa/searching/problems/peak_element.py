from src.helpers.custom_typevars import NumberType


def get_peak_element(arr: list[NumberType]) -> NumberType | None:
    n = len(arr)
    if n == 0:
        return None
    # If one element the that is peak
    if n == 1:
        return arr[0]
    # Now proceed with binary search to find peak
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (
            mid == n - 1 or arr[mid + 1] <= arr[mid]
        ):
            # Mid is peak
            return arr[mid]
        elif arr[mid - 1] > arr[mid]:
            # slope is increasing on left side so consider left half
            high = mid - 1
        else:
            # Slope is increasing on right side
            low = mid + 1
    return None
