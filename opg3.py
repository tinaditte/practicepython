number = int(input("Pick a number "))

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist = []

for elements in list:
    if elements < 5:
        newlist.append(elements)
        print(newlist)

for elements in list:
    if elements < number:
        newlist.append(elements)
print(newlist)