class Rotation:
    def __init__(self, distance):
        self.distance = distance

    def describe(self):
        print(f"Type: [{type(self).__name__}] Distance: [{self.distance}]")


class LeftRotation(Rotation):
    def __init__(self, distance):
        super().__init__(distance)


class RightRotation(Rotation):
    def __init__(self, distance):
        super().__init__(distance)


rotation_map = {"L": LeftRotation, "R": RightRotation}
