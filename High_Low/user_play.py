from CommandLineHighLow import CommandLineHighLow

def main():
    scores = []

    game = CommandLineHighLow()

    stop = False
    while not stop:
        scores.append(game.play())
        stop = input("Would you like to quit? ")

    print("Total games:", len(scores))
    print("Total: ", sum(scores))
    print("Average Score", sum(scores)/len(scores))
    print("Scores:")
    for x in scores:
        print(x)

if __name__ == "__main__":
    main()
