from aoc.day_01 import part_one, part_two

def test_part_one():

    test_file_path = "tests/test_inputs/test_day_01.txt"

    assert part_one(test_file_path) == 24000

def test_part_two():

    test_file_path = "tests/test_inputs/test_day_01.txt"

    assert part_two(test_file_path) == 45000