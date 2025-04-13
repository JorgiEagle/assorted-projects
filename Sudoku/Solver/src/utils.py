def get_row(grid, position):
    """ Returns a list of all elements in the same row"""
    horizontal_position = position//9
    grid_position = horizontal_position*9
    return grid[grid_position:grid_position+9]


def get_column(grid, position):
    """ Returns a list of all elements in the same column"""
    vertical_position = position % 9
    return grid[vertical_position::9]


def get_sector(grid, position):
    """ Returns a list of all elements in the same sector"""
    sector = (position//27)*3 + (position % 9)//3
    start = (sector % 3)*3 + (sector//3)*27
    return [x for index in [0, 9, 18] for x in grid[start+index: start+index+3]]
