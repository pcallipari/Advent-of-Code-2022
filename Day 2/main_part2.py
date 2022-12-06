from enum import Enum

input_filename = r"Day 2\my_input.txt"


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"


def get_opp_choice(char: str):
    if char == "A":
        return Choice.ROCK
    elif char == "B":
        return Choice.PAPER
    elif char == "C":
        return Choice.SCISSORS
    else:
        return ValueError


def get_points(opp: str, cond: str):
    # opp, mine = input_string.split(" ")

    opp_choice = get_opp_choice(opp)
    outcome = Outcome(cond)

    if outcome is Outcome.LOSE:
        if opp_choice is Choice.ROCK:
            return 0 + 3
        elif opp_choice is Choice.PAPER:
            return 0 + 1
        elif opp_choice is Choice.SCISSORS:
            return 0 + 2
    elif outcome is Outcome.DRAW:
        if opp_choice is Choice.ROCK:
            return 3 + 1
        elif opp_choice is Choice.PAPER:
            return 3 + 2
        elif opp_choice is Choice.SCISSORS:
            return 3 + 3
    elif outcome is Outcome.WIN:
        if opp_choice is Choice.ROCK:
            return 6 + 2
        elif opp_choice is Choice.PAPER:
            return 6 + 3
        elif opp_choice is Choice.SCISSORS:
            return 6 + 1


def main():
    opp_input = ["A", "B", "C"]
    win_conditions = ["X", "Y", "Z"]

    point_dict = {}

    for opp_choice in opp_input:
        for win_cond in win_conditions:
            point_dict[f"{opp_choice} {win_cond}"] = get_points(opp_choice, win_cond)

    with open(input_filename, "r") as f:
        points = map(lambda line: point_dict[line], f.read().splitlines())
        print(f"The total points are {sum(points)}")


if __name__ == "__main__":
    main()
