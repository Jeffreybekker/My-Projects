import random
from logo import logo
import os

def clear():
    """Clear the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

# ----------------------------------------------
def random_cards(player, dealer):
    """Picks 2 random cards for the player."""
    for player in range(2):
       player = random.choice(cards)
       player_cards.append(player)
    for dealer in range(1):
       dealer = random.choice(cards)
       dealer_cards.append(dealer)
    return

# ----------------------------------------------
def current_score_player():
    """Giving the current score of the player."""
    return sum(player_cards)

def current_score_dealer():
    """Giving the current score of the dealer."""
    return sum(dealer_cards)

# ----------------------------------------------
def extra_card_player():
    """Give the player an extra card."""
    for extra in range(1):
        extra = random.choice(cards)
        player_cards.append(extra)
    return

def extra_card_dealer():
    """Give the dealer an extra card."""
    while current_score_dealer() < 17:
        for extra in range(1):
            extra = random.choice(cards)
            dealer_cards.append(extra)
    return

# ----------------------------------------------
def compare_scores():
    """Compare the scores between player and dealer."""
    if current_score_player() > 21:
        return "You lose."
    elif current_score_player() > current_score_dealer():
        return "You win!"
    elif current_score_player() == current_score_dealer():
        return "It's a draw."
    elif current_score_dealer() > 21:
        return "You win."
    else:
        return "You lose."

# ----------------------------------------------
# Ask the player if he wants to play.
want_to_play = False
while not want_to_play:
    question_play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    if question_play == 'y':
        want_to_play = True
        clear()
    elif question_play == 'n':
        quit()
    else:
        print(f"'{question_play}' is not a valid input, please try again.\n")

# ----------------------------------------------
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []

active_game = True
while active_game:
    print(logo)
    random_cards(player=cards, dealer=cards)

    # Running the game till the player doesn't want more cards.
    extra_round = False
    while not extra_round:
        ask_again = True

        if 11 in player_cards and current_score_player() > 21:
            target_index = player_cards.index(11)
            player_cards[target_index] = 1

        print(f"    Your cards: {player_cards}, current score: {current_score_player()}")
        print(f"    Dealer's first card: {current_score_dealer()}")

        if current_score_player() == 21:
            print("    Blackjack!")
            extra_round = True
            ask_again = False

        elif current_score_player() > 21:
            extra_round = True
            ask_again = False

        elif current_score_player() < 21:
            while ask_again:
                extra_card = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
                if extra_card == 'y':
                    extra_card_player()
                    ask_again = False
                elif extra_card == 'n':
                    extra_round = True
                    ask_again = False
                else:
                    print(f"'{extra_card}' is not a valid input, please try again.")

    extra_card_dealer()
    print(f"\n    Your final hand is {player_cards}, final score {current_score_player()}.")
    print(f"    The dealer's final hand is {dealer_cards}, final score {current_score_dealer()}.\n")
    print(f"    {compare_scores()}")

    play_again = True
    while play_again:
        new_game = input("\nDo you want to play again? Type 'y' to restart or 'n' to quit: ").lower()
        if new_game == 'y':
            play_again = False
        elif new_game == 'n':
            active_game = False
            play_again = False
        else:
            print(f"'{new_game}' is not a valid input, please try again.")

    player_cards = []
    dealer_cards = []
    clear()