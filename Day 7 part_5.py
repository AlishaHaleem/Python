import random
from hangman_words import word_list
from hangman_art import HANGMAN,logo

#TODO: Create a variable called lives

lives = 6
print(logo)

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
    print(f"***********<{lives}/6 LIVE LEFT >**********")
    guess = input("Enter a guess letter:").lower()
    if guess in correct_letter:
        print(f"You already guessed this {guess} letter.")



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
    print("word to guess: " + display)
# TODO: If guess not in chosen word then live reduce by 1.

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives ==0:
            game_over = True
            print(f"*******The word is  {chosen_word}. YOU LOSE! *******")

    if "_" not in display:
        game_over = True
        print("******* You win!********")


# TODO: Print the ascii art from hangman.
print(HANGMAN[lives])