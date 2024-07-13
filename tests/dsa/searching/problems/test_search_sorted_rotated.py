import pytest
from src.dsa.searching.problems.search_sorted_rotated import search_sorted_rotated_array
from src.helpers.custom_typevars import NumberType


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([10, 20, 40, 60, 5, 8], 40, 2),
        ([100, 200, 300, 10, 20], 30, -1),
        # Float test cases
        ([10.0, 20.0, 40.0, 60.0, 5.0, 8.0], 40.0, 2),
        ([100.5, 200.5, 300.5, 10.5, 20.5], 30.5, -1),
    ],
)
def test_search_sorted_rotated_array(
    arr: list[NumberType], target: NumberType, expected: list[int] | int
):
    result = search_sorted_rotated_array(arr, target)
    if isinstance(expected, list):
        assert result in expected
    else:
        assert result == expected
