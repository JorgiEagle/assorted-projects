from Farkle.src.FarkleRoll import FarkleRoll


num_all = {key: len(value) for key, value in FarkleRoll.all_rolls.items()}
num_winning = {key: len(value) for key, value in FarkleRoll.winning_rolls.items()}

print(num_all)
print(num_winning)

percentage_chance_winning = {key: round(num_winning[key]/num_all[key], 4) for key in num_all}
print(percentage_chance_winning)