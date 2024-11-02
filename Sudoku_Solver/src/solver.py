from utils import get_column, get_row, get_sector
from typing import Callable
from cell import Cell


class SudokuSolver:
    def __init__(self):
        self.grid = [Cell() for _ in range(81)]

    def set_initial_grid(self, input_grid: list):
        for index, x in enumerate(input_grid):
            self.grid[index].insert(self.get_grid_row(), self.get_grid_column(), self.get_grid_sector(), x)

    def get_grid_row(self, position):
        return get_row(self.grid, position)

    def get_grid_column(self, position):
        return get_column(self.grid, position)

    def get_grid_sector(self, position):
        return get_sector(self.grid, position)

    def consolidate_solution(self):
        changed = True
        while changed:
            changed = False
            for cell in self.grid:
                cell.update_guess()

    def validate(self):
        return False

    def fill_single_options_in_axis(self,  index: int, sector_func: Callable):
        """ Fills in all positions where that number is the only position available for that axis"""
        single_options = set()
        axis_set = sector_func(index)
        for guess_set in axis_set:
            if guess_set is not None:
                single_options.symmetric_difference_update(guess_set)
        for index, entry in enumerate(axis_set):
            eligable = entry.intersection(single_options)
            assert len(eligable) <= 1
            if eligable:
                eligable.pop()

    def solve(self) -> list:
        while self.solution.count(None):
            self.consolidate_solution()
            self.fill_single_options_in_axis()
        return self.solution
