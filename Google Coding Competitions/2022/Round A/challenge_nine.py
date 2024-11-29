"""
Ada gives John a positive integer N. She challenges him to construct a new number (without leading zeros), that is a
multiple of 9, by inserting exactly one digit (0 … 9) anywhere in the given number N. It is guaranteed that N does not
have any leading zeros.

As John prefers smaller numbers, he wants to construct the smallest such number possible. Can you help John?
"""
for test in range(int(input())):
    N = input()
    running_sum = 0
    for number in N:
        running_sum = (running_sum + int(number)) % 9
    number_to_add = (9 - running_sum) % 9
    index = 0 if number_to_add > 0 else 1
    for number in N:
        if number_to_add < int(number):
            break
        index += 1

    print("Case #{}: {}".format(test+1, (N[:index] + str(number_to_add) + N[index:])))
