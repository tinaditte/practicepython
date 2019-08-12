import random

user = int(input("Guess a number between 1 and 9 "))
num = random.randint(1,9)
guesses = 0

print("Type 'q' to quit"
      )
while True:
    if user < num:
        print("Too low ")
        guesses += 1
    elif user > num:
        print("Too high ")
        guesses += 1
    elif user == num:
        print("You guessed it!")
        break

    user = int(input("Guess again "))

print("Your number of guesses: ", guesses)