from typing import Tuple, List
from collections import deque

input_filename = r"Day 12/my_input.txt"


def main_part1():
    with open(input_filename, "r") as f:
        input_grid = [[*line] for line in f.read().splitlines()]
    # print(input_grid)
    # start_pos = get_start_positon(input_grid)
    start_pos = get_end_positon(input_grid)
    distance_grid = [
        # Set default distance to arbitary large number.
        [99999 for _ in range(len(input_grid[0]))]
        for _ in range(len(input_grid))
    ]
    distance_grid[start_pos[0]][start_pos[1]] = 0
    check_queue = deque([(1, pos) for pos in get_possible_moves(start_pos, input_grid)])
    while check_queue:
        current_distance, current_pos = check_queue.pop()
        current_distance += 1

        # Part 2
        # if input_grid[current_pos[0]][current_pos[1]] == "a":
        #     print(f"Shortest distance to 'a': {current_distance}")
        #     break

        # Continue if grid distance is already lower.
        if distance_grid[current_pos[0]][current_pos[1]] <= current_distance:
            continue
        distance_grid[current_pos[0]][current_pos[1]] = current_distance
        for next_move in get_possible_moves(current_pos, input_grid):
            check_queue.append((current_distance, next_move))
    # Get the end value
    # end_pos = get_end_positon(input_grid)
    # print(f"The shortest path is at distance: {distance_grid[end_pos[0]][end_pos[1]]}")

    # part 2
    min_dist = 99999
    for i, line in enumerate(input_grid):
        for j, char in enumerate(line):
            if char == "a":
                min_dist = min(min_dist, distance_grid[i][j])
    print(f"Min dist {min_dist}")


def get_start_positon(input_grid: List[List[str]]) -> Tuple[int, int]:
    for y, line in enumerate(input_grid):
        for x, char in enumerate(line):
            if char == "S":
                return y, x


def get_end_positon(input_grid: List[List[str]]):
    for y, line in enumerate(input_grid):
        for x, char in enumerate(line):
            if char == "E":
                return y, x


def get_possible_moves(
    position: Tuple[int, int], input_grid: List[List[str]]
) -> List[Tuple[int, int]]:

    current_height = get_height(input_grid[position[0]][position[1]])
    possible_locations = []
    for xi, yi in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x = position[1] + xi
        y = position[0] + yi
        max_x = len(input_grid[0])
        max_y = len(input_grid)
        if x < 0 or y < 0 or x >= max_x or y >= max_y:
            continue
        height = get_height(input_grid[y][x])
        # if height - current_height <= 1:
        if height - current_height >= -1:
            possible_locations.append((y, x))
    return possible_locations


def get_height(char: str) -> int:
    if char == "S":
        return ord("a") - 97
    elif char == "E":
        return ord("z") - 97
    else:
        return ord(char) - 97


if __name__ == "__main__":
    main_part1()
