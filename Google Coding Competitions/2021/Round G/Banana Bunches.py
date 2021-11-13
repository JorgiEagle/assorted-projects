for test in range(int(input())):
    case = 'Case #' + str(test+1) + ':'
    number_of_trees, capacity_K = map(int, input().split())
    bananas_on_trees = list(map(int, input().split()))
    max_bananas = max(bananas_on_trees)
    total_bananas = sum(bananas_on_trees)
    if max_bananas == capacity_K:
        print(case, '1')
        continue
    if total_bananas < capacity_K:
        print(case, '-1')
        continue

    current_best = float('inf')

    for x in range(number_of_trees):
        for y in range(x, number_of_trees):
            if sum(bananas_on_trees[:x]) + sum((bananas_on_trees)[y:]) == capacity_K:
                print(case, x+(number_of_trees-y)-1)
                break
        else:
            continue
        break
    else:
        print(case, '-1')
