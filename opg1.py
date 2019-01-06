import datetime

name = input("Your name? ")
age = int(input("Your age? "))

now = datetime.datetime.now()
currentYear = now.year
restAge = 100 - age

turn100 = now.year + restAge

print("Your name is: ", name, " and you are ", age, " years old.")
print("In year " + str(turn100) + " you will be 100 years old")
