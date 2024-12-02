import random
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "baboon", "camel"]

#TODO: Create a variable called lives

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO: Create a placeholder
placeholder = ""
length = len(chosen_word)
for position in range(length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []
while not game_over:
    guess = input("Enter a guess letter:").lower()

    display = ""


# TODO: Change the placeholder with the guessed letter
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter

        else:
            display += ("_")
    print(display)
# TODO: If guess not in chosen word then live reduce by 1.

    if guess not in chosen_word:
        lives -= 1
        if lives ==0:
            game_over = True
            print("You Lose.")

    if "_" not in display:
        game_over = True
        print("You win.")


# TODO: Print the ascii art from hangman.
print(HANGMAN[lives])




