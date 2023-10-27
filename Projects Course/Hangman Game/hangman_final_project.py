#Step 5 (improvement for user experience)

import random
from hangman_word_list import word_list
from hangman_art import *

stages = stages
word_list = word_list

number_of_words = len(word_list)
random_word = random.randint(0, number_of_words - 1)
chosen_word = word_list[random_word]
word_length = len(chosen_word)
guessed_letters = []
lives = 6

# Printing the logo
print(logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for i in range(word_length):
    i = display.append("_")
print(f"{' '.join(display)}")

# Game active when False
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.s
    if guess in guessed_letters:
        print(f"You already guessed {guess.title()}. Try another letter.")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Reduce live by 1 if chosen_word is not good.
    if guess not in chosen_word:
        if guess not in guessed_letters:
            print(f"{guess.title()} is not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The correct word was '{chosen_word}'.")
            
    # Appending and printing the guessed letters
    guessed_letters.append(guess)
    print(f"Guessed letters: {' '.join(guessed_letters).title()}")
    
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(f"You win, the correct word was '{chosen_word}'!")

    # Printing the stage of lives.
    print(stages[lives])