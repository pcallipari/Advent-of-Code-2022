import re


def parse_input(filename: str):
    point_pattern = re.compile(r"(\d+),(\d+)")
    with open(filename, "r") as f:
        output = []
        for line in f.read().splitlines():
            points = [
                (int(match.group(1)), int(match.group(2)))
                for match in point_pattern.finditer(line)
            ]
            output.append(points)
    return output


def get_grid_bounds(rock_paths):
    points = []
    for path in rock_paths:
        points.extend(path)
    start_x, start_y = points[0]
    min_x = start_x
    max_x = start_x
    min_y = start_y
    max_y = start_y

    for x, y in points[1:]:
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        min_y = min(y, min_y)
        max_y = max(y, max_y)

    return (min_x, min_y), (max_x, max_y)


# input_filename = r"Day 14/test_input.txt"
input_filename = r"Day 14/my_input.txt"


def get_grid_pos(x, y, min_pos):
    return x - min_pos[0], y - min_pos[1]


def add_rocks(path, grid, min_pos):
    current_pos = path[0]
    for pos in path[1:]:
        min_x = min(current_pos[0], pos[0])
        max_x = max(current_pos[0], pos[0])
        min_y = min(current_pos[1], pos[1])
        max_y = max(current_pos[1], pos[1])
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                ix, iy = get_grid_pos(x, y, min_pos)
                grid[iy][ix] = "#"
        current_pos = pos
    return grid


def get_sand_drop(sand_pos, grid, min_pos):
    x, y = sand_pos[0]
    ix, iy = get_grid_pos(x, y, min_pos)
    while True:
        if grid[iy + 1][ix] == ".":
            iy += 1
        elif grid[iy + 1][ix - 1] == ".":
            iy += 1
            ix -= 1
        elif grid[iy + 1][ix + 1] == ".":
            iy += 1
            ix += 1
        else:
            break
    return ix, iy


def print_grid(grid):
    for line in grid:
        print("".join(line))


def main_part1():
    rock_paths = parse_input(input_filename)
    sand_pos = [(500, 0)]
    min_pos, max_pos = get_grid_bounds([*rock_paths, sand_pos])
    # Need to add +1 to count for the starting position
    # e.g 400-400 would have a width of 1.
    x_range = max_pos[0] - min_pos[0] + 1
    y_range = max_pos[1] - min_pos[1] + 1
    grid = [["." for _ in range(x_range)] for _ in range(y_range)]
    # print(len(grid[0]))
    # print(len(grid))
    for path in rock_paths:
        grid = add_rocks(path, grid, min_pos)
    # print_grid(grid)
    sand_dropped = 0
    try:
        while True:
            x, y = get_sand_drop(sand_pos, grid, min_pos)
            grid[y][x] = "o"
            sand_dropped += 1
    except IndexError:
        print(f"The total sand dropped is: {sand_dropped}")


def main_part2():
    rock_paths = parse_input(input_filename)
    sand_pos = [(500, 0)]
    min_pos, max_pos = get_grid_bounds([*rock_paths, sand_pos])
    floor_y = max_pos[1] + 2
    floor_path = [(min_pos[0], floor_y), (max_pos[0], floor_y)]
    rock_paths.append(floor_path)
    # Recalculate for the floor
    min_pos, max_pos = get_grid_bounds([*rock_paths, sand_pos])

    grid = create_grid_part2(min_pos, max_pos)
    # Adding the rocks
    for path in rock_paths:
        add_rocks_part2(path, grid)
    print_grid_part2(grid)
    dropped_sand = 0
    while grid[sand_pos[0][0]][sand_pos[0][1]] != "o":
        add_sand(sand_pos, grid)
        dropped_sand += 1
    print(f"The total sand dropped is {dropped_sand}")


def create_grid_part2(min_pos, max_pos):
    grid = {}

    for x in range(min_pos[0], max_pos[0] + 1):
        line = {}
        for y in range(min_pos[1], max_pos[1] + 1):
            line[y] = "."
        grid[x] = line

    return grid


def add_rocks_part2(path, grid):
    current_pos = path[0]
    for pos in path[1:]:
        min_x = min(current_pos[0], pos[0])
        max_x = max(current_pos[0], pos[0])
        min_y = min(current_pos[1], pos[1])
        max_y = max(current_pos[1], pos[1])
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                grid[x][y] = "#"
        current_pos = pos
    return grid


def add_sand(sand_pos, grid):
    x, y = sand_pos[0]
    # ix, iy = get_grid_pos(x, y, min_pos)
    while True:
        if x - 1 not in grid or x + 1 not in grid:
            y_range = grid[500].keys()
            floor_y = max(y_range)
            if x - 1 not in grid:
                grid[x - 1] = {iy: "." for iy in y_range}
                grid[x - 1][floor_y] = "#"
            elif x + 1 not in grid:
                grid[x + 1] = {iy: "." for iy in y_range}
                grid[x + 1][floor_y] = "#"

        if grid[x][y + 1] == ".":
            y += 1
        elif grid[x - 1][y + 1] == ".":
            y += 1
            x -= 1
        elif grid[x + 1][y + 1] == ".":
            y += 1
            x += 1
        else:
            break

    grid[x][y] = "o"


def print_grid_part2(grid):
    x_values = grid.keys()
    y_values = grid[500].keys()
    for y in y_values:
        line = ""
        for x in x_values:
            line += grid[x][y]
        print(line)


if __name__ == "__main__":
    main_part2()
