logo = """                            
  __ _ _   _  ___  ___ ___ 
 / _` | | | |/ _ \/ __/ __|
| (_| | |_| |  __/\__ \__ \
 \__, |\__,_|\___||___/___/
  __/ |                    
 |___/                         """


from random import randint

Easy_leval = 10
Hard_leval = 5


def guess_the_number(user_answer ,actual_answer ,turns):
    """ Check answer against guess. Returns the number of turns remaining."""
    if user_answer > actual_answer:
        print("Too high")
        return turns - 1
    elif user_answer < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it ! The answer was {actual_answer}")

def difficulty_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return Easy_leval
    else:
        return Hard_leval


def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1, 100)  # GLOBAL VARIABLE
    print(f"Pass, the correct answer is {answer}")



    turns = difficulty_level()



    guess = 0 #GLOBAL VARIABLE
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = guess_the_number(guess, answer , turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        if guess != answer:
            print("Guess again.")
game()