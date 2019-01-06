import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [elem for ele in a for elem in b if ele == elem]
ca = []
c = [ca.append(ele) for ele in c if ele not in ca]
#print(ca)

aa = [random.randrange(100) for i in range(120)]
aa.sort()
print(aa)
bb = [random.randrange(100) for i in range(120)]
bb.sort()
print(bb)

cc = [elem for ele in aa for elem in bb if ele == elem]
cca = []
cc = [cca.append(ele) for ele in cc if ele not in cca]
print(cca)
