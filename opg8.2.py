from random import randint

names = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
beatings = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}
possible_moves = list(beatings.keys())

while True:
    player = names[str.lower(input("Your move? ")[0])]
    computer = possible_moves[randint(0, 2)]
    if player == computer:
        print("Tied with two", player)
    elif computer in beatings[player]:
        print("Player wins with", player, "over", computer)
    else:
        print("Computer wins with", computer, "over", player)
