# Calculator program containing multiple edits and updates.
# This is the final program.

import os
from logo import *

# Adding numbers
def add(n1, n2):
    """Adding numbers."""
    return n1 + n2

# Substracting numbers
def substract(n1, n2):
    """Substracting numbers."""
    return n1 - n2

# Multiplying numbers
def multiply(n1, n2):
    """Multiplying numbers."""
    return n1 * n2

# Dividing numbers
def divide(n1, n2):
    """Dividing numbers."""
    return n1 / n2

# Dict of operations
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def clear():  # Cross-platform clear screen
     os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    print(logo)
    num_1 = float(input("What is the first number?: "))

    # Showing all the operation keys
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:

        operation_symbol = input("Pick an operation: ")
        num_2 = float(input("What is the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num_1, num_2)

        print(f"{num_1} {operation_symbol} {num_2} = {answer}")


        if input(f"Type 'y' to continue calculating with {answer}, " 
                 "or type 'n' to start a new calculation: ") == "y":
            num_1 = answer
        else:
            should_continue = False
            clear()
            calculator()
calculator()