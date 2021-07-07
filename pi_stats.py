# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:02:42 2021

@author: JackX
"""
import numpy as np
#digits of pi
pi_txt = open("pidigits.txt", "r")
pi_digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    i = pi_txt.read(1)
    if i == '':
        break
    pi_digits[int(i)] += 1
    
print(pi_digits)
print(np.mean(pi_digits))
print(np.std(pi_digits))