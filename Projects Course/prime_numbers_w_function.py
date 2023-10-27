# You need to write a function that checks whether if the number passed into it is a prime number or not.

# My code below:
def prime_checker(number):
    if n == 2 or n == 3 or n == 5 or n == 7:
        print("It's a prime number.")
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)


# ÑInstructor code below:
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)