num = int(input("Number: "))

def isprime(num):
    num_range = range(1, num)
    listofdivs = [i for i in num_range if num % i == 0]
    if len(listofdivs) == 1:
        return True
    else:
        print(listofdivs)
        return False

if isprime(num) == True:
    print("Your number is a prime")
elif isprime(num) == False:
    print("Your number is not a prime, here is a list of divisors ")
