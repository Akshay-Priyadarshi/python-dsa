import pytest
from src.dsa.searching.problems.first_occurence import get_first_occurence


def test_get_first_occurence_found():
    arr = [1, 2, 2, 3, 4, 4, 4, 5]
    assert get_first_occurence(arr, 4) == 4
    assert get_first_occurence(arr, 2) == 1
    assert get_first_occurence(arr, 5) == 7


def test_get_first_occurence_not_found():
    arr = [1, 2, 2, 3, 4, 4, 4, 5]
    assert get_first_occurence(arr, 6) == -1
    assert get_first_occurence(arr, 0) == -1


def test_get_first_occurence_empty():
    arr = []
    assert get_first_occurence(arr, 1) == -1


def test_get_first_occurence_single_element():
    arr = [5]
    assert get_first_occurence(arr, 5) == 0
    assert get_first_occurence(arr, 1) == -1


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 2, 2, 3], 2, 1),
        ([1, 1, 1, 1, 1], 1, 0),
        ([1, 2, 3, 4, 5], 6, -1),
        ([2, 2, 2, 2, 2], 2, 0),
        ([1],2,1)
    ],
)
def test_get_first_occurence_param(arr, target, expected):
    assert get_first_occurence(arr, target) == expected
