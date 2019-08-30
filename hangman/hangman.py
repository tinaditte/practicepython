#list of words
#illustrate hangman
#illustrate letter guessed, and length of the word
#max 5 guess wrong

#_____
#|    '
#|    o
#|   /\
#|    |
#|   /\
#_\__
# _ _ _ _

string_word = "hangman"
string_illu_word = "_______"
life = 5

def convert(string):
    return [char for char in string]

word = convert(string_word)
illu_word = convert(string_illu_word)

while (len(word) != 0 or life != 0):
    guess_letter = input("Guess a letter: ")

    if guess_letter in word:
        guess_index = word.index(guess_letter)


    elif guess_letter not in word:
        life -= 1
        print("Guesses left",life)
