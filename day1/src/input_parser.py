import os
from rotation import rotation_map

class InputParser:
    def __init__(self, filepath: str) -> None:
        assert os.path.exists(filepath), f"Filepath {filepath} does not exist"
        self.filepath = filepath
        self.file = open(filepath, "r")
        self.instructions = list()
        return

    def parse(self) -> None:
        for line in self.file:
            line = line.strip()
            direction, distance = line[0], int(line[1:])
            print(f"Direction: [{direction}] Distance: [{distance}]")
            rotation = rotation_map.get(direction, None)
            assert rotation is not None, f"Failed to parse input file [{self.filepath}]"
            self.instructions.append(rotation(distance))
        return

    def get_instructions(self) -> list:
        return self.instructions

    def close(self) -> None:
        self.file.close()
        return
