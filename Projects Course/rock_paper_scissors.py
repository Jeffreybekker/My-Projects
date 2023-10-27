# Create a rock, paper and scissor game against the computer.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]
my_pick = int(input("What gesture do you choose? 1 for rock, 2 for paper, 3 for scissors: "))
print(f"You picked: {game_images[my_pick - 1]}")

# Computer pick and compare
number_of_gestures = len(game_images)
random_number = random.randint(0, number_of_gestures - 1)
print(f"The computer picked: {game_images[random_number]}")

if random_number == 0 and my_pick == 1:
    print("It's a draw.")
elif random_number == 0 and my_pick == 2:
    print("You win!")
elif random_number == 0 and my_pick == 3:
    print("The computer wins.")

elif random_number == 1 and my_pick == 1:
    print("The computer wins.")
elif random_number == 1 and my_pick == 2:
    print("It's a draw.")
elif random_number == 1 and my_pick == 3:
    print("You win!")

elif random_number == 2 and my_pick == 1:
    print("You win!")
elif random_number == 2 and my_pick == 2:
    print("The computer wins.")
else:
    print("It's a draw.")