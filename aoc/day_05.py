def part_one(file_path: str) -> str:
    """
    parses initial crates and moves
    then moves the stack by popping and appending

    Args:
        file_path (str): file input
    Returns:
        str: top crates at the end of all moves
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    # get stacks and moves
    stacks = parse_stacks(lines)
    moves = parse_moves(lines)

    # for each move
    for move in moves:
        # get n moves, stack to move from and to
        n, a, b = move
        # for each move
        for _ in range(n):
            # stack the crate on the new stack
            stacks[b - 1].append(stacks[a - 1].pop())
    # return strings at the top
    return "".join([stack.pop() for stack in stacks])


def part_two(file_path: str):
    """
    parses initial crates and moves
    then moves the stack by popping, reversing and appending

    Args:
        file_path (str): file input

    Returns:
        str: top crates at the end of all moves
    """
    # read file
    with open(file_path) as f:
        lines = f.readlines()

    # parse stacks and moves
    stacks = parse_stacks(lines)
    moves = parse_moves(lines)

    # for each mvoe
    for move in moves:
        # get n moves, stack to move from and to
        n, a, b = move
        # initialise crates
        crates = []
        # for each move
        for _ in range(n):
            # get all the crates
            crates.append(stacks[a - 1].pop())
        # for crate in reversed crate
        for crate in crates[::-1]:
            # stick the crate on
            stacks[b - 1].append(crate)
    # return strings at the top
    return "".join([stack.pop() for stack in stacks])


def parse_stacks(lines):

    grid = lines[: lines.index("\n") - 1]
    grid = [[line[i] for i in range(1, len(line), 4)] for line in grid]

    stacks = [[] for i in grid[0]]
    for row in grid[::-1]:
        for i, column in enumerate(row):
            if column != " ":
                stacks[i].append(column)

    return stacks


def parse_moves(lines):

    moves = [
        [int(word.strip()) for word in line.strip().split(" ") if word.isnumeric()]
        for line in lines[lines.index("\n") + 1 :]
    ]

    return moves


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_05.txt"))
    print(part_two("aoc/inputs/day_05.txt"))
