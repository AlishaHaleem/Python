import random

word_list = ["aardvark", "baboon", "camel"]
#TODO: Chose the word randomly from the word_list
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO:Ask the user to guess a letter
guess = input("Enter a guess letter:").lower()
print(guess)

# TODO: Check if the guess is correct or wrong
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")