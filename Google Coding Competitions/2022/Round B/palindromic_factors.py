def palindrome(x):
    index = 0
    number = str(x)
    while index < len(number)//2:
        if number[index] != number[len(number)-index-1]:
            return False
        index += 1
    return True


def factors(x):
    fact = set()
    for i in range(1, int(x**0.5)+1):
        if not x % i:
            fact.add(i)
            fact.add(x//i)
    return fact


for test in range(int(input())):
    a = int(input())
    palindrome_factors = map(palindrome, factors(a))
    print("Case #{}: {}".format(test + 1, sum(palindrome_factors)))

