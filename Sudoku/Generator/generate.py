from collections import deque, Counter
from Sudoku.Solver.src.utils import get_row, get_column, get_sector
import pickle
all_valid = deque()
sudoku_list = [None for _ in range(81)]
validate_funcs = [get_row, get_column]
count = 0


def recurse(curr_list: list[int], running_index: int):
    for i in range(1, 10):
        curr_list[running_index] = i
        if validate(curr_list, running_index):
            if running_index == len(curr_list) - 1:
                all_valid.append(curr_list)
            recurse(curr_list.copy(), running_index+1)


def validate(grid, curr_index):
    global count
    count += 1
    for index in range(0, 81, 10):
        for func in (validate_funcs if index % 30 else validate_funcs + [get_sector]):
            counter = Counter(func(grid, index))
            if not all(count == 1 for value, count in counter.items() if value is not None):
                return False
    return True


recurse(sudoku_list, 0)
print(f"Grids checked: {count}")
print(f"Valid grids: {len(all_valid)}")
pickle.dump(all_valid, 'all_sudoku_python.pkl')
