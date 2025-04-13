from typing import Iterable
from exceptions import InvalidSolution


class Cell:
    def __init__(self, value: int = None):
        if value:
            self.insert_solution(value)
        else:
            self.solution: int = None
            self.guess: set = set(range(1, 10))

    def __bool__(self):
        return bool(self.solution)

    def _set_solution(self, value: int) -> None:
        self.solution: int = value

    def _set_guess(self, value: set) -> None:
        self.guess: set = value

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
        self.guess.difference_update(set_to_remove)

    def __str__(self):
        return f"Cell {self.solution if self.solution else self.guess}"

    def __repr__(self):
        return f"Cell({self.solution})"


class GridCell(Cell):
    def initialise_axies(self, row: list['GridCell'], column: list['GridCell'], sector: list['GridCell']) -> None:
        self.row: Iterable[Cell] = row
        self.column: Iterable[Cell] = column
        self.sector: Iterable[Cell] = sector
        self.axies = [row, column, sector]
        for axis in self.axies:
            axis.remove(self)

    def __repr__(self):
        return "Grid" + super().__repr__()

    def update_guess(self) -> None:
        for axis in self.axies:
            self.remove_guess_set({cell.solution for cell in axis if cell.solution})
        if len(self.guess) == 0:
            raise InvalidSolution
