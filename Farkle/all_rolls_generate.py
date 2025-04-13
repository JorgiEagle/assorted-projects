from Farkle.src.FarkleRoll import FarkleRoll


def write_rolls(roll_dict, file_out):
    for key, rolls in roll_dict.items():
        file_out.write(str(key))
        file_out.write("\n")
        sorted_rolls = sorted(rolls)
        for roll in sorted_rolls:
            file_out.write(str(roll) + '\n')
        file_out.write('\n\n')
    

with open('Farkle/all_farkle_rolls.txt', 'w') as out:
    write_rolls(FarkleRoll.all_rolls, out)

with open('Farkle/all_winning_rolls.txt', 'w') as out:
    write_rolls(FarkleRoll.winning_rolls, out)