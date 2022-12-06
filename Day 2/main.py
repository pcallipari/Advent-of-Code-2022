from enum import Enum

input_filename = r"Day 2\my_input.txt"


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def get_points(mine: str, opp: str):
    # opp, mine = input_string.split(" ")

    if opp == "A":
        opp_choice = Choice.ROCK
    elif opp == "B":
        opp_choice = Choice.PAPER
    elif opp == "C":
        opp_choice = Choice.SCISSORS
    else:
        raise ValueError

    if mine == "X":
        my_choice = Choice.ROCK
    elif mine == "Y":
        my_choice = Choice.PAPER
    elif mine == "Z":
        my_choice = Choice.SCISSORS
    else:
        raise ValueError

    # Win Conditions
    # 6 for a win, 3 for a draw and 0 for a loss
    if my_choice == Choice.ROCK:
        if opp_choice == Choice.ROCK:
            return 3 + 1
        elif opp_choice == Choice.PAPER:
            return 0 + 1
        elif opp_choice == Choice.SCISSORS:
            return 6 + 1
    elif my_choice == Choice.PAPER:
        if opp_choice == Choice.ROCK:
            return 6 + 2
        elif opp_choice == Choice.PAPER:
            return 3 + 2
        elif opp_choice == Choice.SCISSORS:
            return 0 + 2
    elif my_choice == Choice.SCISSORS:
        if opp_choice == Choice.ROCK:
            return 0 + 3
        elif opp_choice == Choice.PAPER:
            return 6 + 3
        elif opp_choice == Choice.SCISSORS:
            return 3 + 3


def main():
    opp_input = ["A", "B", "C"]
    my_inputs = ["X", "Y", "Z"]

    point_dict = {}

    for opp_choice in opp_input:
        for my_choice in my_inputs:
            point_dict[f"{opp_choice} {my_choice}"] = get_points(my_choice, opp_choice)

    with open(input_filename, "r") as f:
        points = map(lambda line: point_dict[line], f.read().splitlines())
        print(f"The total points are {sum(points)}")


if __name__ == "__main__":
    main()
