#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for i in range(0, nr_letters):
    rand_letter = random.randint(0, len(letters))
    password += letters[rand_letter - 1]

for i in range(0, nr_symbols):
    rand_symbol = random.randint(0, len(symbols))
    password += symbols[rand_symbol - 1]

for i in range(0, nr_numbers):
    rand_number = random.randint(0, len(numbers))
    password += numbers[rand_number - 1]

print("Your password:")
print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []
for i in range(0, nr_letters):
    rand_letter = random.randint(0, len(letters))
    password.append(letters[rand_letter - 1])

for i in range(0, nr_symbols):
    rand_symbol = random.randint(0, len(symbols))
    password.append(symbols[rand_symbol - 1])

for i in range(0, nr_numbers):
    rand_number = random.randint(0, len(numbers))
    password.append(numbers[rand_number - 1])
    
random.shuffle(password)
j = ""
for i in password:
    j += i
print("Your more randomized password")
print(j)
