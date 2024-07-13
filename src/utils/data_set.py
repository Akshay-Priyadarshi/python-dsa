import random

from src.helpers.custom_typevars import NumberType


def generate_random_array(
    size: int,
    sorted: bool | None = False,
    minEl: NumberType = 0,
    maxEl: NumberType = 100,
) -> list[int] | list[float]:
    if type(minEl) is float and type(maxEl) is float:
        array = [random.uniform(minEl, maxEl) for _ in range(size)]
    elif type(minEl) is int and type(maxEl) is int:
        array = [random.randint(minEl, maxEl) for _ in range(size)]
    else:
        raise Exception("Pass valid types for min and max element!")
    # If sorted is True, sort the array
    if sorted:
        array.sort()
    return array
