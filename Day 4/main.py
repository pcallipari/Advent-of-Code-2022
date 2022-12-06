from typing import Tuple


def is_subset_of(start1: int, end1: int, start2: int, end2: int) -> bool:
    # This function makes the assumption that start and end are ordered. (start > end)
    # Check that the start of the second set of values is between the start and end of the first
    if start2 >= start1 and start2 <= end1:
        # Check that the end is contained in the start and end of the first
        if end2 >= start1 and end2 <= end1:
            return True

    return False


def either_subset(start1: int, end1: int, start2: int, end2: int) -> bool:
    """Checks if either is a subset."""
    a = is_subset_of(start1, end1, start2, end2)
    b = is_subset_of(start2, end2, start1, end1)
    return a or b


def get_int_values(input_line: str) -> Tuple[int]:
    """Converts the lines into int values"""
    first, second = input_line.split(",")
    first_start, first_end = first.split("-")
    second_start, second_end = second.split("-")
    return (first_start, first_end, second_start, second_end)


input_file = r"Day 4\test_input.txt"


def main():
    with open(input_file, "r") as f:
        input_coordinates = map(get_int_values, f.readlines())
    overlapped_sets = filter(lambda x: either_subset(*x), input_coordinates)
    total_overlapped = sum(1 for _ in overlapped_sets)
    print(f"The number of overlapping sets is {total_overlapped}")


if __name__ == "__main__":
    main()
