import pytest

from src.helpers.custom_typevars import NumberType
from src.pareto.array.contain_duplicates import check_duplicates


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 5, 8, 12, 30], False),
        ([3, 8, 13, 18], False),
        ([2, 4, 8, 9, 11, 8, 12, 20, 30], True),
    ],
)
def test_check_duplicates(
    arr: list[NumberType],
    expected: bool,
):
    result = check_duplicates(arr)
    assert result == expected
