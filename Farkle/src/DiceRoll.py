from collections import Counter
from dataclasses import dataclass



@dataclass(frozen=True)
class DiceRoll:
    one: int = 0
    two: int = 0
    three: int = 0
    four: int = 0
    five: int = 0
    six: int = 0

    @classmethod
    def fromFaceValues(cls, face_values: list[int]):
        """ Constructor from face value of dice rolls, values seen on table. """
        count_values = Counter(face_values)
        return cls(*[count_values.get(index, 0) for index in range(1, 7)])

    def get_roll(self) -> tuple[int]:
        return (self.one, self.two, self.three, self.four, self.five, self.six)

    def get_num_dice(self) -> int:
        return sum(self.get_roll())

    def counts(self) -> tuple[int]:
        return set(self.get_roll())

    def __str__(self) -> str:
        return str(self.get_roll())

    def __repr__(self) -> str:
        return f"DiceRoll{self.__str__()}"
    
    def __lt__(self, value: 'DiceRoll'):
        return self.get_roll() < value.get_roll()
    
    def __eq__(self, value: 'DiceRoll'):
        self.get_roll() == value.get_roll()


if __name__ == "__main__":
    new = DiceRoll(3, 2)
    print(new)
    print(new.one)
    print(new)