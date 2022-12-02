from aoc.day_02 import part_one, part_two, result_score, calculate_move
import pytest


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_02.txt"

    assert part_one(test_file_path) == 15


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_02.txt"

    assert part_two(test_file_path) == 12


@pytest.mark.parametrize(
    "a,b,score",
    [
        (0, 0, 3),
        (0, 1, 6),
        (0, 2, 0),
        (1, 0, 0),
        (1, 1, 3),
        (1, 2, 6),
        (2, 0, 6),
        (2, 1, 0),
        (2, 2, 3),
    ],
)
def test_result_score(a, b, score):

    assert result_score(a, b) == score


@pytest.mark.parametrize(
    "a,r,move",
    [
        (0, 0, 2),
        (0, 1, 0),
        (0, 2, 1),
        (1, 0, 0),
        (1, 1, 1),
        (1, 2, 2),
        (2, 0, 1),
        (2, 1, 2),
        (2, 2, 0),
    ],
)
def test_result_score(a, r, move):

    assert calculate_move(a, r) == move
