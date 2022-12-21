import re


def load_monkeys(filename: str):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        commands = []
        values = {}
        for line in lines:
            name, command = line.split(":")
            command = command.strip()
            number_match = re.search(r"\d+", command)
            if number_match is None:
                a, operator, b = command.split(" ")
                commands.append((name, a, b, operator))
            else:
                value = int(command)
                values[name] = value
    return values, commands


# input_filename = r"Day 21/test_input.txt"
input_filename = r"Day 21/my_input.txt"


def main_part1():
    # Testing my input
    values, commands = load_monkeys(input_filename)
    # print("The already given values are:")
    # for name, value in values.items():
    #     print(f"{name}: {value}")
    # print("The commands are:")
    # for name, command in commands.items():
    #     print(f"{name}: {command}")

    while commands:
        for command in commands:
            name, a, b, operator = command
            if not a in values or not b in values:
                continue
            values[name] = eval(f"values['{a}'] {operator} values['{b}']")
            commands.remove(command)

    print(f"The value for root is {values['root']}")


if __name__ == "__main__":
    main_part1()
