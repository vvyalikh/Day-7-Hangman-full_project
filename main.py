 
word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
for letter in range(word_length):
  display.append('_')
print(display)

guess = input('Guess the letter: ').lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = guess

print(display)
