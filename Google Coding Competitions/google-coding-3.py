import math
import sympy


def prime_factors(number, limit):
    factors = {}
    for prime in sympy.primerange(2, limit+1):
        while (number/prime).is_integer():
            number /= prime
            factors[prime] += 1
    return factors

tests = int(input())
for test in range(tests):
    N, Q, P = list(map(int, input().split()))
    Array_A = list(map(int, input().split()))
    for case in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            Array_A[query[1]] = query[2]
        else:
            S, L, R = query[1:]
            total = 0
            for x in range(L, R+1):
                Array_A[x]**S - (Array_A[x] % P)**S
                total+=