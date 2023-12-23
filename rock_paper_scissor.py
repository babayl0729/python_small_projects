import random

print("...enter 0 for rock...")
print("...enter 1 for paper...")
print("...enter 2 for scissor...")

rock = 0
paper = 1
scissor = 2

player1 = int(input("(Enter your choice): "))
player2 = random.randint(0,2)

if player1 == player2:
    print("DRAW!")
elif player1 == 0:
    if player2 == 2:
        print("Player 1 picks rock")
        print("The computer picks scissor!")
        print("Player 1 wins!")
    elif player2 == 1:
        print("Player 1 picks rock")
        print("The computer picks paper!")
        print("Player 2 wins!")
elif player1 == 1:
    if player2 == 0:
        print("Player 1 picks paper")
        print("The computer picks rock!")
        print("Player 1 wins!")
    elif player2 == 2:
        print("Player 1 picks paper")
        print("The computer picks scissor")
        print("Computer wins!")
elif player1 == 2:
    if player2 == 1:
        print("Player 1 picks scissor")
        print("The computer picks paper!")
        print("Player 1 wins!")
    elif player2 == 0:
        print("Player 1 picks scissor")
        print("The computer picks rock!")
        print("Computer wins!")
else:
    print("something went wrong")