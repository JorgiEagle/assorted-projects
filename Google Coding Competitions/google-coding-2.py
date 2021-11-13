import bisect

tests = int(input())
for _ in range(tests):
    N, M = input().split()
    problem_sets = []
    for i in range(int(N)):
        problem_sets += list(map(int, input().split()))
    problem_sets.sort()
    students = list(map(int, input().split()))
    answer = []
    for grade in students:
        if grade in problem_sets:
            answer.append(grade)

