from collections import Counter
import random
try:
    user_selection = list(map(int, input('Make your selection: ').split()))
except ValueError:
    print('Please type only numbers separated with a space')

print(user_selection)