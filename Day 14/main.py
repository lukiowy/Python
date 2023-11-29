import art
from game_data import data
import random

score = 0

def random_person():
    length = random.randint(0, len(data)-1)
    print(f"{data[length]['name']}, {data[length]['description']}, from {data[length]['country']}")
    followers = data[length]['follower_count']
    return followers

def compare(choice,score,running):
    if choice == "A" and first_followers > second_followers:
        score += 1
        return score
    
    elif choice == "A" and first_followers < second_followers:
        print(f"You lose with score: {score}.")
        running = False
        return running
    
    elif choice == "B" and first_followers < second_followers:
        score += 1
        return score
    
    elif choice == "B" and first_followers > second_followers:
        print(f"You lose with score: {score}.")
        running = False
        return running
    
running = True
while running:
    print(art.logo)

    if score > 0:
        print(f"Good job! Current score: {score}")

    print("Compare A:")
    first_followers = random_person()
    #print(first_followers)
    print(art.vs)
    
    print("Compare B:")
    second_followers = random_person()
    #print(second_followers)

    choice = input("Who has more followers? Type 'A' or 'B': ")
    score = compare(choice,score,running)
    if score == False:
        running = score
