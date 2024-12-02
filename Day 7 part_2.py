import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO: Create a placeholder
placeholder = ""
length = len(chosen_word)
for position in range(length):
    placeholder += "_"
print(placeholder)

guess = input("Enter a guess letter:").lower()
print(guess)

# TODO: Create a "display" that shows the user the guessed letter.

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += ("_")
print(display)