from utils import get_column, get_row, get_sector
from cell import GridCell
from typing import Iterable
from itertools import chain
from exceptions import InvalidSolution


class SudokuSolver:
    def __init__(self, input_grid: list):
        self.grid = [GridCell(value) for value in input_grid]
        # TODO see if using to_solve set is more efficient
        for index, cell in enumerate(self.grid):
            cell.initialise_axies(self.get_grid_row(index), self.get_grid_column(index), self.get_grid_sector(index))

    def __str__(self):
        output = ''
        for line in range(9):
            for sector in range(0, 9, 3):
                output += ", ".join(map(lambda x: str(x.solution), self.grid[line+sector: line+sector+3])) + "\t"
            output += '\n'
        return output
            
    def get_grid_row(self, position):
        return get_row(self.grid, position)

    def get_grid_column(self, position):
        return get_column(self.grid, position)

    def get_grid_sector(self, position):
        return get_sector(self.grid, position)

    @staticmethod
    def convert_guess_to_solution(cell: 'GridCell'):
        if len(cell.guess) != 1:
            raise ValueError(f"Too many guesses to insert solution: {len(cell.guess)}")
        else:
            cell.insert_solution(*cell.guess)

    @staticmethod
    def propagate_solution(source_cell: 'GridCell'):
        for neighbour_cell in chain(*source_cell.axies):
            if not neighbour_cell:
                neighbour_cell.remove_single_guess_value(source_cell.solution)
                if len(neighbour_cell.guess) == 1:
                    SudokuSolver.insert_solution(neighbour_cell)

    @staticmethod
    def insert_solution(cell: 'GridCell'):
        SudokuSolver.convert_guess_to_solution(cell)
        SudokuSolver.propagate_solution(cell)

    @staticmethod
    def consolidate_solution(grid: Iterable[GridCell]):
        changed = True
        while changed:
            changed = False
            for cell in grid:
                if cell:
                    continue
                cell.update_guess()
                match len(cell.guess):
                    case 0:
                        raise InvalidSolution
                    case 1:
                        SudokuSolver.insert_solution(cell)
                        changed = True

    def fill_single_options_in_axis(self):
        """ Fills in all positions where that number is the only position available for that axis"""
        for cell in self.grid:
            if cell:
                continue
            for axis in cell.axies:
                unique_value = cell.guess.difference(
                    set().union(*[other_cell.guess for other_cell in axis if (other_cell is not cell
                                                                              and other_cell.guess is not None)])
                    )
                if len(unique_value) == 1:
                    cell.insert_solution(*unique_value)
                    break

    def solve(self) -> list:
        count = 0
        SudokuSolver.consolidate_solution(self.grid)
        self.fill_single_options_in_axis()
        return self.grid


def main():
    test_grid = [
        4, 3, None,         None, None, None,   1, 9, None,
        7, None, 2,         9, None, None,      None, 8, None,
        None, None, None,   None, None, 6,      3, None, None,

        5, 1, 7,            4, 3, None,         9, None, 8,
        3, 8, None,         6, 9, 7,            5, None, 2,
        None, None, None,   None, None, 1,      7, None, 4,

        None, 2, None,      None, None, None,   None, 7, None,
        None, None, None,   None,  3, 2, None,  8, None, None,
        1, None, 3,         None, 6, 8,         None, None, None]
    solver = SudokuSolver(test_grid)
    solver.solve()
    print(solver)


if __name__ == "__main__":
    main()
