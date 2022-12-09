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


if __name__ == "__main__":
    main_part1()
