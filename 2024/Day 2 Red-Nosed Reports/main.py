def is_monotonic(lst):
    return all(
        a > b and 1 <= abs(a - b) <= 3
        for a, b in zip(lst, lst[1:])
    ) or all (
        a < b and 1 <= abs(a - b) <= 3
        for a, b in zip(lst, lst[1:])
    )

def main():
    def read_input(file_path="input.txt"):
        with open(file_path, "r") as f:
            return [line.strip() for line in f.readlines()]


    def parse_input(input_data):       
        return [[*map(int, v.split())] for v in input_data]

    raw_input = read_input()
    parsed_input = parse_input(raw_input)

    print(sum(map(is_monotonic, parsed_input)))

