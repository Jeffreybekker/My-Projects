print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

prize = 0

if size == "S":
    if add_pepperoni == "Y":
        prize += 17
    else:
        prize += 15
elif size == "M":
    if add_pepperoni == "Y":
        prize += 23
    else:
        prize += 20
else:
    if add_pepperoni =="Y":
        prize += 28
    else:
        prize += 25


if extra_cheese == "Y":
    prize += 1
else:
    prize += 0

print(f"Your final bill is: ${prize}.")