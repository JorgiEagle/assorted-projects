from collections import Counter


class DiceRoll:
    def __init__(self, ones: int = 0, twos: int = 0, threes: int = 0, fours: int = 0, fives: int = 0, sixes: int = 0):
        self.one = ones
        self.two = twos
        self.three = threes
        self.four = fours
        self.five = fives
        self.six = sixes
        self.set_roll()

    @classmethod
    def fromFaceValues(cls, face_values: list[int]):
        """ Constructor from face value of dice rolls, values seen on table. """
        count_values = Counter(face_values)
        return cls(*[count_values.get(index, 0) for index in range(1, 7)])

    def set_roll(self):
        self.roll = (self.one, self.two, self.three, self.four, self.five, self.six)

    def get_roll(self):
        return self.roll


if __name__ == "__main__":
    pass