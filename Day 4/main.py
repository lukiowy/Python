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

choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
options = [rock, paper, scissors]
rand_int = random.randint(0, 2)
if choice >= 0 and choice <= 2:
    print(options[choice])
    print("Enemy chose: ")
    print(options[rand_int])
else:
    print("You've entered invalid number, you lost!")

if (choice == 0 and rand_int == 1) or (choice == 1 and rand_int == 2) or (
        choice == 2 and rand_int == 0):
    print("You lose!")
elif (choice == 0 and rand_int == 0) or (choice == 1 and rand_int == 1) or (
        choice == 2 and rand_int == 2):
    print("It's a draw!")
elif (choice == 0 and rand_int == 2) or (choice == 1 and rand_int == 0) or (
        choice == 2 and rand_int == 1):
    print("You won!")
