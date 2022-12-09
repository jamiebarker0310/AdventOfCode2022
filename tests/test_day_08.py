import numpy as np
import pytest

from aoc.day_08 import part_one, part_two, scenic_score


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_08.txt"

    assert part_one(test_file_path) == 21


@pytest.mark.parametrize("i,j,expected", [(1, 2, 4), (3, 2, 8)])
def test_scenic_score(i, j, expected):

    test_file_path = "tests/test_inputs/test_day_08.txt"

    with open(test_file_path) as f:
        lines = f.readlines()

    height_map = np.array([[int(x) for x in line.strip()] for line in lines])

    assert scenic_score(i, j, height_map) == expected


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_08.txt"

    assert part_two(test_file_path) == 8
