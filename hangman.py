import random
stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
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
word_list = ["dog", "cat", "deer", "panda"]
choice_word = random.choice(word_list)
word_length = len(choice_word)

lives = 6

display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = choice_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in choice_word:
        print(f"You guessed {guess}, wrong that's not in the word. You lose a live.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose !")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Won !")

    print(stages[lives])