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
    # add an empty line to finish last elf
    for line in lines + ["\n"]:
        # try to convert to int
        try:
            # add to total calories
            sum_calories += int(line.strip())
        except ValueError:
            # update maximum calories
            max_calories = max(max_calories, sum_calories)
            # reset calorie count
            sum_calories = 0
    # return max calories
    return max_calories


def part_two(file_path: str) -> int:
    """
    splits lines of integers by blank lines
    then takes the sum of each of the integeres
    and returns the sum of the 3 largest values

    Args:
        file_path (str): input filepath

    Returns:
        int: sum of the 3 largest values
    """
    #  read file
    with open(file_path) as f:
        lines = f.readlines()
    # initialise list of empty calories
    calories = []
    # initialise calorie count
    sum_calories = 0
    # add an empty line to finish last elf
    for line in lines + ["\n"]:
        # try to convert to int
        try:
            # add to total calories
            sum_calories += int(line.strip())
        except ValueError:
            # update maximum calories
            calories.append(sum_calories)
            # reset calorie count
            sum_calories = 0
    # return sum of 3 largest values
    return sum(sorted(calories)[-3:])


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_01.txt"))
    print(part_two("aoc/inputs/day_01.txt"))
