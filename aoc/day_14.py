import numpy as np
import matplotlib.pyplot as plt


def parse_rock_grid(file_path: str) -> set:
    """
    parses line into set of coordinates of all rocks

    Args:
        file_path (str): input file path

    Returns:
        set: co-ordinates of all rocks
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # initialise empty rock
    rock = []
    # for each lines
    for line in lines:
        # split points  by arrow
        pairs = line.split(" -> ")
        # for pairs of points
        for pair1, pair2 in zip(pairs[:-1], pairs[1:]):
            # convert to int
            x1, y1 = map(int, pair1.split(","))
            x2, y2 = map(int, pair2.split(","))
            # add co ordinates
            rock.append((x1, y1))
            rock.append((x2, y2))
            # if it is a vertical line
            if x1 == x2:
                # if an upward line
                if y1 <= y2:
                    # swap direction
                    y2, y1 = y1, y2
                # going downward
                for i in range(y1 - y2):
                    # add point on path
                    rock.append((x1, y2 + i))
            # if it is a horizontal line
            elif y1 == y2:
                # if rightward line
                if x1 <= x2:
                    # swap direction
                    x2, x1 = x1, x2
                for i in range(x1 - x2):
                    # add point on path
                    rock.append((x2 + i, y1))
    # convert to set
    rock = set([(x, y) for x, y in rock])
    # return set and maximum depth
    return rock, max([y for x, y in rock])


def sandfall(rock: set, max_depth: int) -> tuple:
    """
    simulates sand fall from (500, 0)

    Args:
        rock (set): set of existing rocks and sand
        max_depth (int): maximum depth

    Returns:
        tuple: co-ordinate of sand after simulation
        y is None if the sand falls below minimum depth
    """
    # intialise starting point
    x, y = 500, 0
    # while above maximum depth
    while y <= max_depth:
        # if directly below free
        if (x, y + 1) not in rock:
            # fall down
            y += 1
        # if down left free
        elif (x - 1, y + 1) not in rock:
            # fall down left
            x -= 1
            y += 1
        # if down right free
        elif (x + 1, y + 1) not in rock:
            # fall down right
            x += 1
            y += 1
        # else return the final position
        else:
            return (x, y)
    # if falls below, maximum depth return y as none
    return (x, None)


def show_rock(initial_rock: set, sanded_rocks: set):
    """
    shows image of rock tavern after sandfall

    Args:
        initial_rock (set): set of co-ords of rocks
        sanded_rocks (set): set of co-ords rocks and sand
    """
    # convert to numpy arrays
    sand_array = np.array([[x, y] for x, y in sanded_rocks])
    rock_array = np.array([[x, y] for x, y in initial_rock])

    # normalise so min x is 0  and min y is 0
    norm_sand_array = sand_array - sand_array.min(axis=0)
    norm_rock_array = rock_array - sand_array.min(axis=0)

    # intialise empty array
    grid = np.zeros(shape=norm_sand_array.max(axis=0)[::-1] + 1)

    # increase coordinates by 1
    for x, y in norm_rock_array:
        grid[y, x] += 1

    # increase coordinates by 1
    for x, y in norm_sand_array:
        grid[y, x] += 1

    # draw image
    plt.imshow(grid / 2)
    # show image
    plt.show()


def part_one(file_path: str) -> int:
    """
    parses rocks
    then calculates how many sands fall until one
    falls infinitely

    Args:
        file_path (str): input file

    Returns:
        int: how many sand grains fall
    """
    # parse rocks
    rock, max_depth = parse_rock_grid(file_path)
    # intialise results
    result = ()
    count = 0
    while result is not None:
        # simulate sandfall
        x, y = sandfall(rock, max_depth)
        # if sand did not fall down forever
        if y is not None:
            # add coord to rock
            rock.add((x, y))
            # increase count
            count += 1
        # else return the final count
        else:
            return count


def part_two(file_path: str) -> int:
    """
    parses rocks
    calculates how many grains of sand it takes to
    fill up to (500,0) when there is an infinite floor
    2 below the lowest rock

    Args:
        file_path (str): input file

    Returns:
        int: number of grains of sand to reach (500,0)
    """
    # parse rock
    rock, max_depth = parse_rock_grid(file_path)
    # # initialise rock for drawing
    # initial_rock = set([(x, y) for x, y in rock])

    # increment max depth by 1
    max_depth += 1
    # initialise count and x,y co-ords
    x, y = None, None
    count = 0
    # while x,y is not 500, 0
    while (500, 0) != (x, y):
        # simulate sandfall
        x, y = sandfall(rock, max_depth)
        # if y is falling infinitely
        if y is None:
            # y is now maximum depth
            y = max_depth
        # add sand to rocks
        rock.add((x, y))
        # increase count
        count += 1
    # show rock
    # show_rock(initial_rock, rock)
    # return count
    return count


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_14.txt"))
    print(part_two("aoc/inputs/day_14.txt"))
