import unittest
from abc import ABC


class SudokuBaseTest(unittest.TestCase, ABC):
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
        self.test_parital = [
            4, 3, None,         None, None, None,   1, 9, None,
            7, None, 2,         9, None, None,      None, 8, None,
            None, None, None,   None, None, 6,      3, None, None,

            5, 1, 7,            4, 3, None,         9, None, 8,
            3, 8, None,         6, 9, 7,            5, None, 2,
            None, None, None,   None, None, 1,      7, None, 4,

            None, 2, None,      None, None, None,   None, 7, None,
            None, None, None,   3, 2, None,         8, None, None,
            1, None, 3,         None, 6, 8,         None, None, None
        ]
        
        self.valid_axis = [2, 3, 4, 9, 5, 6, 8, 1, 7]
        self.invalid_axis = [9, 3, 4, 9, 5, 6, 8, 1, 1]
