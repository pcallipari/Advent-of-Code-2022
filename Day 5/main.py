import re
from collections import deque
from typing import Tuple, List, Deque

# input_file = r"Day 5\test_input.txt"
input_file = r"Day 5\my_input.txt"


def initial_test_state() -> List[Deque]:
    columns = []
    columns.append(deque(["Z", "N"]))
    columns.append(deque(["M", "C", "D"]))
    columns.append(deque(["P"]))
    return columns


def my_initial_state() -> List[Deque]:
    columns = []
    columns.append(deque("TPZCSLQN"))
    columns.append(deque("LPTVHCG"))
    columns.append(deque("DCZF"))
    columns.append(deque("GWTDLMVC"))
    columns.append(deque("PWC"))
    columns.append(deque("PFJDCTSZ"))
    columns.append(deque("VWGBD"))
    columns.append(deque("NJSQHW"))
    columns.append(deque("RCQFSLV"))
    return columns


def parse_moves(input: str) -> Tuple[int, int, int]:
    move_format = re.compile(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)")
    for match in move_format.finditer(input):
        output_values = match.groups()
        yield [int(i) for i in output_values]


def move_blocks(quantity: int, start: int, end: int, columns):
    for _ in range(quantity):
        columns[end].append(columns[start].pop())


def stack_move_blocks(quantity: int, start: int, end: int, columns) -> None:
    temp_stack = Deque()
    for _ in range(quantity):
        temp_stack.append(columns[start].pop())
    for _ in range(quantity):
        columns[end].append(temp_stack.pop())


def get_message(columns):
    message = [col.pop() for col in columns]
    return "".join(message)


def main_part1():
    with open(input_file, "r") as f:
        move_iter = parse_moves(f.read())
    # columns = initial_test_state()
    columns = my_initial_state()
    for move in move_iter:
        # move_blocks(
        #     quantity=move[0], start=move[1] - 1, end=move[2] - 1, columns=columns
        # )
        stack_move_blocks(
            quantity=move[0], start=move[1] - 1, end=move[2] - 1, columns=columns
        )
    print(f"The message is: {get_message(columns)}")


if __name__ == "__main__":
    main_part1()
