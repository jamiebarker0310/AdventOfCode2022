from aoc.day_11 import part_one, part_two, Monkey


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_11.txt"

    assert part_one(test_file_path) == 10605


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_11.txt"

    assert part_two(test_file_path) == 2713310158


def test_monkey_init():

    test_file_path = "tests/test_inputs/test_day_11.txt"

    with open(test_file_path) as f:
        lines = f.readlines()

    monkey = Monkey(lines[0:6])
    assert monkey.items == [79, 98]
    # assert test
    for i in range(1000):
        assert monkey.operation(i) == 19 * i
        assert monkey.test(i) == (i % 23 == 0)

    assert monkey.true_monkey == 2
    assert monkey.false_monkey == 3


def test_monkey_round():

    test_file_path = "tests/test_inputs/test_day_11.txt"

    with open(test_file_path) as f:
        lines = f.readlines()

    monkey = Monkey(lines[0:6])

    output = monkey.round()

    assert output == [(3, 500), (3, 620)]
