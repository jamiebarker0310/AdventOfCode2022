from aoc.day_05 import part_one, part_two, parse_stacks, parse_moves


def test_parse_stacks():

    test_file_path = "tests/test_inputs/test_day_05.txt"

    with open(test_file_path) as f:
        lines = f.readlines()

    expected = [["Z", "N"], ["M", "C", "D"], ["P"]]

    response = parse_stacks(lines)

    assert expected == response


def test_parse_moves():

    test_file_path = "tests/test_inputs/test_day_05.txt"

    with open(test_file_path) as f:
        lines = f.readlines()

    expected = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]

    response = parse_moves(lines)

    assert expected == response


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_05.txt"

    assert part_one(test_file_path) == "CMZ"


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_05.txt"

    assert part_two(test_file_path) == "MCD"
