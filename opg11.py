def get_number():
    return int(input("Pick a number "))

number = get_number()
num_range = range(1, number)
listOfDivs = []

listOfDivs = [element for element in num_range if number % element == 0]

#checkprime = [listOfDivs.remove(element) for element in listOfDivs if 1 in listOfDivs]

if len(listOfDivs) == 1:
    print("Your number is a prime!")
else:
    print("Your number is not a prime, here's a list of divisors.")
    print(listOfDivs)
