import random

running = True
while running:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
        while attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess > number:
                print("Too high.\nGuess again.\n")
            elif guess < number:
                print("Too low.\nGuess again.\n")
            elif guess == number :
                print(f"\nYou got it! The answer was {number}")
                running = False
                attempts = -1
            if guess != number:
                attempts -= 1
            if attempts == 0:
                print("\nYou lose.")
                running = False
    elif difficulty == "hard":
        attempts = 5
        while attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess > number:
                print("Too high.\nGuess again.\n")
            elif guess < number:
                print("Too low.\nGuess again.\n")
            elif guess == number :
                print(f"\nYou got it! The answer was {number}")
                running = False
                attempts = -1
            if guess != number:
                attempts -= 1
            if attempts == 0:
                print("\nYou lose.")
                running = False
