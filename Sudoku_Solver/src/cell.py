from typing import Iterable
from exceptions import InvalidSolution


class Cell:
    def __init__(self, row: list, column: list, sector: list, value: int = None):
        if value:
            self.insert_solution(value)
        else:
            self.solution = None
            self.guess = set(range(1, 10))
        self.row: Iterable[Cell] = None
        self.column: Iterable[Cell] = None
        self.sector: Iterable[Cell] = None
        self.axies = [row, column, sector]

    def _set_solution(self, value: int) -> None:
        self.solution = value

    def _set_guess(self, value: set) -> None:
        self.guess = value

    def insert_solution(self, value: int) -> None:
        self._set_solution(value)
        self._set_guess(None)

    def remove_single_guess_value(self, value: int) -> bool:
        if value in self.guess:
            self.guess.remove(value)
            return True
        else:
            return False

    def remove_guess_set(self, set_to_remove: set) -> None:
        self.guess_set = self.guess_set.difference(set_to_remove)

    def update_guess(self):
        for axis in self.axies:
            self.guess.difference_update({cell.solution for cell in axis if cell.solution})
        if len(self.guess) == 0:
            raise InvalidSolution
        if len(self.guess) == 1:
            self.insert_solution(self.guess.pop())