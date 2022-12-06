def get_priority(char: str) -> int:
    if char.islower():
        return ord(char) - 97 + 1
    else:
        return ord(char) - 65 + 27


def get_total_priority(overlap_chars):
    return sum(map(get_priority, overlap_chars))


def split_compartments(input: str):
    half = int(len(input) / 2)
    first = input[:half]
    second = input[half:]
    return first, second


def element_overlap(first: str, second: str):
    first_set = set(first)
    second_set = set(second)
    return first_set.intersection(second_set)


input_file = r"Day 3\my_input.txt"


def main():
    with open(input_file, "r") as f:
        rucksacks = f.read().splitlines()
    split_comps = map(split_compartments, rucksacks)
    overlap_items = map(lambda c: element_overlap(c[0], c[1]), split_comps)
    total = sum(map(get_total_priority, overlap_items))
    print(f"The total is {total}")


if __name__ == "__main__":
    main()
