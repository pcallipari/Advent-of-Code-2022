# input_filename = r"Day 10/test_input.txt"
input_filename = r"Day 10/my_input.txt"


def main_part1():
    with open(input_filename, "r") as f:
        input_lines = f.read().splitlines()

    current_cycle = 0
    X_register = 1

    checkpoints = [20, 60, 100, 140, 180, 220]
    checkpoints.reverse()
    current_sum = 0

    for command in input_lines:
        if command.startswith("noop"):
            current_cycle += 1
            if current_cycle == checkpoints[-1]:
                current_sum += checkpoints.pop() * X_register

        elif command.startswith("addx"):
            if checkpoints[-1] <= current_cycle + 2:
                current_sum += checkpoints.pop() * X_register

            add_value = int(command.split(" ")[1])
            X_register += add_value
            current_cycle += 2

        if len(checkpoints) == 0:
            break

    print(f"The final sum is: {current_sum}")


def main_part2():
    with open(input_filename, "r") as f:
        input_lines = f.read().splitlines()
    # Iterating over rows
    current_line = ""
    current_cycle = 0
    sprite_position = 1

    for command in input_lines:
        if command.startswith("noop"):
            current_line = process_frame(current_line, current_cycle, sprite_position)
            current_cycle += 1
        elif command.startswith("addx"):
            current_line = process_frame(current_line, current_cycle, sprite_position)
            current_cycle += 1
            current_line = process_frame(current_line, current_cycle, sprite_position)
            current_cycle += 1
            add_value = int(command.split(" ")[1])
            sprite_position += add_value
    print_crt(current_line)


def process_frame(current_line: str, cycle: int, sprite_pos: int):
    cycle = cycle % 40
    if sprite_visible(cycle, sprite_pos):
        return current_line + "#"
    return current_line + "."


def print_crt(current_line: str):
    max_len = len(current_line)
    total_lines = int(max_len / 40)
    for i in range(0, total_lines * 40, 40):
        print(current_line[i : i + 40])


def sprite_visible(current_pixel: int, sprite_pos: int) -> bool:
    diff = current_pixel - sprite_pos
    if diff == -1 or diff == 0 or diff == 1:
        return True
    return False


if __name__ == "__main__":
    main_part2()
