import random
#print("Welcome to the rock, paper or scissor game!")
rock ='''  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock , paper, scissor]



user_choice = int(input("What you choose? Type 0 for rock, 1 for paper, 2 for scissor.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])


computer_choice= random.randint(0 ,2)
print("Computer choose :")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You type an invalid number. You lose!")
elif user_choice ==0 and computer_choice == 2:
    print("You win!")
elif user_choice ==2 and computer_choice ==0:
    print("You lose!")
elif computer_choice > user_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("You Draw!")
elif user_choice >= 3 or user_choice < 0:
    print("You type an invalid number. You lose!")
print("you lose")
