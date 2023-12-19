import random

while True:
    random_number = random.randint(1,10)

    player = int(input("Guess a number between 1 and 10: "))
    correct = random_number

    if player < correct:
        print(f"{player} Too low, try again!")
    elif player > correct:
        print(f"{player} Too high, try again")
    else:
        if player == correct:
            print(f"{correct} You guessed it! You won!")


    playback = input("Do you want to keep playing? (y/n) ")

    if playback == "y":
        continue
    else:
        if playback == "n":
            print("Thanks for playing. Bye!")
            break





