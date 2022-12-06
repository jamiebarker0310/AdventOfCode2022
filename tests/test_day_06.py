from aoc.day_06 import part_one, part_two, start_of_packet_detection
import pytest


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_06.txt"

    assert part_one(test_file_path) == [5, 6, 10, 11]


@pytest.mark.parametrize(
    "datastream, expected, n",
    [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 4),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6, 4),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 4),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 4),
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19, 14),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23, 14),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23, 14),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29, 14),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26, 14),
    ],
)
def test_start_of_packet_detection(datastream, expected, n):

    assert start_of_packet_detection(datastream, n) == expected


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_06.txt"

    assert part_two(test_file_path) == [23, 23, 29, 26]
