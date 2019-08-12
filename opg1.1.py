name = input("Name? ")
age = int(input("Age? "))
turned = input("Has your birthday passed this year? y/n")

if turned == 'n':
    age = age + 1

age_100 = (2019 - age) + 100

message = "Hello", name, " in ", age_100, "you'll turn a 100 years old!"
string_message = " ".join(str(x) for x in message)
print(string_message)

num = int(input("Now give me a number! "))

for i in range(num):
    print(string_message)
    i += i

