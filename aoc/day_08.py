import numpy as np


def part_one(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    height_map = np.array([[int(x) for x in line.strip()] for line in lines])
    visible_trees = (sum(height_map.shape) * 2) - 4
    for i in range(1, height_map.shape[0] - 1):
        for j in range(1, height_map.shape[1] - 1):
            val = height_map[i, j]
            top_view = height_map[:i, j].max()
            below_view = height_map[i + 1 :, j].max()
            left_view = height_map[i, :j].max()
            right_view = height_map[i, j + 1 :].max()
            if min(val, top_view, below_view, left_view, right_view) != val:
                visible_trees += 1

    return visible_trees


def scenic_score(i, j, height_map):

    height = height_map[i, j]
    up_distance = calculate_distance(height, height_map[:i, j][::-1])
    left_distance = calculate_distance(height, height_map[i, :j][::-1])
    right_distance = calculate_distance(height, height_map[i, j + 1 :])
    below_distance = calculate_distance(height, height_map[i + 1 :, j])

    return np.prod([up_distance, left_distance, right_distance, below_distance])


def calculate_distance(height, view):

    try:
        return np.where(view >= height)[0][0] + 1
    except IndexError:
        return len(view)


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    with open(file_path) as f:
        lines = f.readlines()

    height_map = np.array([[int(x) for x in line.strip()] for line in lines])
    scores = []
    for i in range(height_map.shape[0]):
        for j in range(height_map.shape[1]):
            scores.append(scenic_score(i, j, height_map))
    return max(scores)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_08.txt"))
    print(part_two("aoc/inputs/day_08.txt"))
