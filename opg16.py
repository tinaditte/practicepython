"""
Write a password generator in Python. Be creative with how you generate passwords
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be.
For weak passwords, pick a word or two from a list.
"""

import random
import string

number = string.digits
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
symbol = string.punctuation

def generator_strong(size, password=number + lowercase + uppercase + symbol):
    return ''.join(random.choice(password) for x in range(size))

def generator_medium(size, password=number + lowercase + uppercase):
    return ''.join(random.choice(password) for y in random(size))

def generator_mild(size, password=number + lowercase):
    return ''.join(random.choice(password) for z in random(size))

def generator_weak(size, password= lowercase):
    return ''.join(random.choice(password) for i in random(size))

print("How strong do you want your password to be?")
inp = input("strong, medium, mild or weak? ")
size = input("Pick a length for your password: ")

if inp == "strong":
    print(generator_strong(size))
elif inp == "medium":
    print(generator_medium(size))
elif inp == "mild":
    print(generator_mild(size))
elif inp == "weak":
    print(generator_weak(size))
else:
    print("Your choice is invalid")