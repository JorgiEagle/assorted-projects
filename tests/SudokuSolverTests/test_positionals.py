from Sudoku_Solver.src.utils import get_row, get_column, get_sector
from setup import SudokuBaseTest


class TestPositionals(SudokuBaseTest):
    def test_first_horizontal(self):
        self.assertListEqual(get_row(self.grid, 0), [2, 3, 4, 9, 5, 6, 8, 1, 7])

    def test_first_vertical(self):
        self.assertListEqual(get_column(self.grid, 0), [2, 9, 1, 5, 6, 7, 3, 4, 8])

    def test_first_sector(self):
        self.assertListEqual(get_sector(self.test_grid, 0), [2, 3, 4, 9, 5, 7, 1, 8, 6])

    def test_last_horizontal(self):
        self.assertListEqual(get_row(self.test_grid, 80), [8, 6, 1, 2, 4, 9, 3, 7, 5])

    def test_last_veritcal(self):
        self.assertListEqual(get_row(self.test_grid, 80), [7, 3, 9, 2, 4, 1, 8, 6, 5])

    def test_last_sector(self):
        self.assertListEqual(get_sector(self.test_grid), [1, 4, 8, 9, 2, 6, 3, 7, 5])
