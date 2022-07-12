def score_from_string(given_weights, string, given_n):
    return sum([given_weights[string_index] if int(string[string_index]) else given_n - given_weights[string_index] for string_index in range(len(string))])


for test in range(int(input())):
    N, M, P = map(int, input().split())
    friends = []
    forbidden = []
    for friend in range(N):
        friends.append(input())
    for option in range(M):
        forbidden.append(input())
    preferences = [N]*P

    for x in friends:
        for index in range(P):
            preferences[index] -= int(x[index])

    optimal = [('0', score_from_string(preferences, '0', N)), ('1', score_from_string(preferences, '1', N))]
    for x in range(P-1):
        next_optimal = []
        for base in optimal:
            base_one = base[0] + '1'
            base_zero = base[0] + '0'
            next_optimal.append((base_one, score_from_string(preferences, base_one, N)))
            next_optimal.append((base_zero, score_from_string(preferences, base_zero, N)))
        optimal = sorted(next_optimal, key=lambda entry: entry[1])[:M+1]
    for combination in optimal:
        if combination[0] not in forbidden:
            print(f'Case #{test+1}: {combination[1]}')
            break
