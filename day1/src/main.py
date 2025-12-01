import os
from dial import Dial
from input_parser import InputParser
from rotation import LeftRotation, RightRotation


def main():
    num_zeros = 0
    dial = Dial()
    input_filename = os.path.join(os.getcwd(), "data", "input.txt")
    print("Opening file")
    input_parser = InputParser(input_filename)
    print("Parsing file")
    input_parser.parse()
    for instruction in input_parser.get_instructions():
        if isinstance(instruction, LeftRotation):
            dial.rotate_left(instruction.distance)
        elif isinstance(instruction, RightRotation):
            dial.rotate_right(instruction.distance)
        if 0 == dial.get_position():
            num_zeros += 1
    print("Closing file")
    input_parser.close()
    print(f"Number of Zeros {[num_zeros]}")


if __name__ == "__main__":
    main()
