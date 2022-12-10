from aoc.day_10 import part_one, part_two, ClockCircuit


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_10.txt"

    assert part_one(test_file_path) == 13140


def test_clock_circuit():

    test_file_path = "tests/test_inputs/test_day_10_simple.txt"

    with open(test_file_path) as f:
        lines = f.readlines()
    clock_circuit = ClockCircuit(cycle_checks=[1, 2, 3, 4, 5])
    for line in lines:
        if line.strip() == "noop":
            clock_circuit.noop()
        else:
            value = int(line.strip().split(" ")[-1])
            clock_circuit.add_x(value)

    assert clock_circuit.cycle_values[1] == 1
    assert clock_circuit.cycle_values[2] == 1
    assert clock_circuit.cycle_values[3] == 1
    assert clock_circuit.cycle_values[4] == 4
    assert clock_circuit.cycle_values[5] == 4


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_10.txt"
    expected_file_path = "tests/test_inputs/test_day_10_2_expected.txt"

    with open(expected_file_path) as f:
        expected = f.readlines()

    expected = "\n".join([line.strip() for line in expected])

    assert part_two(test_file_path) == expected
