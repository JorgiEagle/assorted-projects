import unittest
from src.utils import get_row, get_column, get_sector


class TestPositionals(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.test_grid = [
            2, 3, 4,  9, 5, 6,  8, 1, 7,
            9, 5, 7,  8, 1, 4,  2, 6, 3,
            1, 8, 6,  3, 7, 2,  4, 5, 9,

            5, 4, 9,  6, 8, 1,  7, 3, 2,
            6, 1, 8,  7, 2, 3,  5, 9, 4,
            7, 2, 3,  4, 9, 5,  6, 8, 1,

            3, 9, 2,  5, 6, 7,  1, 4, 8,
            4, 7, 5,  1, 3, 8,  9, 2, 6,
            8, 6, 1,  2, 4, 9,  3, 7, 5
        ]

    def test_first_horizontal(self):
        self.assertListEqual(get_row(0), [2, 3, 4, 9, 5, 6, 8, 1, 7])

    def test_first_vertical(self):
        self.assertListEqual(get_column(0), [2, 9, 1, 5, 6, 7, 3, 4, 8])
