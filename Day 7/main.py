input_file = r"Day 7\my_input.txt"


class TreeNode:
    def __init__(self, parent=None):
        self.parent = parent
        self.contents = dict()

    def get_size(self):
        total = 0
        for name, value in self.contents.items():
            if isinstance(value, TreeNode):
                total = total + value.get_size()
            else:
                total = total + value
        return total


def main_part1():
    f = open(input_file, "r")
    raw_input = f.read()
    f.close()

    split_commands = raw_input.split("$")[1:]  # First element is blank

    current_node = TreeNode()
    current_node.contents["/"] = TreeNode()

    answer_total = 0

    # Parsing comamnds
    for command in split_commands:
        command = command.strip()

        if command.startswith("cd"):
            dest = command.split(" ")[1].strip("\n")
            if dest == "..":
                if current_node.get_size() <= 100_000:
                    answer_total = answer_total + current_node.get_size()
                current_node = current_node.parent
                continue

            current_node = current_node.contents[dest]

        elif command.startswith("ls"):
            files = command.split("\n")[1:]  # Ignore the ls
            for file in files:
                if file.startswith("dir"):
                    filename = file.split(" ")[1]
                    current_node.contents[filename] = TreeNode(parent=current_node)
                else:
                    size, filename = file.split(" ")
                    current_node.contents[filename] = int(size)
    print(f"The total is {answer_total}")


if __name__ == "__main__":
    main_part1()
    print("")
