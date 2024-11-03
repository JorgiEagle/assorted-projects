from utils import get_column, get_row, get_sector
from cell import GridCell


class SudokuSolver:
    def __init__(self, input_grid: list):
        self.grid = [GridCell(value) for value in input_grid]
        for index, cell in enumerate(self.grid):
            cell.initialise_axies(self.get_grid_row(index), self.get_grid_column(index), self.get_grid_sector(index))

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
                if cell:
                    continue
                changed |= cell.update_guess()

    def validate(self):
        return False

    def fill_single_options_in_axis(self,  index: int):
        """ Fills in all positions where that number is the only position available for that axis"""
        cell = self.grid[index]
        for axis in cell.axies:
            unique_value = cell.guess.difference(
                set().union(other_cell.guess for other_cell in axis if other_cell is not cell)
                )
            if len(unique_value) == 1:
                cell.insert_solution(*unique_value)

    def solve(self) -> list:
        count = 0
        while not all(self.grid) and count < 100:
            self.consolidate_solution()
            self.fill_single_options_in_axis()
        return self.solution


def main():
    test_grid = [
        4, 3, None,     None, None, None,   1, 9, None,
        7, None, 2,     9, None, None,       None, 8, None,
        None, None, None,    None, None, 6, 3, None, None,

        5, 1, 7,    4, 3, None,     9, None, 8,
        3, 8, None,     6, 9, 7,    5, None, 2,
        None, None, None,    None, None, 1,     7, None, 4,

        None, 2, None,  None, None, None,    None, 7, None,
        None, None, None,  3, 2, None,  8, None, None,
        1, None, 3,     None, 6, 8,     None, None, None]
    solver = SudokuSolver(test_grid)
    solver.solve()


if __name__ == "__main__":
    main()
