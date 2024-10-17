from utils import get_column, get_row, get_sector


class SudokuSolver:
    def __init__(self):
        self.grid = [None]*81
        self.solution = [None] * 81
        self.guess = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(81)]

    def set_initial_grid(self, input_grid: list):
        for index, x in enumerate(input_grid):
            if x is None:
                continue
            else:
                self.grid[index] = x
                self.solution[index] = x
                self.guess[index] = None

    def get_grid_row(self, position):
        return get_row(self.grid, position)

    def get_grid_column(self, position):
        return get_column(self.grid, position)

    def get_grid_sector(self, position):
        return get_sector(self.grid, position)

    def get_solution_row(self, position):
        return get_row(self.solution, position)

    def get_solution_column(self, position):
        return get_column(self.solution, position)

    def get_solution_sector(self, position):
        return get_sector(self.solution, position)
    
    def get_guess_row(self, position):
        return get_row(self.guess, position)

    def get_guess_column(self, position):
        return get_column(self.guess, position)

    def get_guess_sector(self, position):
        return get_sector(self.guess, position)

    def consolidate_solution(self):
        changed = True
        while changed:
            changed = False
            for index in range(81):
                if self.guess[index]:
                    horizontal = self.get_solution_row(index)
                    vertical = self.get_solution_column(index)
                    sector = self.get_solution_sector(index)
                    self.guess[index] = self.guess[index].difference(set().union(set(axis) for axis in (horizontal, vertical, sector)))
                    if len(self.guess[index]) == 1:
                        self.solution[index] = self.guess[index].pop()
                        self.guess[index] = None
                        changed = True

    # def fill_single_options(self,  index: int, sector_func: Callable):
    #     """ Fills in all positions where that number is the only position available for that sector"""
    #     single_options = set()
    #     axis_set = sector_func(index)
    #     (single_options.symmetric_difference_update(guess_set) for guess_set in axis_set if guess_set is not None)
    #     for index, entry in enumerate(axis_set):
    #         eligable = entry.intersection(single_options)
    #         assert(len(eligable) <= 1)
    #         if eligable:
    #             eligable.pop()

    def solve(self) -> list:

        return self.solution