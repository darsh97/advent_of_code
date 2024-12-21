
def main():
    def read_input(file_path="input.txt"):
        with open(file_path, "r") as f:
            return [line.strip() for line in f.readlines()]


    def parse_input(input_data):       
        return [[*map(int, value.split())] for value in input_data]

    parsed_input = parse_input(raw_input)

    print(
        sum(starmap(lambda a, b: abs(a-b), zip(*map(sorted, (zip(*parsed_input))))))
        )