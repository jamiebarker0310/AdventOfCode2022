import numpy as np


def part_one(file_path: str) -> int:
    """
    calculates how many trees can be seen from the edge of the forest

    Args:
        file_path (str): filepath to read

    Returns:
        int: number of visible trees
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # create height map
    height_map = np.array([[int(x) for x in line.strip()] for line in lines])
    # can see all trees on the edge
    visible_trees = (sum(height_map.shape) * 2) - 4
    # for all interior trees
    for i in range(1, height_map.shape[0] - 1):
        for j in range(1, height_map.shape[1] - 1):
            # get height
            val = height_map[i, j]
            # get tree heights in different directions
            top_view = height_map[:i, j].max()
            below_view = height_map[i + 1 :, j].max()
            left_view = height_map[i, :j].max()
            right_view = height_map[i, j + 1 :].max()
            # if the tree is not the smallest in one of the directions
            if min(val, top_view, below_view, left_view, right_view) != val:
                # it is a visible tree
                visible_trees += 1
    return visible_trees


def scenic_score(i: int, j: int, height_map: np.array) -> int:
    """
    calculates the scenic score for each tree

    Args:
        i (int): row
        j (int): column
        height_map (np.array): height map

    Returns:
        int: scenic score
    """
    # calculate height
    height = height_map[i, j]
    # calculate how far can be seen in each direction
    up_distance = calculate_distance(height, height_map[:i, j][::-1])
    left_distance = calculate_distance(height, height_map[i, :j][::-1])
    right_distance = calculate_distance(height, height_map[i, j + 1 :])
    below_distance = calculate_distance(height, height_map[i + 1 :, j])
    # return the product
    return np.prod([up_distance, left_distance, right_distance, below_distance])


def calculate_distance(height: int, view: np.array) -> int:
    """
    calculates how far can be seen from a tree

    Args:
        height (int): _description_
        view (np.array): _description_

    Returns:
        int: distance to tree
    """
    # attempt to find a tree bigger or the same size
    try:
        # return index of first tree
        return np.where(view >= height)[0][0] + 1
    # if can't find one
    except IndexError:
        # return length of view because we can see all the trees
        return len(view)


def part_two(file_path: str) -> int:
    """
    calculate the maximum scenic score of all trees

    Args:
        file_path (str): input file

    Returns:
        int: max scenic score
    """
    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # parse height map
    height_map = np.array([[int(x) for x in line.strip()] for line in lines])
    # initialise scores
    scores = []
    # get all scores of trees
    for i in range(height_map.shape[0]):
        for j in range(height_map.shape[1]):
            scores.append(scenic_score(i, j, height_map))
    # return max of scores
    return max(scores)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_08.txt"))
    print(part_two("aoc/inputs/day_08.txt"))
