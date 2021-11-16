for test in range(int(input())):
    case = 'Case #' + str(test+1) + ':'
    number_of_trees, capacity_K = map(int, input().split())
    bananas_on_trees = list(map(int, input().split()))

    # a list storing the shortest array length that has the sum equal to the index which it is at,
    # Could be presented in dictionary format where the key is the sum ,and the value is the shortest array
    # whose sum is equal to the key
    Best_min_Sum = {}
    for i in range(capacity_K):
        Best_min_Sum[i] = float('inf')
