def turn_right(orientation):
    turn = {'N': (0, 1), 'NE': (1, 0), 'SE': (1, -1), 'S': (0, -1), 'SW': (-1, 0), 'NW': (-1, 1)}
    return turn[orientation], list(turn.keys())[(list(turn.keys()).index(orientation) + 1) % 5]


def turn_left(orientation):
    turn = {'N': (0, -1), 'NE': (-1, 0), 'SE': (-1, 1), 'S': (0, 1), 'SW': (1, 0), 'NW': (1, -1)}
    return turn[orientation], list(turn.keys())[(list(turn.keys()).index(orientation) + 1) % 5]


def trace_path_sw(current_x, current_y, orientation, colour):
    path = []
    while current_x > 0 and current_y < N + 1:
        cell = board[current_x][current_y]
        if cell == colour:  # turn right
            path.append((current_x, current_y))
            delta, orientation = turn_right(orientation)
            current_x += delta[0]
            current_y += delta[1]
        else:  # cell is either red or empty, so turn left
            delta, orientation = turn_left(orientation)
            current_x += delta[0]
            current_y += delta[1]
    if current_y == N + 1:  # reached the right
        return path
    else:
        return False


def trace_path_nw(current_x, current_y, orientation, colour):
    path = []
    while current_x > 0 and current_y < N + 1:
        cell = board[current_x][current_y]
        if cell == colour:  # turn left
            path.append((current_x, current_y))
            delta, orientation = turn_left(orientation)
            current_x += delta[0]
            current_y += delta[1]
        else:  # cell is either red or empty, so turn right
            delta, orientation = turn_right(orientation)
            current_x += delta[0]
            current_y += delta[1]
    if current_y == N + 1 and colour == 'B':  # reached the right
        return path
    elif current_x == 0 and colour == 'R':  # reached top
        return path
    else:
        return False


for test in range(int(input())):
    N = int(input())
    board = []
    blue = 0
    red = 0
    result = ''
    board.append(['B'] + ['R']*N + ['B'])
    for x in range(N):
        row = ['B'] + input().split() + ['B']
        blue += row.count('B')
        red += row.count('R')
        board.append(row)
    board.append(['B'] + ['R'] * N + ['B'])

    if abs(blue - red) > 1:
        print(f'Case #{test+1}: Impossible')
        continue

    # checking blue
    # start in south_west
    south_west_path = trace_path_sw(N, 1, 'N', 'B')
    north_west_path = None
    if south_west_path:
        north_west_path = trace_path_nw(0, 1, 'SE', 'B')

    finished = False
    if south_west_path and not north_west_path:
        print(f'Case #{test + 1}: Blue wins')
        continue
    elif south_west_path and north_west_path:
        if len(south_west_path) < len(north_west_path):
            for x in south_west_path:
                if x in north_west_path:
                    print(f'Case #{test + 1}: Blue wins')
                    finished = True
                    break
            if finished:
                continue
        print(f'Case #{test+1}: Impossible')
        continue
    # no blue path, check red
    south_west_path = trace_path_sw(N, 1, 'N', 'R')
    north_west_path = None
    if south_west_path:
        north_west_path = trace_path_nw(0, 1, 'SE', 'R')

    finished = False
    if south_west_path and not north_west_path:
        print(f'Case #{test + 1}: Red wins')
        continue
    elif south_west_path and north_west_path:
        if len(south_west_path) < len(north_west_path):
            for x in south_west_path:
                if x in north_west_path:
                    print(f'Case #{test + 1}: Red wins')
                    finished = True
                    break
            if finished:
                continue
        print(f'Case #{test + 1}: Impossible')
        continue
    print(f'Case #{test + 1}: Nobody wins')



