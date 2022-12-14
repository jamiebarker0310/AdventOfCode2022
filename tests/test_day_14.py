from aoc.day_14 import part_one, part_two, parse_rock_grid


def test_parse_rock_grid():

    test_file_path = "tests/test_inputs/test_day_14.txt"

    expected = set(
        [
            (498, 4),
            (498, 5),
            (498, 6),
            (497, 6),
            (496, 6),
            (503, 4),
            (502, 4),
            (502, 5),
            (502, 6),
            (502, 7),
            (502, 8),
            (502, 9),
            (501, 9),
            (500, 9),
            (499, 9),
            (498, 9),
            (497, 9),
            (496, 9),
            (495, 9),
            (494, 9),
        ]
    )

    response, _ = parse_rock_grid(test_file_path)

    response = sorted(list(response))
    expected = sorted(list(expected))

    assert response == expected


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_14.txt"

    assert part_one(test_file_path) == 24


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_14.txt"

    assert part_two(test_file_path) == 93
