from logo_and_art import *
import random
from game_data import data
import os

def clear():
    """Clear the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --------------------------------------------

def get_random_account():
    """Creates a random person/account from data."""
    return random.choice(data)

# --------------------------------------------

def letter_a(account_a):
    """Everything combined for 'A'"""
    name = account_a["name"]
    description = account_a["description"]
    country = account_a["country"]
    
    return f"Compare A: {name}, a {description}, from {country}."

def letter_b(account_b):
    """Everything combined for 'B'"""
    name = account_b["name"]
    description = account_b["description"]
    country = account_b["country"]
    
    return f"Against B: {name}, a {description}, from {country}."

# --------------------------------------------

def a_followers():
    """The followers of the person."""
    return int(dict_letter_a["follower_count"])

def b_followers():
    """The followers of the person."""
    return int(dict_letter_b["follower_count"])

# --------------------------------------------

def comparing():
    """Comparing A and B."""
    if a_followers() > b_followers():
        return True
    elif a_followers() < b_followers():
        return False

# --------------------------------------------
start = True
while start:
    clear()
    total_score = 0

    game_active = True
    while game_active:
        print(logo)

        if total_score > 0:
            print(f"You're right! Current score: {total_score}.")
        
        dict_letter_a = get_random_account()
        print(letter_a(dict_letter_a)) # Printing comparison A.
        print(vs) # Printing the VS art.
        dict_letter_b = get_random_account()
        print(letter_b(dict_letter_b))  # Printing comparison B.
        
        question = True
        while question:
            q_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
            if q_answer == 'a':
                if comparing() == True:
                        total_score += 1
                        clear()
                        question = False
                else:
                    clear()
                    print(logo)
                    print(f"Sorry, that's wrong. Final score {total_score}.")
                    question = False
                    game_active = False
            elif q_answer == 'b':
                if comparing() == False:
                        total_score += 1
                        clear()
                        question = False
                else:
                    clear()
                    print(logo)
                    print(f"Sorry, that's wrong. Final score {total_score}.")
                    question = False
                    game_active = False
            else:
                print(f"Invalid input. Try again.")

    play_again = True
    while play_again:
        play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
        if play_again == 'y':
            play_again = False
            start = True
            clear()
        elif play_again == 'n':
            print("Thank you for playing 'Higher/lower'!")
            quit()
        else:
            print(f"Invalid input. Try again.")