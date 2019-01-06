inp = input("Type a word ")

chars = []
for c in inp:
    if c != ' ':
        chars.append(c)

input = chars[::1]
tupni = chars[::-1]

#print(input)
#print(tupni)

if input == tupni:
    print("It's the same backwards! Look")
    print(input,"\n",tupni)
else:
    print("It doesn't seem to mean much read backwards...")