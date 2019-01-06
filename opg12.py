def first_last(list):
    list = [element for element in list if element == list[0] or element == list[-1]]
    return list

alist = [5, 10, 15, 20, 25]

print(first_last(alist))
