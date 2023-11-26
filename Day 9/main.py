from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the auction.")
running = True
dict = {}
lista = []


def find(bidding):
    highest = 0
    for bidder in bidding:
        amount = bidding[bidder]
        if amount > highest:
            highest = amount
            winner = bidder
    print(f"{winner} won with {highest}$.")


while running:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    dict[name] = bid
    print(dict)
    other = input("Are there any other bidders? Type yes or no\n")
    if other == "no":
        running = False
        find(dict)
    elif other == "yes":
        clear()
