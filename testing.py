import random


def solution(A):
    A_unique = set(A)
    A_plus_one = {x+1 for x in A_unique}
    for element in A_unique:
        if element in A_plus_one:
            return True
    return False


list_ = [random.randrange(1, 1000000, 2) for x in range(1000000)]

# file.write(str(random.randint(1, 1000000)))
print(solution(list_))