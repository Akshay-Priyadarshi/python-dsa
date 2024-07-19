from src.helpers.custom_typevars import NumberType


def check_duplicates(arr: list[NumberType]) -> bool:
    distinct_arr = set(arr)
    return len(distinct_arr) != len(arr)
