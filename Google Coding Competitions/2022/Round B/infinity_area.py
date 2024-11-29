for test in range(int(input())):
    r, a, b = map(int, input().split())
    total_area = 0
    current_radius = r
    while current_radius > 0:
        total_area += current_radius**2 * (1 + a**2)
        current_radius = (current_radius * a) // b
    print("Case #{}: {:.6f}".format(test+1, total_area*3.14159265358979323))
