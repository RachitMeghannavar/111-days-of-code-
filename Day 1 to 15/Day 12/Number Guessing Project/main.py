from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_guess, turns):
    if user_guess > actual_guess:
        print("Too high")
        return turns - 1
    elif user_guess < actual_guess:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it. The correct answer is {actual_guess}")

def set_difficulty():
    level = input("Choose a difficulty (easy or hard): ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    answer = randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()