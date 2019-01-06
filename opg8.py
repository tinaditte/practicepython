import random

#Rock Paper Scissors
#Den vil ikke køre videre :(

print("Let's play Rock, Paper, Sciccors.")
player = input("type r, p or s: ")

while player != 'quit':

    rand = random.randrange(1, 3)

    if player == 'r':
        print("You chose Rock")
    elif player == 'p':
        print("You chose Paper")
    elif player == 's':
        print("You chose Scissors")
    else:
        print("You typed an incorrect command. Try again.")

    if rand == 1:
        rand = 'r'
        print("The computers move is Rock.")
    elif rand == 2:
        rand = 'p'
        print("The computers move is Paper.")
    elif rand == 3:
        rand = 's'
        print("The computers move is Scissors.")

    move = rand

    if player == move:
        print("Tied!")

    elif player == 'r' and move == 's' or player == 'p' and move == 'r' or player == 's' and move == 'p':
        print("You win!")

    elif player == 'r' and move == 'p' or player == 's' and move == 'r' or player == 'p' and move == 's':
        print("You loose...")

    print("\nDo you wish to quit? Type quit.")
    player = input("Otherwise, type r, p or s: ")

