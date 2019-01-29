"""
write program w functions
- ask user for a string, w/ multiple words
- send back string with words reversed order
"""

user = input("Type a sentence: ")
words = []

def reverse_sentence(words):
    words = user.split()
    for i in reversed(words):
        words.reverse()
    return words

new_sentence = reverse_sentence(user)
print(new_sentence)