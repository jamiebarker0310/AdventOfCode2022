import numpy as np
from collections import Counter
from functools import reduce


def parse_line(line: str) -> list:
    """
    parse string and return list of complex numbers
    first representing sensor
    second representing beacon

    Args:
        line (str): line

    Returns:
        list: list of sesnosr beacon
    """
    # initialise data
    data = []
    # for sensor and beacon
    for substr in [line[: line.index(":")], line[line.index(":") + 1 :]]:
        # find x and y
        substr_x = int(substr[substr.index("x=") + 2 : substr.index(",")])
        # multiple y by complex
        substr_y = int(substr[substr.index("y=") + 2 :]) * 1j
        # append to data
        data.append(substr_x + substr_y)
    # return data
    return data


def part_one(file_path: str, y: int = 2_000_000) -> int:
    """
    reads file
    parses data
    calculates difference between sensor and beacon



    Args:
        file_path (str): input file
        y (int, optional): y value to check ruled out x points for.
            Defaults to 2_000_000.

    Returns:
        int: Number of x coordinates ruled out
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # parse files
    data = np.array([parse_line(line) for line in lines])
    # calculates difference between sensor and beacon
    manhattan_dist = np.diff(data, axis=1)[:, 0]
    manhattan_dist = np.abs(np.real(manhattan_dist)) + np.abs(np.imag(manhattan_dist))
    # calculate y distance
    y_dist = np.abs(np.imag(data[:, 0]) - y)
    # calculate x distance it can be
    x_dist = np.vstack(manhattan_dist - y_dist).clip(min=0)[:, 0]
    # calculate min and max x_val
    x_range = np.vstack(
        [np.real(data[:, 0]) - x_dist, np.real(data[:, 0]) + x_dist]
    ).T.astype(int)
    # initialise ruled out positions
    ruled_out = []
    # for each row
    for row in x_range:
        # append the range between the two values
        ruled_out.append(np.arange(start=row[0], stop=row[1] + 1))
    # concatenate values
    ruled_out = np.concatenate(ruled_out)
    # take unique of values
    ruled_out = np.unique(ruled_out)
    # remove all beacons on the row
    beacons = np.real(data[:, 1])[np.where(np.imag(data[:, 1]) == y)]
    beacons = np.unique(beacons)
    return len(ruled_out) - len(beacons)


def part_two(file_path: str, max_val=4000000) -> int:
    """
    read file
    parse data
    calculate manhattan distnace between sensors and beacons
    for each sensor, beacon calculate the outer perimeter
    create set of perimeter points that occur at least 4 times
    check whether each of these can be a beacon

    Args:
        file_path (str): file path
        max_val (int, optional): maximum value of ruled out point.
        Defaults to 4000000.

    Returns:
        int: 4000000 * x coordinate + y coordinate of ruled out point
    """
    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # parse data
    data = np.array([parse_line(line) for line in lines])
    # calcaulte manhattan distances
    manhattan_dist = np.diff(data, axis=1)[:, 0]
    manhattan_dist = np.abs(np.real(manhattan_dist)) + np.abs(np.imag(manhattan_dist))
    # initialise counter object
    counter = Counter()
    # for each pair
    for i in range(len(data)):
        # calculate y values of perimeter
        y_range = np.arange(
            start=np.imag(data[i, 0]) - manhattan_dist[i] - 1,
            stop=np.imag(data[i, 0]) + manhattan_dist[i] + 2,
        )
        # calculate y distance for each of those
        y_dist = np.abs(np.imag(data[i, 0]) - y_range)
        # calculate remaining x_dist for each value
        x_dist = manhattan_dist[i] + 1 - y_dist
        # minimum value and maximum_value
        x_min = np.real(data[i, 0]) - x_dist
        x_max = np.real(data[i, 0]) + x_dist
        # get coords
        co_ords = np.concatenate([x_min, x_max]) + 1j * np.concatenate(
            [y_range, y_range]
        )
        # filter coordinates
        co_ords = co_ords[
            np.where(
                reduce(
                    lambda x, y: x & y,
                    [
                        np.real(co_ords) >= 0,
                        np.real(co_ords) <= max_val,
                        np.imag(co_ords) >= 0,
                        np.imag(co_ords) <= max_val,
                    ],
                )
            )
        ]
        # append all values
        counter.update(
            np.concatenate([x_min, x_max]) + 1j * np.concatenate([y_range, y_range])
        )
    # filter on all coords that occur 4+ times
    co_ords = np.array([key for key, value in counter.items() if value >= 4])
    # calculate distances from all beacons
    co_ords_grid, sensors = np.meshgrid(co_ords, data[:, 0])
    coord_sensor_distance = co_ords_grid - sensors
    coord_sensor_distance = np.abs(np.real(coord_sensor_distance)) + np.abs(
        np.imag(coord_sensor_distance)
    )
    # get manhattan distance for each coord
    _, man_dist = np.meshgrid(co_ords, manhattan_dist)
    # ensure all are outside manhattan distance
    free_space = co_ords[(coord_sensor_distance > man_dist).all(axis=0)][0]
    # return calc value of free space
    return np.real(free_space) * 4000000 + np.imag(free_space)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_15.txt"))
    print(part_two("aoc/inputs/day_15.txt"))
