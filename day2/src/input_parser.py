import os
from pid_range import PidRange


class InputParser:
    def __init__(self, filepath: str) -> None:
        assert os.path.exists(filepath), f"Filepath {filepath} does not exist"
        self.filepath = filepath
        self.file = open(filepath, "r")
        self.data = list()
        return

    def parse(self) -> None:
        pid_boundaries = self.file.readline().strip().split(',')
        for boundary in pid_boundaries:
            pid_boundary = tuple([int(num) for num in boundary.split('-')])
            self.data.append(PidRange(*pid_boundary))
        return

    def get_data(self) -> list:
        return self.data

    def close(self) -> None:
        self.file.close()
        return
