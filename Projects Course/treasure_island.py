print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
choice_1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()

if choice_1 == "left":
    choice_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice_2 == "wait":
        choice_3 = input("You arrive at the island unharmed. There's a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice_3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice_3 == "yellow":
            choice_4 = input('You found the big treasure! Congratulations! Curious what is inside the treasure? Type "yes"!\n').lower()
            if choice_4 == "yes":
                print("A lot of shining mini gemstones with a great value are sparkling there!")
        elif choice_3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")