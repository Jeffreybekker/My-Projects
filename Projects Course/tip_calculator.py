#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? €"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15: "))
people = int(input("How many people to split the bill? "))

total_price_person = bill * ((100 + tip) / 100) / people
rounded_total = "{:.2f}".format(total_price_person)     # round(total_price_person, 2)

print(f"Every person has to pay €{rounded_total}.")