import random

randrang = random.randint(1,3)
gamedict = {1:"r",2:"p",3:"s"}

print("Rock Paper Sciccors game, type r, p or s")
player1 = input("player 1s turn ")

while True:

    k = randrang
    player2 = gamedict[k]

    if player1 == 'r':
        if player2 == 'p':
            print(player2)
            print("Player 2 wins!")
        elif player2 == 'r':
            print(player2)
            print("Tie! ")
        elif player2 == 's':
            print(player2)
            print("Player 1 wins")
        break

    elif player1 == 'p':
        if player2 == 'p':
            print(player2)
            print("Tie! ")
        elif player2 == 'r':
            print(player2)
            print("Player 1 wins")
        elif player2 == 's':
            print(player2)
            print("Player 2 wins")
        break

    elif player1 == 's':
        if player2 == 'p':
            print(player2)
            print("Player 1 wins!")
        elif player2 == 'r':
            print(player2)
            print("Player 2 wins!")
        elif player2 == 's':
            print(player2)
            print("Tie")
        break