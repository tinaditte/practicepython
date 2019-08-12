import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [i for i in a for j in b if i in b]
ca = []
c = [ca.append(ele) for ele in c if ele not in ca]
#print(ca)

aa = random.sample(range(10),5)
bb = random.sample(range(10),5)
cc = [i for i in aa for j in bb if i in bb]
cc2 = []
cc = [cc2.append(ele) for ele in cc if ele not in cc2]
print(aa)
print(bb)
print(cc2)