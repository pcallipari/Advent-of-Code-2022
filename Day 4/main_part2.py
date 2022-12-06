from typing import Tuple


def is_subset_of(start1: int, end1: int, start2: int, end2: int) -> bool:
    # This function makes the assumption that start and end are ordered. (start > end)
    # Check that the start of the second set of values is between the start and end of the first
    if start2 >= start1 and start2 <= end1:
        # Check that the end is contained in the start and end of the first
        if end2 >= start1 and end2 <= end1:
            return True

    return False


def overlap_atall(start1: int, end1: int, start2: int, end2: int) -> bool:
    start_in = start2 >= start1 and start2 <= end1
    end_in = end2 >= start1 and end2 <= end1
    return start_in or end_in


def either_overlap(start1: int, end1: int, start2: int, end2: int) -> bool:
    """Checks if either is a subset."""
    a = overlap_atall(start1, end1, start2, end2)
    b = overlap_atall(start2, end2, start1, end1)
    return a or b


def get_int_values(input_line: str) -> Tuple[int]:
    """Converts the lines into int values"""
    # first, second = input_line.split(",")
    first, second = input_line.strip("\n").split(",")
    first_start, first_end = first.split("-")
    second_start, second_end = second.split("-")
    return (int(first_start), int(first_end), int(second_start), int(second_end))


input_file = r"Day 4\my_input.txt"


def main():
    total_pairs = 0
    with open(input_file, "r") as f:
        newline = f.readline()
        while newline != "":
            input_coords = get_int_values(newline)
            if either_overlap(*input_coords):
                total_pairs += 1
            newline = f.readline()

    print(f"The number of overlapping sets is {total_pairs}")


if __name__ == "__main__":
    main()
