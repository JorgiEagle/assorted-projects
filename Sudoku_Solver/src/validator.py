from collections import Counter
from utils import get_column, get_row, get_sector


class SudokuValidate:
    @staticmethod
    def validate(axis: list[int]) -> bool:
        return all(x == 1 for x in Counter(axis).values())

    @staticmethod
    def validate_grid(grid: list[int]) -> bool:
        for index in range(0, 81, 10):
            if index % 30 == 0:
                if not SudokuValidate.validate(get_sector(grid, index)):
                    return False
            if (not SudokuValidate.validate(get_row(grid, index))) or (not SudokuValidate.validate(get_column(grid, index))):
                return False
        return True
