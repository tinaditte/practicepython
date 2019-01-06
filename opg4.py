number = int(input("Pick a number "))

alist = range(1, number+1)
listOfDivs = []

for element in alist:
    if number % element == 0:
        listOfDivs.append(element)
        print(element)
print(listOfDivs)

