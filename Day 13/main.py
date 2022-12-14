from collections import deque

input_filename = r"Day 13/my_input.txt"
# input_filename = r"Day 13/test_input.txt"


def parse_input(filename: str):
    with open(filename, "r") as f:
        raw_input = f.read()

    raw_pairs = raw_input.split("\n\n")
    pairs = []
    for pair in raw_pairs:
        left, right = pair.split("\n")
        left = eval(left)
        right = eval(right)
        pairs.append([left, right])
    return pairs


def compare(left, right):
    result = None
    for li, ri in zip(left, right):
        if isinstance(li, int) and isinstance(ri, list):
            result = compare([li], ri)
        elif isinstance(li, list) and isinstance(ri, int):
            result = compare(li, [ri])
        elif isinstance(li, list) and isinstance(ri, list):
            result = compare(li, ri)
        else:
            if li < ri:
                result = True
            elif li > ri:
                result = False
            # Otherwise continue looking
        if result is not None:
            return result
    # Ran out of items before making a decision, check which list ran out.
    if len(left) == len(right):
        # If they are equal the result is undecided.
        return None
    else:
        return len(left) < len(right)


def main_part1():
    pairs = parse_input(input_filename)
    # print(f"Comapre [1,2,3] and [1,2,4]: {compare([1,2,3], [1,2,4])}")
    # print(f"Comapre [1,2,3] and [1,2,1]: {compare([1,2,3], [1,2,1])}")
    # print(f"Comapre [[1],[2,3,4]] and [[1],4]: {compare([[1],[2,3,4]], [[1],4])}")
    index_sum = 0
    for index, pair in enumerate(pairs, start=1):
        compare_result = compare(*pair)
        print(f"Pair {index}: {compare_result}")
        if compare_result:
            index_sum += index
    print(f"The sum of the indicies is {index_sum}.")


def parse_part2(filename):
    with open(filename, "r") as f:
        return [eval(line) for line in f.read().splitlines() if line != ""]


def decode(sorted_packets):
    dividers = ([[2]], [[6]])
    current_product = 1
    for i, packet in enumerate(sorted_packets, start=1):
        if packet in dividers:
            current_product *= i
    return current_product


def main_part2():
    packets = []
    for pair in parse_input(input_filename):
        packets.extend(pair)
    packets.append([[2]])
    packets.append([[6]])
    # print("Starting packets")
    # print("\n".join(map(str, packets)))
    # print("")
    sorted_packets = deque([packets.pop()])
    while packets:
        current_packet = packets.pop()
        inserted = False
        for i, sorted_packet in enumerate(sorted_packets):
            if compare(current_packet, sorted_packet):
                sorted_packets.insert(i, current_packet)
                inserted = True
                break

        if not inserted:
            # If it wasn't inserted mid list insert at the end.
            sorted_packets.append(current_packet)

    # print("\n".join(map(str, sorted_packets)))
    print(f"The decoder key is {decode(sorted_packets)}")


if __name__ == "__main__":
    # main_part1()
    main_part2()
