"""
Write a program (function!) that takes a list and returns a new list
that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""
def no_dups(some_list):
    aset = set()
    alist = []

    for i in some_list:
        aset.add(i)

    for i in aset:
        alist.append(i)

    return alist

def no_dups_no_sets(some_list):
    alist = []

    for i in some_list:
        if i not in alist:
            alist.append(i)

    return alist

my_list = [1, 2, 2, 3, 4, 5, 5, 6, 7]

print(no_dups_no_sets(my_list))