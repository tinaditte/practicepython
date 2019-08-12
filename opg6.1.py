word = input("Enter a word: ")

word.lower()
wordlen = len(word)
drow = word[wordlen::-1]

if word == drow:
    print("Your word is a palindrome! ")
    print(word,"=",drow)
else:
    print("Your word is not a palindrome")
    print(word,"!=",drow)
