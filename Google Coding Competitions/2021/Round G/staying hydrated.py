for test in range(int(input())):
    x_points = []
    y_points = []
    for K in range(int(input())):
        x_bottom_left, y_bottom_left, x_top_right, y_top_right = map(int, input().split())
        x_points.append(x_bottom_left)
        x_points.append(x_top_right)
        y_points.append(y_bottom_left)
        y_points.append(y_top_right)
    x_points.sort()
    y_points.sort()
    print('Case #' + str(test+1) + ':', x_points[(len(x_points)//2)-1], y_points[(len(y_points)//2)-1])
