import random
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = [random.randint(0,10) for i in range(15)]
b = [random.randint(0,10) for i in range(15)]
c  = set()

c = [i for i in a for j in b if i in b]
c = list(dict.fromkeys(c))

print(c)

