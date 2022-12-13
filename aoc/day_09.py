class Knot:
    def __init__(self, child=None) -> None:
        # initialise empty position
        self.x = 0
        self.y = 0
        # set child
        self.child = child
        # initialise moved places
        self.moved_places = set()
        # add to moved places
        self.moved_places.add((self.x, self.y))

    def move(self, x: int = 0, y: int = 0):
        """
        move position
        update children
        add position to moved places

        Args:
            x (int, optional): how far to move x. Defaults to 0.
            y (int, optional): how far to move y . Defaults to 0.
        """
        # adjust x and y
        self.x += x
        self.y += y
        # update child
        self.update_child()
        # add position to moved places
        self.moved_places.add((self.x, self.y))

    def update_child(self):
        """
        update child position
        """
        # if there is no child, do nothing
        if self.child is None:
            pass
        # otherwise
        else:
            # calculate the differences
            x_diff = self.x - self.child.x
            y_diff = self.y - self.child.y
            # if both are 1 or less away then it is adjacent
            if max(abs(x_diff), abs(y_diff)) <= 1:
                # do not change position
                pass
            # else
            else:
                # normalise difference
                x_diff = normalise_direction(x_diff)
                y_diff = normalise_direction(y_diff)
                # move child
                self.child.move(x=x_diff, y=y_diff)


def normalise_direction(x: int) -> int:
    """
    sign of number

    Args:
        x (int): integer

    Returns:
        int: sign of integer
    """
    try:
        return x / abs(x)
    except ZeroDivisionError:
        return 0


def simulation(lines: list, n: int) -> int:
    """
    runs a simulation of moving rope for n nots

    Args:
        lines (list): rope moves
        n (int): number of knots

    Returns:
        int: run simulation
    """
    # initalise empty head
    head = None
    # for n in number of knots
    for _ in range(n):
        # add head to chain
        head = Knot(child=head)
    # for each move
    for line in lines:
        # parse the direction and distance
        direction, distance = line.strip().split(" ")
        # for each move in the direction
        for _ in range(int(distance)):
            # move object in that direction
            if direction == "R":
                head.move(x=1)
            elif direction == "L":
                head.move(x=-1)
            elif direction == "U":
                head.move(y=1)
            elif direction == "D":
                head.move(y=-1)
    # while the head has a child
    while head.child is not None:
        # the head becomes the child
        head = head.child
    # return number of moved places of final knot
    return len(head.moved_places)


def part_one(file_path: str) -> int:
    """
    2 knotted string simulation

    Args:
        file_path (str): input file

    Returns:
        int: number of distinct positions final knot has moved to
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # run simulation
    return simulation(lines, n=2)


def part_two(file_path: str) -> int:
    """
    10 knot simulation

    Args:
        file_path (str): filepath

    Returns:
        int: number of distinct positions final knot has moved to
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # run simulation
    return simulation(lines, n=10)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_09.txt"))
    print(part_two("aoc/inputs/day_09.txt"))
