from itertools import combinations
from pprint import pprint

length_of_500 = [
    24,
    51,
    12,
    42,
    7,
    7,
    14,
    20,
    9,
    16,
    25,
    85,
    101,
    20,
    45,
    101
]

names = [
    "Frontend",
    "Video Playback",
    "Backend",
    "Content Management",
    "Network",
    "Input",
    "Email",
    "UI Set",
    "Storage",
    "Database",
    "Authentication",
    "Payment",
    "Design Guideline",
    "Notification",
    "API Module",
    "Code Optimisation"
]

length_combinations = combinations(length_of_500, 4)
name_combinations = list(combinations(names, 4))
sorted_combinations = [sorted(x) for x in name_combinations]
pprint(sorted_combinations)
set_names = set(name_combinations)
#for names, total in zip(name_combinations, length_combinations):
 #   print(names, sum(total))


    # 'Content Management', 'Authentication', 'API Module', 'Code Optimisation'