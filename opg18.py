"""
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number.
Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.”
Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
"""
import random
com = []
user = []
count = 0
cow = 0
bull = 0

def generate(list):
    for i in range(4):
        i = random.randrange(1, 9)
        list.append(i)
    return list

print("Type q to quit.")
generate(com)
print(com)

while user != 'q':
    user = int(input('Type 4 digits'))

    if user == 'q':
        break

    while user != com:
        for i in user:
            for j in com:
                if user[i] == com[j]:
                    print("You've got",cow, "cow/s")
                    cow += 1
                elif user(i) in com(j):
                    print("You've got", bull, "bull/s")
                    bull += 1
                else:
                    print("Guess again")
                count += 1

            print("You've got", cow, "cow/s and", bull, "bull/s")
            print("This is round", count)