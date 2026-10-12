import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _________
---'   ______)____
          ________)
          ___________)
         ___________)
---.____________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images=[rock, paper, scissors]
user_guess = int(input("What do you choose, 0 for rock, 1 for paper, 2 for scissors: "))
if user_guess >=0 and user_guess <=2:
    print(game_images[user_guess])
else :
    print("Invalid input")
computer_choice = random.randint(0,2)
print("Computer chooses rock, paper, scissors: ")
print(game_images[computer_choice])
if user_guess >=3 and user_guess <0:
    print("You typed an invalid number you lose")
elif user_guess == 0 and computer_choice == 2 :
    print("You win!")
elif user_guess == 2 and computer_choice == 0:
    print("You lose!")
elif computer_choice > user_guess:
    print("You lose!")
elif computer_choice < user_guess:
    print("You win!")
elif computer_choice == user_guess:
    print("It's a draw!")
