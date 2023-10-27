from logo_bidding import logo
import os

print("Welcome to the blind auction!")
print(logo)

name_and_bid = {}

def clear():  # Cross-platform clear screen
     os.system('cls' if os.name == 'nt' else 'clear')

def add_new_bidders(name, price):
    name_and_bid[name] = price
    name_and_bid.update(name_and_bid)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of €{highest_bid}.")

active_auction = True
while active_auction:

    ask_name = input("What is your name?: ").title()
    ask_bid = int(input("What is your bid?: €"))

    add_new_bidders(name=ask_name, price=ask_bid)

    answer_others = True
    while answer_others:
        ask_others = input("Are there any other bidders 'yes' or 'no'?: ").lower()

        if ask_others == "yes":
            active_auction = True
            answer_others = False
            clear()
        elif ask_others == "no":
            active_auction = False
            answer_others = False
        else:
            answer_others = True

find_highest_bidder(name_and_bid)