class File:
    def __init__(self, parent, filename, size):
        self.parent = parent
        self.filename = filename
        self.size = size

    def __repr__(self) -> str:
        return self.filename


class Directory:
    def __init__(self, parent=None, directory_name=None):
        self.parent = parent
        self.children = {}
        self.name = directory_name

    def __repr__(self) -> str:
        return self.name

    def add_child_file(self, filename: str, size: int):
        """
        add file to children dict

        Args:
            filename (str): file name
            size (int): file size
        """
        self.children[filename] = File(parent=self, filename=filename, size=size)

    def add_child_directory(
        self,
        directory_name: str,
    ):
        """
        add directory to children dict

        Args:
            directory_name (str): name of directory
        """
        self.children[directory_name] = Directory(
            parent=self, directory_name=directory_name
        )

    @property
    def size(self):
        # get sum of all files inside directory
        return sum([child.size for child in self.children.values()])

    @property
    def outermost_parent(self):
        # keeps looking for a files parent until there isn't one
        directory = self
        while directory.parent is not None:
            directory = directory.parent
        return directory


def parse_directory(lines: str) -> Directory:
    """
    parse input to Directory file structure object

    Args:
        lines (str): input

    Returns:
        Directory: outermost directory created
    """
    # initialise directory
    directory = Directory()
    # for each line
    for line in lines:
        # parse arguments
        args = line.strip().split(" ")
        # if it's a command
        if args[0] == "$":
            # if it's change directory
            if args[1] == "cd":
                # the argument is "/"
                if args[2] == "/":
                    # set directory to outermost parent
                    directory = directory.outermost_parent
                # if the argument is ".."
                elif args[2] == "..":
                    # set directory to parent
                    directory = directory.parent
                else:
                    # navigate to child directory
                    directory = directory.children[args[2]]
            # if ls do nothing
            elif args[1] == "ls":
                continue
        # if object is directory
        elif args[0] == "dir":
            # add directory
            directory.add_child_directory(args[1])
        # else it is a file
        else:
            # add file
            directory.add_child_file(filename=args[1], size=int(args[0]))
    # return directory at outermost parent
    return directory.outermost_parent


def traverse_files(directory: Directory, sizes: list) -> list:
    """
    recursive function to get all directory sizes

    Args:
        directory (Directory): directory to parse
        sizes (list): list of file sizes

    Returns:
        sizes: list of file sizes
    """
    # append file size
    sizes.append(directory.size)
    # for each child
    for child in directory.children.values():
        # if it's a directory
        if isinstance(child, Directory):
            # traverse that directory
            traverse_files(child, sizes)
    # return sizes
    return sizes


def part_one(file_path: str) -> int:
    """
    returns the sum of the size of all directories smaller than 100000

    Args:
        file_path (str): filepath

    Returns:
        int: file size sum
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    # get directory
    directory = parse_directory(lines)
    # return sum of all directories smaller than 100000
    return sum([size for size in traverse_files(directory, []) if size < 100000])


def part_two(file_path: str) -> int:
    """
    returns the smallest directory size to create enough space
    for update

    Args:
        file_path (str): filepath

    Returns:
        int: directory size
    """
    # read files
    with open(file_path) as f:
        lines = f.readlines()
    # get directory
    directory = parse_directory(lines)
    # set spaces sizes
    total_disk_space = 70000000
    unused_space_req = 30000000
    # get all file sizes
    file_sizes = [size for size in traverse_files(directory, [])]
    # calculate file space
    file_space = total_disk_space - max(file_sizes)
    # calculate space requirement
    space_req = unused_space_req - file_space
    # return minimum size bigger than space requirement
    return min([size for size in file_sizes if size > space_req])


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_07.txt"))
    print(part_two("aoc/inputs/day_07.txt"))
