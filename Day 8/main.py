# input_file = r"Day 8\test_input.txt"
input_file = r"Day 8\my_input.txt"


def main_part1():
    input_array = [[*map(int, line.rstrip())] for line in open(input_file, "r")]

    maxCols = len(input_array[0])
    maxRows = len(input_array)

    total = 0

    for i in range(0, maxCols):
        for j in range(0, maxRows):
            total += isVisible(i, j, input_array)

    print(f"The total is: {total}.")


def isVisible(i: int, j: int, input_array):
    if i == 0 or i == len(input_array[0]) - 1:
        return True
    elif j == 0 or j == len(input_array) - 1:
        return True

    if isVisibleLeft(i, j, input_array):
        return True
    elif isVisibleRight(i, j, input_array):
        return True
    elif isVisibleTop(i, j, input_array):
        return True
    elif isVisibleBottom(i, j, input_array):
        return True

    return False


def isVisibleLeft(i, j, input_array):
    maxValue = max(input_array[i][:j])
    return input_array[i][j] > maxValue


def isVisibleRight(i, j, input_array):
    maxValue = max(input_array[i][j + 1 :])
    return input_array[i][j] > maxValue


def isVisibleTop(i, j, input_array):
    top_column = [input_array[ix][j] for ix in range(0, i)]
    maxValue = max(top_column)
    return input_array[i][j] > maxValue


def isVisibleBottom(i, j, input_array):
    maxRows = len(input_array)
    top_column = [input_array[ix][j] for ix in range(i + 1, maxRows)]
    maxValue = max(top_column)
    return input_array[i][j] > maxValue


# Part 2


def getSightLeft(i, j, input_array):
    sight_total = 0
    for tree in reversed(input_array[i][:j]):
        if tree < input_array[i][j]:
            sight_total += 1
        else:
            sight_total += 1
            break
    # if sight_total == 0:
    #     sight_total += 1
    return sight_total


def getSightRight(i, j, input_array):
    sight_total = 0
    for tree in input_array[i][j + 1 :]:
        if tree < input_array[i][j]:
            sight_total += 1
        else:
            sight_total += 1
            break
    # if sight_total == 0:
    #     sight_total += 1
    return sight_total


def getSightUp(i, j, input_array):
    up_list = [input_array[ix][j] for ix in range(i - 1, -1, -1)]
    sight_total = 0
    for tree in up_list:
        if tree < input_array[i][j]:
            sight_total += 1
        else:
            sight_total += 1
            break
    # if sight_total == 0:
    #     sight_total += 1
    return sight_total


def getSightDown(i, j, input_array):
    max_row = len(input_array)
    down_list = [input_array[ix][j] for ix in range(i + 1, max_row)]
    sight_total = 0
    for tree in down_list:
        if tree < input_array[i][j]:
            sight_total += 1
        else:
            sight_total += 1
            break
    # if sight_total == 0:
    #     sight_total += 1
    return sight_total


def main_part2():
    input_array = [[*map(int, line.rstrip())] for line in open(input_file, "r")]

    maxCols = len(input_array[0])
    maxRows = len(input_array)

    max_score = 0

    for i in range(0, maxCols):
        for j in range(0, maxRows):
            left = getSightLeft(i, j, input_array)
            right = getSightRight(i, j, input_array)
            down = getSightDown(i, j, input_array)
            up = getSightUp(i, j, input_array)
            scen_score = left * right * down * up
            if scen_score > max_score:
                max_score = scen_score

    print(f"The max score is: {max_score}.")


if __name__ == "__main__":
    main_part2()
