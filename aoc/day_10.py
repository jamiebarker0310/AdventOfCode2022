class ClockCircuit:
    def __init__(
        self, cycle_checks: list = [], drawing: bool = False, line_length: int = None
    ) -> None:
        """
        initialise clock circuit

        Args:
            cycle_checks (list, optional): _description_. Defaults to [].
            drawing (bool, optional): _description_. Defaults to False.
            line_length (int, optional): _description_. Defaults to None.
        """
        # intialise sprite
        self.x = 1
        # initialise cycles
        self.cycles = 0
        # initialise cycle checks
        self.cycle_checks = cycle_checks
        # initialise cycle values for part 1
        self.cycle_values = {}
        # whether to output drawing (part 2)
        self.drawing = drawing
        # if we are drawing
        if drawing:
            # intialise pixels
            self.pixels = []
            # set length of line of drawing
            self.line_length = line_length

    def add_cycle(self):
        """
        increment cycle
        """
        # if drawing
        if self.drawing:
            # check is sprite is near CRT
            if abs(self.cycles % self.line_length - self.x) <= 1:
                # if it is then draw
                pixel = "#"
            # else
            else:
                # don't draw
                pixel = "."
            # append pixel to pixels
            self.pixels.append(pixel)
        # increment cycle
        self.cycles += 1
        # if cycle in cycles to check
        if self.cycles in self.cycle_checks:
            # add cycle value to dictionary
            self.cycle_values[self.cycles] = self.x

    def add_x(self, x: int, n_cycles: int = 2):
        """
        move sprite by x amount

        Args:
            x (int): distance to move
            n_cycles (int, optional): how long moving x takes. Defaults to 2.
        """
        # for how many cycles it takes
        for _ in range(n_cycles):
            # increase cycles
            self.add_cycle()
        # increase x
        self.x += x

    def noop(self):
        """
        increment cycle
        """
        self.add_cycle()

    def parse_instructions(self, lines: list):
        """parse instructions

        Args:
            lines (list): from read lines object
        """
        # for each line
        for line in lines:
            # if noop
            if line.strip() == "noop":
                # then noop
                self.noop()
            else:
                # parse value
                value = int(line.strip().split(" ")[-1])
                # add x
                self.add_x(value)

    def draw(self) -> str:
        """
        draw image outputted

        Returns:
            str: string of outputted image
        """

        return "\n".join(["".join(self.pixels[i : i + 40]) for i in range(0, 240, 40)])


def part_one(file_path: str) -> int:
    """
    calculate sum of signal strengths at
    20, 60, 100, 140, 180, 220

    Args:
        file_path (str): input file

    Returns:
        int: signal strength
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    clock_circuit = ClockCircuit(cycle_checks=[20, 60, 100, 140, 180, 220])
    clock_circuit.parse_instructions(lines)

    return sum([key * value for key, value in clock_circuit.cycle_values.items()])


def part_two(file_path: str) -> str:
    """
    draw outputted signal

    Args:
        file_path (str): input file

    Returns:
        str: file path
    """
    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # initialise clock circuit
    clock_circuit = ClockCircuit(drawing=True, line_length=40)
    # parse instructions
    clock_circuit.parse_instructions(lines)
    # draw image
    return clock_circuit.draw()


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_10.txt"))
    print(part_two("aoc/inputs/day_10.txt"))
