import os
from input_parser import InputParser


def main():
    input_filename = os.path.join(os.getcwd(), "data", "input.txt")
    print("Opening file")
    input_parser = InputParser(input_filename)
    print("Parsing file")
    input_parser.parse()
    test_invalid_ids = list()
    for test_pid in input_parser.get_data():
        test_invalid_ids.extend(test_pid.get_invalid_ids())
    print(f"Sum of invalid ids [{sum(test_invalid_ids)}]")
    print("Closing File")
    input_parser.close()


if __name__ == "__main__":
    main()
