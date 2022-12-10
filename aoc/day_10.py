class ClockCircuit:
    def __init__(self, cycle_checks=[], drawing=False, line_length=None) -> None:
        self.x = 1
        self.cycles = 0
        self.cycle_checks = cycle_checks
        self.cycle_values = {}
        self.drawing = drawing
        if drawing:
            self.pixels = []
            self.line_length = line_length

    def add_cycle(self):
        if self.drawing:
            if abs(self.cycles % self.line_length - self.x) <= 1:
                pixel = "#"
            else:
                pixel = "."
            self.pixels.append(pixel)
        self.cycles += 1
        if self.cycles in self.cycle_checks:
            if self.drawing:
                self.cycles = 0
            self.cycle_values[self.cycles] = self.x

    def add_x(self, x: int, n_cycles: int = 2):

        for _ in range(n_cycles):
            self.add_cycle()

        self.x += x

    def noop(self):

        self.add_cycle()


def part_one(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    clock_circuit = ClockCircuit(cycle_checks=[20, 60, 100, 140, 180, 220])
    for line in lines:
        if line.strip() == "noop":
            clock_circuit.noop()
        else:
            value = int(line.strip().split(" ")[-1])
            clock_circuit.add_x(value)

    return sum([key * value for key, value in clock_circuit.cycle_values.items()])


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    clock_circuit = ClockCircuit(drawing=True, line_length=40)
    for line in lines:
        if line.strip() == "noop":
            clock_circuit.noop()
        else:
            value = int(line.strip().split(" ")[-1])
            clock_circuit.add_x(value)

    return "\n".join(
        ["".join(clock_circuit.pixels[i : i + 40]) for i in range(0, 240, 40)]
    )


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_10.txt"))
    print(part_two("aoc/inputs/day_10.txt"))
