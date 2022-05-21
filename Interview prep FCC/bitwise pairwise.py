'''
https://www.youtube.com/watch?v=Roz2OEKYlIE&ab_channel=Scaler
Given a list of positive integers, give the sum of the number of different bits between every pairing of the numbers
e.g. [1, 2]. Gives the pairing: (1,1), (1,2), (2,1), (2,2) The number of differing bits between each respective pair is:
0, 2, 2, 0. Giving a total sum of 4
'''

import itertools
import time
import random

def different_bits(number_1, number_2):
    max_length = len('{0:b}'.format(max(number_1, number_2)))
    bits_1 = '{:b}'.format(number_1).rjust(max_length, '0')
    bits_2 = '{:b}'.format(number_2).rjust(max_length, '0')

    return sum([1 for x in range(max_length) if bits_1[x] != bits_2[x]])


def different_bits_2(number_1, number_2):
    return sum([int(x) for x in '{:b}'.format(number_1 ^ number_2)])


given_input = [random.randint(0, 10) for x in range(10000)]
start_time = time.time()
answer = sum([different_bits(x[0], x[1]) for x in itertools.product(given_input, repeat=2)])
print('Answer', answer, time.time()-start_time)

start_time = time.time()
answer_2 = sum([different_bits_2(x[0], x[1]) for x in itertools.product(given_input, repeat=2)])
print('Answer 2', answer_2, time.time()-start_time)
