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

game_over = False
correct_letter = []
while not game_over:
    guess = input("Enter a guess letter:").lower()

    display = ""


# TODO Change the placeholder with the guessed letter
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter

        else:
            display += ("_")
    print(display)

    if "_" not in display:
        game_over = True
        print("You win")

