import random
#Guess a number

num = random.randint(1, 9)
count = 0
user = 0

print("Type 'q' to quit.")

while user != 'q' and user != num:

    #print(num)
    user = input("Pick a number between 1 and 9 ")

    if user == 'q':
        break

    if int(user) == num:
        print("You guessed right!")
        count += 1
        print("You guessed ", count, " time/s.")
    elif int(user) < num:
        print("You guessed too low!")
        count += 1
        print("Try again or type 'q' to quit.")
    elif int(user) > num:
        print("You guessed too high!")
        count += 1
        print("Try again or type 'q' to quit.")
    else:
        print("The number is not within range, or what you type was not a number.")
