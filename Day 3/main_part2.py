from itertools import islice, starmap
import time


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


def element_overlap(*strings: str):
    current_set = None
    for str in strings:
        if current_set is None:
            current_set = set(str)
            continue
        current_set = current_set.intersection(str)
    return current_set


def get_threes(input_list):
    it = iter(input_list)
    while batch := list(islice(it, 3)):
        yield batch


def get_badge(*group_lines):
    element_set = element_overlap(*group_lines)
    if len(element_set) == 1:
        badge_chracter = [i for i in element_set][0]
        return badge_chracter
    else:
        raise ValueError


def get_priority_from_lines(*group_lines):
    elf_badge = get_badge(*group_lines)
    return get_priority(elf_badge)


input_file = r"Day 3\my_input.txt"


def new_main():
    total_priority = 0
    with open(input_file, "r") as f:
        nextline = f.readline().strip("\n")
        i = 0
        current_triple = ["", "", ""]
        while nextline != "":
            current_triple[i] = nextline
            if i == 2:
                badge_sets = list(map(set, current_triple))
                badge_intersection = badge_sets[0]
                badge_intersection = badge_intersection.intersection(badge_sets[1])
                badge_intersection = badge_intersection.intersection(badge_sets[2])
                badge_char = [a for a in badge_intersection][0]
                total_priority += get_priority(badge_char)
            nextline = f.readline().strip("\n")
            i = (i + 1) % 3
    print(f"The total priority is {total_priority}")


def main():
    with open(input_file, "r") as f:
        rucksacks = f.read().splitlines()
    triples = get_threes(rucksacks)
    # elf_badges = starmap(get_badge, triples)
    total = sum(starmap(get_priority_from_lines, triples))
    print(f"The total priority value on the badges is {total}")


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    diff1 = time.perf_counter() - start
    print(f"The time for the first function was {diff1}")

    start = time.perf_counter()
    new_main()
    diff2 = time.perf_counter() - start
    print(f"The time for the second function was {diff2}")
    print(f"{(1 - diff2/diff1) * 100:.2f}% faster than the first method.")
