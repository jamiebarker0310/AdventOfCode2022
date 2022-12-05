def part_one(file_path: str) -> int:
    """
    count of pairs where number pair
    completely overlap one of the options

    Args:
        file_path (str): filepath

    Returns:
        int: pair count
    """

    # read file
    with open(file_path) as f:
        lines = f.read().splitlines()

    count = 0
    for line in lines:
        p1, p2 = line.split(",")

        p1a, p1b = map(int, p1.split("-"))
        p2a, p2b = map(int, p2.split("-"))

        if (min(p1a, p2a) == p1a and max(p1b, p2b) == p1b) or (
            min(p1a, p2a) == p2a and max(p1b, p2b) == p2b
        ):
            count += 1

    return count


def part_two(file_path: str):
    """
    get counts of pairs that overlap at all

    Args:
        file_path (str): file path

    Returns:
        int: count of overlapping pairs
    """

    with open(file_path) as f:
        lines = f.read().splitlines()
    count = 0
    for line in lines:
        p1, p2 = line.split(",")

        p1a, p1b = map(int, p1.split("-"))
        p2a, p2b = map(int, p2.split("-"))

        try:
            (set(range(p1a, p1b + 1)) & set(range(p2a, p2b + 1))).pop()
            count += 1
        except:
            continue

    return count


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_04.txt"))
    print(part_two("aoc/inputs/day_04.txt"))
