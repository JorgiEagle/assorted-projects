import itertools
strings = ['eb', 'r', 'v', 'rey', 'ond']
strings = [entry.upper() for entry in strings]
combinations_string = [list(itertools.permutations(string, len(string))) for string in strings]
string_combinations = []
string_combinations += [list(dict.fromkeys([''.join(tuple_entry) for tuple_entry in entry])) for entry in combinations_string]

print(string_combinations)
final_string = 'LET T'
first_string_products = ['REETFAS', 'ERETFAS']

#first_string_products += [list(itertools.permutations((entry_1, first_string_combinations[1][0], entry_2))) for entry_1 in first_string_combinations[0] for entry_2 in first_string_combinations[2]]
#first_string_products = list(itertools.chain(*first_string_products))
#first_string_products = [''.join(entry) for entry in first_string_products]


second_string_products = []
second_string_products += [list(itertools.permutations((entry_1, string_combinations[1][0], string_combinations[2][0], entry_2))) for entry_1 in string_combinations[0] for entry_2 in string_combinations[3]]
second_string_products = list(itertools.chain(*second_string_products))
second_string_products = [''.join(entry) for entry in second_string_products]

mid_string = []
mid_string = list(itertools.product(first_string_products, second_string_products))
mid_string = [''.join(entry) for entry in mid_string]

for entry in mid_string:
    print(final_string + entry + 'OND')
