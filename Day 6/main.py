# input_file = r"Day 6\test_input.txt"
input_file = r"Day 6\my_input.txt"


def check_doubles(input_list):
    for index, value in enumerate(input_list, start=1):
        if value in input_list[index:]:
            return False
    return True


def main_part1():
    with open(input_file, "r") as f:

        temp_array = [*f.read(4)]
        i = 5
        while True:
            next_character = f.read(1)
            temp_array = temp_array[1:]
            temp_array.append(next_character)
            if check_doubles(temp_array):
                print(f"The first marker point is at i={i}.")
                break

            i += 1


def main_part2():
    with open(input_file, "r") as f:

        temp_array = [*f.read(14)]
        i = 15
        while True:
            next_character = f.read(1)
            temp_array = temp_array[1:]
            temp_array.append(next_character)
            if check_doubles(temp_array):
                print(f"The first message point is at i={i}.")
                break

            i += 1


if __name__ == "__main__":
    main_part2()
