from tqdm import tqdm
import numpy as np
import pandas as pd
from collections import Counter

def parse_line(line: str):

    sensor = line[: line.index(":")]
    sensor_x = int(sensor[sensor.index("x=") + 2 : sensor.index(",")])
    sensor_y = int(sensor[sensor.index("y=") + 2 :])

    beacon = line[line.index(":") + 1 :]
    beacon_x = int(beacon[beacon.index("x=") + 2 : beacon.index(",")])
    beacon_y = int(beacon[beacon.index("y=") + 2 :])

    return [sensor_x + sensor_y * 1j, beacon_x + beacon_y * 1j]


def part_one(file_path: str, y=2_000_000) -> int:
    """[summary]

    Args:
        file_path (str): input file

    Returns:
        [type]: [description]
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    data = np.array([parse_line(line) for line in lines])

    manhattan_dist = np.diff(data, axis=1)[:, 0]
    manhattan_dist = np.abs(np.real(manhattan_dist)) + np.abs(np.imag(manhattan_dist))

    y_dist = np.abs(np.imag(data[:,0]) - y)

    x_dist = np.vstack(manhattan_dist - y_dist).clip(min=0)[:,0]

    x_range = np.vstack([np.real(data[:,0]) - x_dist, np.real(data[:,0]) + x_dist]).T.astype(int)

    ruled_out = []
    for row in x_range:
        ruled_out.append(np.arange(start=row[0], stop=row[1]+1))
    
    ruled_out = np.concatenate(ruled_out)
    ruled_out = np.unique(ruled_out)

    beacons = np.real(data[:, 1])[np.where(np.imag(data[:, 1])==y)]
    beacons = np.unique(beacons)
        
    return len(ruled_out) - len(beacons)

def part_two(file_path: str, max_val=4000000, n_rows=2):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()
    
    data = np.array([parse_line(line) for line in lines])

    manhattan_dist = np.diff(data, axis=1)[:, 0]
    manhattan_dist = np.abs(np.real(manhattan_dist)) + np.abs(np.imag(manhattan_dist))

    co_ords = []
    for i in range(len(data)):
        # calculate y values of perimeter
        y_range = np.arange(
                        start = np.imag(data[i,0]) - manhattan_dist[i] - 1,
                        stop= np.imag(data[i,0]) + manhattan_dist[i] + 2
                        )
        # calculate y distance for each of those
        y_dist = np.abs(np.imag(data[i,0]) - y_range)
        # calculate remaining x_dist for each value
        x_dist = manhattan_dist[i] + 1 - y_dist
        # minimum value and maximum_value
        x_min = np.real(data[i,0]) - x_dist
        x_max = np.real(data[i,0]) + x_dist

        co_ords.append(np.concatenate([x_min, x_max]) + 1j * np.concatenate([y_range, y_range]))

    co_ords = np.concatenate(co_ords)

    co_ords = np.array([key for key, value in Counter(co_ords).items() if value >=4])
    
    co_ords = co_ords[np.where(
        (np.real(co_ords) >= 0) & 
        (np.real(co_ords) <= max_val) &  
        (np.imag(co_ords) >= 0) & 
        (np.imag(co_ords) <= max_val))]
    
    co_ords_grid, sensors = np.meshgrid(co_ords, data[:,0])
    coord_sensor_distance = co_ords_grid - sensors
    coord_sensor_distance = np.abs(np.real(coord_sensor_distance)) + np.abs(np.imag(coord_sensor_distance))

    _, man_dist = np.meshgrid(co_ords, manhattan_dist)

    free_space = co_ords[(coord_sensor_distance > man_dist).all(axis=0)][0]

    return  np.real(free_space)*4000000 + np.imag(free_space)



if __name__ == "__main__":
    print(part_one("aoc/inputs/day_15.txt"))
    print(part_two("aoc/inputs/day_15.txt"))
