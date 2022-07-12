'''
pairwise([1, 4, 2, 3, 0, 5], 7) should return 11.
pairwise([1, 3, 2, 4], 4) should return 1.
pairwise([1, 1, 1], 2) should return 1.
pairwise([0, 0, 0, 0, 1, 1], 1) should return 10.
pairwise([], 100) should return 0.
'''

def pairwise(arr, target):
    indexes = list(range(len(arr)))
    total = 0
    while len(arr) > 1:
        for index_, element in enumerate(arr[1:]):
            if arr[0] + element == target:
                total += indexes[0] + indexes[index_+1]
                indexes.pop(0)
                indexes.pop(index_)
                arr.pop(0)
                arr.pop(index_)
                break
        else:
            arr.pop(0)
            indexes.pop(0)
    return total



tests = [[1, 4, 2, 3, 0, 5],
         [1, 3, 2, 4],
         [1, 1, 1],
         [0, 0, 0, 0, 1, 1],
         []]
targets = [7, 4, 2, 1, 100]
results = [11, 1, 1, 10, 0]

for index, test in enumerate(tests):
    user_result = pairwise(test, targets[index])
    try:
        assert user_result == results[index]
    except AssertionError:
        print('Test', index+1, 'failed')
        print('Input', test, targets[index])
        print('output', user_result)
        print('intended output', results[index])
    else:
        print('Test', index+1, 'passed')
