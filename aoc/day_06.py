def start_of_packet_detection(datastream: str, n: int) -> int:
    """
    returns number of characters before the previous n characters are unique

    Args:
        datastream (str): string
        n (int): number of characters to check are unique

    Returns:
        int: char count
    """

    i = 4
    marker = set()

    while len(marker) < n:
        marker = set(datastream[i - n : i])
        i += 1

    return i - 1


def part_one(file_path: str) -> int:
    """
    returns the number of characters needed to scan
    before the previous 4 characters are all unique

    Args:
        file_path (str): filepath

    Returns:
        int: character count
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    return [start_of_packet_detection(line, n=4) for line in lines]


def part_two(file_path: str):
    """
    returns the number of characters needed to scan
    before the previous 14 characters are all unique


    Args:
        file_path (str): filepath

    Returns:
        int: character count
    """

    with open(file_path) as f:
        lines = f.readlines()

    return [start_of_packet_detection(line, n=14) for line in lines]


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_06.txt"))
    print(part_two("aoc/inputs/day_06.txt"))
