"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.

(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

user = int(input("How many sequences of fibonnaci numbers? "))

cache = dict()

def fibo(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    elif num in cache.keys():
        return cache[num]
    else:
        cache[num] = fibo(num-1) + fibo(num-2)
        return cache[num]

alist = [fibo(i) for i in range(user)]
print(alist)

def fibonacci():
    i = 0
    while True:
        yield fibo(i)
        i += 1

fibobject = fibonacci()

fibonaccis = [next(fibobject) for i in range(user)]
print(fibonaccis)