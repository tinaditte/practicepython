import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = set()
for ele in a:
    for elem in b:
        if ele == elem:
            c.add(elem)

#print(c)


aa = [random.randrange(1000) for i in range(120)]
print(aa)
bb = [random.randrange(1000) for i in range(120)]
print(bb)
cc = set()

for ele in aa:
    for elem in bb:
        if ele == elem:
            cc.add(elem)
print(cc)
