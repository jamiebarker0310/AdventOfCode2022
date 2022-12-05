import string


def part_one(file_path: str) -> int:
    """
    splits string in half
    finds common letter
    returns sum of score of letters e.g. a->1, A->27

    Args:
        file_path (str): filepath

    Returns:
        int: sum of score of common letters
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    return sum(
        [
            string.ascii_letters.index(
                (set(line[: len(line) // 2]) & set(line[len(line) // 2 :])).pop()
            )
            + 1
            for line in lines
        ]
    )


def part_two(file_path: str) -> int:
    """
    splits strings into group of 3 strings
    find only common letter
    returns sum of score of letters e.g. a->1, A->27
    Args:
        file_path (str): filepath

    Returns:
        [type]: sum of score of common letters
    """

    with open(file_path) as f:
        lines = f.readlines()

    return sum(
        [
            string.ascii_letters.index(
                set.intersection(*map(set, lines[i : i + 3])).pop()
            )
            + 1
            for i in range(0, len(lines), 3)
        ]
    )


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_03.txt"))
    print(part_two("aoc/inputs/day_03.txt"))
