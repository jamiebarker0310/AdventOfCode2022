import json
from functools import cmp_to_key


def compare_lists(l1: list, l2: list) -> bool:
    """
    compares list with the following criteria
    If both values are integers, the lower integer should come first.
    If the left integer is lower than the right integer,
        the inputs are in the right order.
    If the left integer is higher than the right integer,
        the inputs are not in the right order.
    Otherwise, the inputs are the same integer;
        continue checking the next part of the input.

    If both values are lists,
        compare the first value of each list,
        then the second value,
        and so on.

    If the left list runs out of items first,
        the inputs are in the right order.
    If the right list runs out of items first,
        the inputs are not in the right order.

    If the lists are the same length and no comparison makes a decision about the order,
        continue checking the next part of the input.

    If exactly one value is an integer,
        convert the integer to a list which contains that integer as its only value,
        then retry the comparison.

    Args:
        l1 (list): list which should be lower
        l2 (list): list which should be higher

    Returns:
        bool: whether the list is sorted
    """
    # if both elements are ints
    if isinstance(l1, int) and isinstance(l2, int):
        # if in right order return true
        if l1 < l2:
            return True
        # if equal return nothing
        if l1 == l2:
            return None
        # if in wrong order return false
        else:
            return False
    # if both elements are a list
    if isinstance(l1, list) and isinstance(l2, list):
        # initialise result and index
        result = None
        i = 0
        # whiel result is null
        while result is None:
            # Nothing if at the end of both lists
            if i == len(l1) and i == len(l2):
                return None
            # True if at the end of l1
            if i == len(l1):
                return True
            # False if at the end of l2
            if i == len(l2):
                return False
            # else, result is the comparison of two items
            result = compare_lists(l1[i], l2[i])
            # look at the next item
            i += 1
        # return the result
        return result

    # if l1 is an integer and l2 a list
    if isinstance(l1, int) and isinstance(l2, list):
        # compare a list containing l1 and l2
        return compare_lists([l1], l2)
    # if l1 is a list and l2 an integer
    if isinstance(l1, list) and isinstance(l2, int):
        # compare l1 and a list containing l2
        return compare_lists(l1, [l2])


def part_one(file_path: str) -> int:
    """
    returns the sum of the indexes of list
    pairs in the right order

    Args:
        file_path (str): input file

    Returns:
        int: sum of ordered indexes
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # initialise total
    total = 0
    # for each line pair triple
    for i in range(0, len(lines), 3):
        # load l1 and l2
        l1 = json.loads(lines[i].strip())
        l2 = json.loads(lines[i + 1].strip())
        # if lists sorted
        if compare_lists(l1, l2):
            # add index (starting at 1) to total
            total += (i // 3) + 1
    # return total
    return total


def sort_compare(l1: list, l2: list) -> int:
    """
    maps compare_lists to integers for sorting
    a list by

    Args:
        l1 (list): should be lower list
        l2 (list): should be higher list

    Returns:
        int: _description_
    """
    # if in order
    if compare_lists(l1, l2):
        # return -1
        return -1
    # else return 1
    else:
        return 1


def part_two(file_path: str) -> int:
    """
    inserts [[2]], [[6]] into list of packets
    sorts all packets
    returns products of indices of [[2]] and [[6]]
    in sorted list

    Args:
        file_path (str): input file

    Returns:
        int: product of indices of [[2]] and [[6]]
    """
    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # initialise packets with [[2]] and [[6]]
    packets = [[[2]], [[6]]]
    # for all lines
    for i in range(0, len(lines), 3):
        # append packet to packets
        packets.append(json.loads(lines[i].strip()))
        packets.append(json.loads(lines[i + 1].strip()))
    # sort packets according to comparison
    packets.sort(key=cmp_to_key(sort_compare))
    # return product of both packets
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_13.txt"))
    print(part_two("aoc/inputs/day_13.txt"))
