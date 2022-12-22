import networkx as nx
import itertools


class Valve:
    def __init__(self, line, max_minutes=30):

        line = line.strip()

        self.valve_name = line[6:8]
        self.flow_rate = int("".join(filter(str.isdigit, line)))
        self.adjacent_valves = line.split("valves ")[-1].split(", ")
        self.opened = False
        self.max_minutes = max_minutes


class PathExplorer:
    def __init__(self, file_path, max_minutes=30, starting_point="AA"):

        self.max_minutes = max_minutes
        self.starting_point = starting_point
        self.parse_distances(file_path)

        self.paths = []

    def parse_distances(self, file_path):

        with open(file_path) as f:
            lines = f.readlines()

        valves = [Valve(line) for line in lines]

        G = nx.Graph()
        for valve in valves:
            for adjacent_valve in valve.adjacent_valves:
                G.add_edge(valve.valve_name, adjacent_valve)

        self.flowing_valves = [valve for valve in valves if valve.flow_rate > 0]
        aa_valve = [
            valve for valve in valves if valve.valve_name == self.starting_point
        ]

        self.distances = {}
        for start, end in itertools.permutations(self.flowing_valves + aa_valve, 2):
            distance = nx.shortest_path_length(G, start.valve_name, end.valve_name) + 1
            start = start.valve_name
            end = end.valve_name
            try:
                self.distances[start][end] = distance

            except KeyError:
                self.distances[start] = {end: distance}

    def traverse_graph(self, path, minutes=0):

        foo = True
        for node, distance in self.distances[path[-1]].items():
            if minutes + distance > self.max_minutes:
                continue

            if node in path:
                continue
            else:
                foo = False
                self.traverse_graph(path + [node], minutes + distance)
        if foo:
            self.paths.append(path)

    def calculate_path_flow(self, path):

        flow = 0
        minutes = 1

        for i in range(len(path) - 1):
            start, end = path[i], path[i + 1]
            minutes += self.distances[start][end]
            valve = [valve for valve in self.flowing_valves if valve.valve_name == end][
                0
            ]
            flow += (1 + self.max_minutes - minutes) * valve.flow_rate

        return flow

    def calculate_max_flow(self, start_point=["AA"]):

        self.traverse_graph(start_point)

        return max([self.calculate_path_flow(path) for path in self.paths])


def part_one(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    # read file
    path_explorer = PathExplorer(file_path)

    return path_explorer.calculate_max_flow()


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    return None


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_16.txt"))
    print(part_two("aoc/inputs/day_16.txt"))
