from Sudoku_Solver.src.validator import SudokuValidate
from setup import SudokuBaseTest


class TestValidate(SudokuBaseTest):
    def test_validate_axis_true(self):
        self.assertTrue(SudokuValidate(self.valid_axis))

    def test_validate_axis_false(self):
        self.assertFalse(SudokuValidate(self.invalid_axis))
