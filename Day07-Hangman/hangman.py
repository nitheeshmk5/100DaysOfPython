import random as rd
from words import words_store

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
          '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
          '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
          '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
          '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
          '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
          '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word = rd.choice(words_store)
word_len = len(word)

#print(f"Chosen word is {word}")
lifes = 6

display = []
for _ in range(word_len):
    display.append('_')

endGame = False
guessed_letters = []

while not endGame:
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.")
        continue
    
    guessed_letters.append(guess)
    
    found = False
    for pos in range(word_len):
        letter = word[pos]
        if letter == guess:
            display[pos] = letter
            found = True
    
    if not found:
        lifes -= 1
        
    print(stages[lifes])
    print(' '.join(display))
    
    if lifes == 0:
        print(f"Game over! The word was '{word}'.")
        endGame = True
    elif '_' not in display:
        print("Congratulations! You guessed the word!")
        endGame = True
