from src.helpers.custom_typevars import NumberType
from .first_occurence import get_first_occurence
from .last_occurence import get_last_occurence


def get_number_of_occurence(arr: list[NumberType], target: NumberType) -> int:
    """
    This function gives the number of occurences of the target in the
    sorted array.
    Time Complexity: log(n)
    Space Complexity: 1
    """
    first_occurence = get_first_occurence(arr, target)
    if first_occurence == -1:
        return 0
    else:
        last_occurence = get_last_occurence(arr, target)
        return last_occurence - first_occurence + 1
