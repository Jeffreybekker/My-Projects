from Menu import *

QUARTERS = 0.25
DIMES = 0.10
NICKELS = 0.05
PENNIES = 0.01

profit = 0

def coins():
    """Returns the total amount of money from the coins that are put in."""
    print("Please insert coins.")
    total = int(input("How many quaters?: ")) * QUARTERS
    total += int(input("How many dimes?: ")) * DIMES
    total += int(input("How many nickels?: ")) * NICKELS
    total += int(input("How many pennies?: ")) * PENNIES
    return total


def report_resources():
    """Checking how much water, milk and coffee there's left."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
    return


def resource_enough(order_ingredients):
    """Returns True when order can be made, False if there's not enough ingredients."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there's not enough {item}.")
            return False
    return True


def make_coffee(drink_name, order_ingredients):
    """Deducting required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy your coffee!")


def transaction_successful(money_recieved, drink_cost):
    """Return True when the payment is accepted, or False when there's not enough money"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
    

is_on = True

while is_on:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_choice == "espresso" or coffee_choice == "latte" or coffee_choice == "cappuccino":
        drink = MENU[coffee_choice]
        if resource_enough(drink["ingredients"]):
            payment = coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(coffee_choice, drink["ingredients"])
    elif coffee_choice == "report":
        report_resources()
    elif coffee_choice == "off":
        is_on = False
    else:
        print("Invalid choice. Please try again.")