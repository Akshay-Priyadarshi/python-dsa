import pytest

from src.dsa.searching.problems.pair_with_sum import has_pair_with_sum
from src.helpers.custom_typevars import NumberType


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([2, 5, 8, 12, 30], 17, True),
        ([3, 8, 13, 18], 14, False),
        ([2, 4, 8, 9, 11, 12, 20, 30], 23, True),
    ],
)
def test_has_pair_with_sum(
    arr: list[NumberType],
    target: NumberType,
    expected: list[NumberType] | NumberType | None,
):
    result = has_pair_with_sum(arr, target)
    assert result == expected
