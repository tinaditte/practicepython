#user number
#print list of dicisors of that number

num = int(input("Number: "))

list = range(1, num+1)
divs = []

for i in list:
    if num % i == 0:
        divs.append(i)
        print(i)
print(divs)