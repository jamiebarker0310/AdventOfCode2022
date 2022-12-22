import pytest

from aoc.day_15 import part_one, part_two, parse_line


@pytest.mark.parametrize(
    "line,expected",
    [
        ("Sensor at x=2, y=18: closest beacon is at x=-2, y=15", [2 + 18j, -2 + 15j]),
        ("Sensor at x=9, y=16: closest beacon is at x=10, y=16", [9 + 16j, 10 + 16j]),
        (
            "Sensor at x=13, y=2: closest beacon is at x=15, y=3",
            [13 + 2j, 15 + 3j],
        ),
        (
            "Sensor at x=12, y=14: closest beacon is at x=10, y=16",
            [12 + 14j, 10 + 16j],
        ),
        (
            "Sensor at x=10, y=20: closest beacon is at x=10, y=16",
            [10 + 20j, 10 + 16j],
        ),
        (
            "Sensor at x=14, y=17: closest beacon is at x=10, y=16",
            [14 + 17j, 10 + 16j],
        ),
        (
            "Sensor at x=8, y=7: closest beacon is at x=2, y=10",
            [8 + 7j, 2 + 10j],
        ),
        ("Sensor at x=2, y=0: closest beacon is at x=2, y=10", [2, 2 + 10j]),
        (
            "Sensor at x=0, y=11: closest beacon is at x=2, y=10",
            [0 + 11j, 2 + 10j],
        ),
        (
            "Sensor at x=20, y=14: closest beacon is at x=25, y=17",
            [20 + 14j, 25 + 17j],
        ),
        (
            "Sensor at x=17, y=20: closest beacon is at x=21, y=22",
            [17 + 20j, 21 + 22j],
        ),
        (
            "Sensor at x=16, y=7: closest beacon is at x=15, y=3",
            [16 + 7j, 15 + 3j],
        ),
        (
            "Sensor at x=14, y=3: closest beacon is at x=15, y=3",
            [14 + 3j, 15 + 3j],
        ),
        (
            "Sensor at x=20, y=1: closest beacon is at x=15, y=3",
            [20 + 1j, 15 + 3j],
        ),
    ],
)
def test_parse_line(line, expected):

    assert parse_line(line) == expected


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_15.txt"

    assert part_one(test_file_path, y=10) == 26


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_15.txt"

    response = part_two(test_file_path, max_val=20)
    assert response == 56000011
