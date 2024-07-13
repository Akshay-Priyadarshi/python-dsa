import pytest

from src.dsa.searching.problems.peak_element import get_peak_element
from src.helpers.custom_typevars import NumberType


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([5, 10, 20, 15, 7], 20),
        ([10, 20, 15, 5, 23, 90, 67], [20, 90]),
        ([80, 70, 60], 80),
        ([80, 70, 90], [80, 90]),
        ([80, 70], 80),
        ([10, 10, 10, 10], 10),
    ],
)
def test_get_first_occurence_param(
    arr: list[NumberType], expected: list[NumberType] | NumberType | None
):
    result = get_peak_element(arr)
    if isinstance(expected, list):
        assert result in expected
    else:
        assert result == expected
