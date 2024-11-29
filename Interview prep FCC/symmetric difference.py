'''
A programe to find the symmetric difference between several sets
sym([1, 2, 3], [5, 2, 1, 4]) should return [3, 4, 5].
sym([1, 2, 3, 3], [5, 2, 1, 4]) should return [3, 4, 5].
sym([1, 2, 3, 3], [5, 2, 1, 4]) should contain only three elements.
sym([1, 2, 3], [5, 2, 1, 4, 5]) should return [3, 4, 5].
sym([1, 2, 5], [2, 3, 5], [3, 4, 5]) should return [1, 4, 5]
sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]) should return [1, 4, 5].
sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]) should contain only three elements.
sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]) should return [2, 3, 4, 6, 7].
sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]) should return [1, 2, 4, 5, 6, 7, 8, 9].
sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]) should contain only eight elements.
'''


def sym(kwargs):
    final_set = set()
    for element in kwargs:
        final_set = final_set ^ set(element)
    return list(final_set)


tests = [([1, 2, 3], [5, 2, 1, 4]),
         ([1, 2, 3, 3], [5, 2, 1, 4]),
         ([1, 2, 3], [5, 2, 1, 4, 5]),
         ([1, 2, 5], [2, 3, 5], [3, 4, 5]),
         ([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]),
         ([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]),
         ([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])
         ]
results = [[3, 4, 5], [ 3, 4, 5], [3, 4, 5], [1, 4, 5], [1, 4, 5], [2, 3, 4, 6, 7], [1, 2, 4, 5, 6, 7, 8, 9]]
for index, test in enumerate(tests):
    user_answer = sym(test)
    try:
        assert user_answer == results[index]
    except AssertionError:
        print('Test:', index+1, "failed")
        print('Input:', test)
        print('Your answer:', user_answer)
        print('Expected answer:', results[index])
    else:
        print('Test', index+1, 'passed')
