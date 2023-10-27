from logo import *
import os
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def clear():
    """Clear the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

# ----------------------------------------------
def set_difficulty():
    """Sets the difficulty of the game."""
    level_answer = True
    while level_answer:
        level = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == 'easy':
            level_answer = False
            return EASY_LEVEL_TURNS
        elif level == 'hard':
            level_answer = False
            return HARD_LEVEL_TURNS
        else:
            print(f"'{level}' is not a valid answer.")

# ----------------------------------------------
def check_answer(guess, answer, turns):
    """Check the guess compared to answer. Returns the number of the remainings.""" 
    if guess > 100:
        print("Give a number below 100.")
        return turns
    elif guess <= -1:
        print("Give a number above 0.")
        return turns
    elif guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
         print("Too low.")
         return turns - 1
    else:
         print(f"That's correct! The answer was {answer}.")

# ----------------------------------------------
def game():
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        
        while True:
            guess = input("Guess a number: ")
            try:
                guess = int(guess)
                break
            except ValueError:
                print("You have to enter a number!\n")

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("\nYou ran out of guesses, you lose.")
            print(f"The correct answer was: {answer}.")
            return     
game()

again = True
while again:
    play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
    if play_again == 'y':
        clear()
        game()
    elif play_again == 'n':
        print("\nThanks for playing the Number Guessing Game!")
        quit()
    else:
        print(f"'{play_again}' is not a valid answer.")