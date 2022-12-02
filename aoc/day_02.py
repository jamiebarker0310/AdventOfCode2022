def part_one(file_path: str) -> int:
    """
    Assuming
    A, X are Rock
    B, Y are Paper
    C, Z are Scissors

    play out games and score as
    6 for win, 3 for draw, 0 for loss

    also score:
        - 1 for Rock
        - 2 for Paper
        - 3 for Scissors
    Args:
        file_path (str): input filepath

    Returns:
        int: score of all games
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # map to values
    a_map = {"A": 0, "B": 1, "C": 2}
    b_map = {"X": 0, "Y": 1, "Z": 2}

    # initialise score
    score = 0
    for line in lines:
        a, b = line.split(" ")
        a = a_map[a.strip()]
        b = b_map[b.strip()]

        score += score_game(a, b)
    return score


def score_game(a: int, b: int) -> int:
    """scores a game for b

    Args:
        a (int): integer representing a's move
        b (int): integer representing b's move

    Returns:
        int: b's score
    """

    return result_score(a, b) + b + 1


def calculate_move(a: int, r: int) -> int:

    return (a + r + 2) % 3


def result_score(a: int, b: int) -> int:
    """score a game of rock paper scissors using a nifty formula

    Args:
        a (int): integer representing a's move
        b (int): integer representing b's move

    Returns:
        int: game score
    """

    return ((1 + (b - a)) % 3) * 3


def part_two(file_path: str):
    """
    takes the opponents move and the result
    calculates the required move
    calculates the score
    sums the total

    Args:
        file_path (str): input filepath

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()
    # map values
    a_map = {"A": 0, "B": 1, "C": 2}
    r_map = {"X": 0, "Y": 1, "Z": 2}

    # initialise score
    score = 0
    for line in lines:
        # pass and map moves
        a, r = line.split(" ")
        a = a_map[a.strip()]
        r = r_map[r.strip()]
        # calulate move
        b = calculate_move(a, r)
        # add to scores
        score += r * 3
        score += b + 1

    return score


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_02.txt"))
    print(part_two("aoc/inputs/day_02.txt"))
