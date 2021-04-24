 
word_list = ["aardvark", "baboon", "camel"]
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
lives = 6

for letter in range(word_length):
    display.append('_')
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"This letter has been named already")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            print(f"Your letter is: {guess}")
            display[position] = letter
    if guess not in chosen_word:
        lives = lives - 1
        print(f"Your letter is: {guess}. There is no letter {guess} in the word. You loose 1 life.")
        if lives == 0:
            end_of_game = True
            print('You loose')
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])