import pytest
from aoc.day_13 import part_one, part_two, compare_lists


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1], True),
        ([[1], [2, 3, 4]], [[1], 4], True),
        ([9], [[8, 7, 6]], False),
        ([[4, 4], 4, 4], [[4, 4], 4, 4, 4], True),
        ([7, 7, 7, 7], [7, 7, 7], False),
        ([], [3], True),
        ([[[]]], [[]], False),
        (
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
            False,
        ),
    ],
)
def test_compare_lists(l1, l2, expected):

    assert compare_lists(l1, l2) == expected


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_13.txt"

    assert part_one(test_file_path) == 13


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_13.txt"

    assert part_two(test_file_path) == 140
