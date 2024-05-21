import random
from itertools import repeat
output = "ouptut.csv"

flip = ["Heads", "Tails"]

results = []
for games in range(10000):
    players = [10000]
    while players[-1] > 0:
        round = [random.choice(flip) for x in range(players[-1])]
        players.append(len(tuple(filter(lambda x: x == "Heads", round))))
    results.append(players)

with open(output, 'w') as out:
    out.write("Initial,")
    for x in range(max(map(len, results))):
        out.write(f"Round {x+1},")
    out.write('\n')
    for x in results:
        out.write(",".join(map(str, x)))
        out.write("\n")
    
print(f"Min number of rounds: {min(map(len, results))}")
print(f"Max number of rounds: {max(map(len, results))}")
