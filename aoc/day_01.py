def part_one(file_path: str) -> int:
    """
    splits lines of integers by blank lines
    then takes the sum of each of the integeres
    and returns the maximum

    Args:
        file_path (str): input filepath

    Returns:
        int: maximum calorie count
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    max_calories = 0
    sum_calories = 0
    for line in lines + ["\n"]:
        try:
            sum_calories += int(line.strip())
        except ValueError:
            max_calories = max(max_calories, sum_calories)
            sum_calories = 0

    return max_calories


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    calories = []
    sum_calories = 0
    for line in lines + ["\n"]:
        try:
            sum_calories += int(line.strip())
        except ValueError:
            calories.append(sum_calories)
            sum_calories = 0
    return sum(sorted(calories)[-3:])


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_01.txt"))
    print(part_two("aoc/inputs/day_01.txt"))
