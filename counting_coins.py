import random


def run():
    money = 10
    while 0 < money < 20:
        if random.random() < 0.5:
            money -= 1
        else:
            money += 1
    return bool(money)


def monte_run():
    total_wins = sum(run() for _ in range(10000000))
    print(total_wins/10000)


def roll_dice():
    return sum(random.randint(1, 6) for _ in range(4))%2


def babies():
    total_kids = 1
    balance = random.choice([-1, 1])
    while balance != 0:
        balance += random.choice([-1, 1])
        total_kids += 1
    return total_kids


trials = 1000
total_kids = sum(babies() for _ in range(trials))
print(total_kids/trials)