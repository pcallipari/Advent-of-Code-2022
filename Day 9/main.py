import numpy as np


directions = {
    b"R": np.array([0, 1]),
    b"L": np.array([0, -1]),
    b"U": np.array([1, 0]),
    b"D": np.array([-1, 0]),
}


def main_part1():
    # with open(r"Day 9/test_input.txt", "r") as f:
    #     raw_input = f.read()
    # input_pattern = re.compile(r"([A-Z]) (\d)\n")
    # commands = [(i[1], int(i[2])) for i in input_pattern.finditer(raw_input)]
    # print(commands)
    # input_filename = r"Day 9/test_input.txt"
    input_filename = r"Day 9/my_input.txt"
    commands = np.loadtxt(
        input_filename, dtype=[("direction", "S1"), ("amount", "i4")], delimiter=" "
    )

    head_pos = np.array([0, 0])
    last_pos = np.array([0, 0])
    tail_pos = np.array([0, 0])
    visted_locations = set([(0, 0)])

    for command in commands:
        print(command)
        current_direction = directions[command[0]]
        for _ in range(command[1]):
            last_pos = head_pos
            head_pos = head_pos + current_direction
            if is_touching(head_pos, tail_pos):
                continue
            tail_pos = last_pos
            visted_locations.add((tail_pos[0], tail_pos[1]))
            # print(f"Tail position: {tail_pos[0]}, {tail_pos[1]}")

    print(visted_locations)
    print(len(visted_locations))


def is_touching(head_pos: np.ndarray, tail_pos: np.ndarray):
    diff = np.abs(tail_pos - head_pos)
    if np.max(diff) <= 1:
        return True
    return False


if __name__ == "__main__":
    main_part1()
