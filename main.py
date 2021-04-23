 
word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)

guess = input('Guess the letter: ').lower()
display = []
for letter in chosen_word:
    if letter == guess:
        display.append(guess)
    else:
        display.append('_')

print(display)
