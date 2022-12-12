import networkx as nx
import networkx.exception


def parse_graph(file_path):

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # initialise directed graph
    G = nx.DiGraph()
    # for y co-ordinate, character (reversed to start bottom as 0)
    for y, line in enumerate(lines[::-1]):
        # for x co-ordinate, character
        for x, char in enumerate(line.strip()):
            # if it's the start
            if char == "S":
                start = (x, y)
                char = "a"
            # if it's the end
            if char == "E":
                end = (x, y)
                char = "z"
            # add node
            G.add_node((x, y), height=ord(char) - 97)
    # get all nodes and heights
    heights = nx.get_node_attributes(G, "height")
    for node1, height1 in heights.items():
        # for surrounding nodes
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # if node exists
            try:
                # get 2nd node
                node2 = (node1[0] + x, node1[1] + y)
                # get height of node
                height2 = heights[node2]
                # if it is less than 1 higher
                if height2 - height1 <= 1:
                    # add edge
                    G.add_edge(node1, node2)
            # catch key errors
            except KeyError:
                pass
    # return graph and start and end points
    return G, start, end


def part_one(file_path: str) -> int:
    """
    get shortest path yawn

    Args:
        file_path (str): input file string

    Returns:
        int: length of shortest path
    """
    # get graph, and endpoints
    G, start, end = parse_graph(file_path)
    # get shortest path
    return nx.shortest_path_length(G, source=start, target=end)


def part_two(file_path: str) -> int:
    """
    get shortest path through multiple points yawn

    Args:
        file_path (str): input file string

    Returns:
        int: shortest length between lowest points to end
    """
    # don't need start
    G, _, end = parse_graph(file_path)
    # get heights
    heights = nx.get_node_attributes(G, "height")
    # initialise empty lengths
    lengths = []
    # for start, heigh in dict
    for start, height in heights.items():
        # if it is the lowest height
        if height == 0:
            # try and find the shortest path between that and the end
            try:
                lengths.append(nx.shortest_path_length(G, start, end))
            # catch if no path exists
            except networkx.exception.NetworkXNoPath:
                pass
    # return minimum lengths
    return min(lengths)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_12.txt"))
    print(part_two("aoc/inputs/day_12.txt"))
