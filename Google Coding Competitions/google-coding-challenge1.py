import statistics as stat
test_cases = int(input())
for _ in range(test_cases):
    total_possible = 0
    g= []
    g.append(list(map(int, input().split())))
    g.append(list(map(int, input().split())))
    g.append(list(map(int, input().split())))
    known_progressions = [(g[0][0], g[0][1], g[0][2]), (g[0][0], g[1][0], g[2][0]), (g[2][0], g[2][1], g[2][2]), (g[0][2], g[1][1], g[2][2])]
    total_possible += sum([1 if entry[0] + entry[2] == 2*entry[1] else 0 for entry in known_progressions])
    possible_progressions = [(g[0][1] + g[2][1])/2, (g[1][0] + g[1][1])/2, (g[0][0] + g[2][2])/2, (g[2][0] + g[0][2])/2]
    desired_number = [i for i in possible_progressions if i.is_integer()]
    if desired_number:
        desired_number = stat.mode(desired_number)
        total_possible += sum([1 if j == desired_number else 0 for j in possible_progressions])
    print('Case #{}: {}'.format(_+1, total_possible))
