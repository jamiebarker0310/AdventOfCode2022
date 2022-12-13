import re
from math import gcd
from functools import reduce


class Monkey:
    def __init__(self, lines: str, inspection_worry: bool = True) -> None:
        """parses line input

        Args:
            lines (str): input set of strings
            inspection_worry (bool, optional): whether to divide by 3 after
            monkeys inspection.
                Defaults to True.
        """
        # get items monkey has
        self.items = [int(item) for item in lines[1].split(":")[-1].split(",")]
        # get operation as a lambda
        self.operation = eval(f"lambda old: {lines[2].split('=')[-1]}")
        # get divisor
        self.divisor = int(re.sub("[^0-9]", "", lines[3]))
        # create divisor function
        self.test = lambda x: x % self.divisor == 0
        # parse true and false monkey values
        self.true_monkey = int(re.sub("[^0-9]", "", lines[4]))
        self.false_monkey = int(re.sub("[^0-9]", "", lines[5]))
        # whether to divide by 3 after monkeys inspects
        self.inspection_worry = inspection_worry
        # initialise inspection count
        self.inspection_count = 0

    def round(self) -> list:
        """
        initialise empty output

        Returns:
            list: list of tuples of form (monkey, item) showing which item
            is thrown where
        """
        # initialise empty output
        output = []
        # for each item
        for item in self.items:
            # after inspection
            self.inspection_count += 1
            # apply operation
            item = self.operation(item)
            # gets bored
            if self.inspection_worry:
                item = int(item / 3)
            # apply test
            if self.test(item):
                # add true monkey
                output.append((self.true_monkey, item))
            # else
            else:
                # add false monkey
                output.append((self.false_monkey, item))
        # empty monkey items
        self.items = []
        # return output
        return output


def monkey_chase(n: int, file_path: str, inspection_worry: bool = True) -> int:
    """
    runs monkey chase
    returns the product of the number of inspections
    of the two most active monkeys (monkey business level)

    Args:
        n (int): integer
        file_path (str): file path

    Returns:
        int: monkey business level
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # parse monkeys
    monkeys = [
        Monkey(lines[i : i + 6], inspection_worry=inspection_worry)
        for i in range(0, len(lines), 7)
    ]
    # get LCM of monkey divisors
    lcm = reduce(
        lambda a, b: a * b // gcd(a, b), [monkey.divisor for monkey in monkeys]
    )
    # for n rounds
    for _ in range(n):
        # for each cheeky monkey
        for monkey in monkeys:
            # monkey does their round
            round_output = monkey.round()
            # for each monkey item pair
            for monkey, item in round_output:
                # throw item (mod LCM) to that monkey
                monkeys[monkey].items.append(item % lcm)
    # sort the monkeys by number of inspection counts
    monkeys = sorted(monkeys, key=lambda x: x.inspection_count)
    # return product of largest two
    return monkeys[-2].inspection_count * monkeys[-1].inspection_count


def part_one(file_path: str) -> int:
    """
    runs monkey chase for 20 rounds

    Args:
        file_path (str): input file

    Returns:
        int: monkey business
    """

    return monkey_chase(20, file_path)


def part_two(file_path: str) -> int:
    """
    runs monkey chase for 10_000 rounds

    Args:
        file_path (str): input file

    Returns:
        int: monkey business
    """

    return monkey_chase(10000, file_path, inspection_worry=False)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_11.txt"))
    print(part_two("aoc/inputs/day_11.txt"))
