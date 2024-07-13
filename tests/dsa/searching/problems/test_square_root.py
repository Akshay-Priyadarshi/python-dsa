import pytest

from src.dsa.searching.problems.square_root import get_square_root


@pytest.mark.parametrize(
    "num, expected",
    [(4, 2), (13, -1), (16, 4)],
)
def test_get_square_root(num, expected):
    assert get_square_root(num) == expected
