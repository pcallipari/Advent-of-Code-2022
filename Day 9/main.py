import numpy as np


directions = {
    b"R": np.array([0, 1]),
    b"L": np.array([0, -1]),
    b"U": np.array([1, 0]),
    b"D": np.array([-1, 0]),
}

# input_filename = r"Day 9/test_input2.txt"
input_filename = r"Day 9/my_input.txt"


def main_part1():

    commands = np.loadtxt(
        input_filename, dtype=[("direction", "S1"), ("amount", "i4")], delimiter=" "
    )

    head_pos = np.array([0, 0])
    last_pos = np.array([0, 0])
    tail_pos = np.array([0, 0])
    visted_locations = set([(0, 0)])

    for command in commands:
        current_direction = directions[command[0]]
        for _ in range(command[1]):
            last_pos = head_pos
            head_pos = head_pos + current_direction
            if is_touching(head_pos, tail_pos):
                continue
            tail_pos = last_pos
            visted_locations.add((tail_pos[0], tail_pos[1]))

    print(len(visted_locations))


def is_touching(head_pos: np.ndarray, tail_pos: np.ndarray):
    diff = np.abs(tail_pos - head_pos)
    if np.max(diff) <= 1:
        return True
    return False


def main_part2():
    commands = np.loadtxt(
        input_filename, dtype=[("direction", "S1"), ("amount", "i4")], delimiter=" "
    )
    visited_locations = set([(0, 0)])
    positions = np.array([[0, 0] for _ in range(10)])

    for command in commands:
        current_direction = directions[command[0]]
        for _ in range(command[1]):
            positions[0] = positions[0] + current_direction
            for index, position in enumerate(positions[1:], start=1):
                if is_touching(position, positions[index - 1]):
                    break
                positions[index] = get_new_pos(positions[index - 1], positions[index])
                if index == 9:
                    visited_locations.add((positions[index][0], positions[index][1]))
                # if index == 2:
        # print(f"location: {positions[2][0]}, {positions[2][1]}")
        # show_grid_positions(positions, (-11, 15), (-5, 16))
    # show_grid(visited_locations, (-11, 15), (-8, 18))
    print(len(visited_locations))


def get_new_pos(head_pos: np.ndarray, tail_pos: np.ndarray):
    directions = [
        np.array([0, 1]),
        np.array([0, -1]),
        np.array([1, 0]),
        np.array([-1, 0]),
        np.array([1, 1]),
        np.array([1, -1]),
        np.array([-1, 1]),
        np.array([-1, -1]),
    ]
    for i in directions:
        if is_touching(head_pos + i, tail_pos):
            return head_pos + i
    else:
        raise Exception


from typing import Tuple


def show_grid(
    visted_locations, x_range: Tuple[int, int], y_range: Tuple[int, int]
) -> None:
    for y in range(y_range[1], y_range[0], -1):
        current_line = ""
        for x in range(x_range[0], x_range[1]):
            if (y, x) in visted_locations:
                current_line = current_line + "#"
            else:
                current_line = current_line + "."
        print(current_line)


def show_grid_positions(positions, x_range: Tuple[int, int], y_range: Tuple[int, int]):
    grid = np.full((y_range[1] - y_range[0], x_range[1] - x_range[0]), fill_value=".")

    offset = np.array([y_range[0], x_range[0]])

    grid[-offset[0]][-offset[1]] = "s"

    for index, position in enumerate(reversed(positions)):
        offset_position = position - offset
        if index == 9:
            grid[offset_position[0], offset_position[1]] = "H"
            continue

        grid[offset_position[0], offset_position[1]] = len(positions) - 1 - index

    # Printing
    for line in reversed(grid):
        print("".join(line))
    print()


if __name__ == "__main__":
    main_part2()
