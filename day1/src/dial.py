class Dial:
    min_value = 0
    max_value = 99
    def __init__(self):
        self.position = 50
        self.num_zeros = 0

    def get_position(self):
        return self.position

    def rotate_right(self, distance) -> None:
        while distance:
            self.position += 1
            if self.position > type(self).max_value:
                self.position = type(self).min_value
            if 0 == self.position:
                self.num_zeros += 1
            distance -= 1
        return

    def rotate_left(self, distance) -> None:
        while distance:
            self.position -= 1
            if self.position < type(self).min_value:
                self.position = type(self).max_value
            if 0 == self.position:
                self.num_zeros += 1
            distance -= 1
        return

    def get_num_zeros(self):
        return self.num_zeros
