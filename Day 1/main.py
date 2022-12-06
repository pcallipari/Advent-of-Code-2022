from typing import List
import time

input_file = "test_input.txt"
# input_file = "my_input.txt"


def top_three(new_value: int, current_top: List[int]):
    for index, value in enumerate(current_top):
        if new_value > value:
            current_top.insert(index, new_value)
            break

    return current_top[0:3]


def main():
    with open(input_file, "r") as f:
        # current_elf = 0
        # max_index = -1
        # max_total = 0
        current_total = 0
        current_top = [0, 0, 0]
        for line in f.readlines():
            if line == "\n":
                # if current_total > max_total:
                if current_total > current_top[2]:
                    current_top = top_three(current_total, current_top)
                    # max_total = current_total
                    # max_index = current_elf
                # current_elf += 1
                current_total = 0
                continue
            current_total += int(line)

        # print(
        #     f"The maximum calories was elf number {max_index+ 1} with total {max_total}"
        # )

        if current_total > current_top[2]:
            current_top = top_three(current_total, current_top)

        print(
            f"The top three values are {current_top}. The total is {sum(current_top)}."
        )


def new_main():
    with open(input_file, "r") as f:
        raw_input = f.read()

    split_elves = raw_input.split("\n\n")

    def get_total(elf_lines: str) -> int:
        str_array = elf_lines.split("\n")
        int_array = map(int, str_array)
        total = sum(int_array)
        return total

    total_list = list(map(get_total, split_elves))
    total_list.sort(reverse=True)
    print(f"The top three are {total_list[0:3]}, the total is {sum(total_list[0:3])}")


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    diff = time.perf_counter() - start
    print(f"The first way has a time of {diff}")
    start = time.perf_counter()
    new_main()
    diff = time.perf_counter() - start
    print(f"The second way has a time of {diff}")
