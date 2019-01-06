number = int(input("Pick a number "))
check = int(input("Pick another "))

if number % 2 > 0:
    print("Your first number is odd")
elif number % 2 == 0:
    print("Your first number is even")
    if number % 4 == 0:
        print("And it is also multiple of 4")

result = number / check
if result % 2 == 0:
    print("Your number can divide evenly into the other")
elif result % 2 > 0:
    print("Cannot divide the second number evenly into the first")
