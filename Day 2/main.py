#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.\n")
bill = float(input("What was the total bill? $"))
tip = input("What percentage tip would you like to to give? %")
people = int(input("How many people to split the bill? "))
percent = float("1." + tip)
result = round((bill * percent) / people, 2)
formatted_result = "{:.2f}".format(result)
print(f"Each person should pay: {formatted_result}$")