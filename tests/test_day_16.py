import pytest

from aoc.day_16 import part_one, part_two, Valve


@pytest.mark.parametrize(
    "line,expected",
    [
        (
            "Valve OQ has flow rate=17; tunnels lead to valves NB, AK, KL",
            {
                "valve_name": "OQ",
                "flow_rate": 17,
                "adjacent_valves": ["NB", "AK", "KL"],
            },
        )
    ],
)
def test_valve_init(line, expected):

    response = Valve(line)

    assert response.valve_name == expected["valve_name"]
    assert response.flow_rate == expected["flow_rate"]
    assert response.adjacent_valves == expected["adjacent_valves"]
    assert response.opened == False


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_16.txt"

    assert part_one(test_file_path) == 1651


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_16.txt"

    assert part_two(test_file_path)
