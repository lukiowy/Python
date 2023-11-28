############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
running = True
#print(logo)

def deal_card(cards):
    card = random.choice(cards)
    return card
 
def another(score, computer_score, is_running):
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "n":
        print(f"Your final hand: {hand}, final score: {score}")
        while computer_score < 17:
            computer_card = random.choice(cards)
            computer_selected = cards[computer_card]
            computer_hand.append(computer_selected)
            computer_score += computer_selected
        if computer_score > 21:
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            print(f"You win with {score} and computer got {computer_score}")
            is_running = False
            return is_running
        if computer_score > score and computer_score <= 21:
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            print(f"You lose with {score} and computer got {computer_score}")
            is_running = False
            return is_running
        if score > 21:
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            print(f"You lose with {score}")
            is_running = False
            return is_running
        if score <= 21 and score > computer_score:
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            print(f"You win with {score} and computer got {computer_score}")
            is_running = False
            return is_running
        if score == computer_score:
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            print("It's a draw")
            is_running = False
            return is_running

    elif another_card == "y" and score < 21 and computer_score < 21:
        print("asd")
        next_card = deal_card(cards)
        computer_card = deal_card(cards)

        next_selected = cards[next_card]
        computer_selected = cards[computer_card]

        hand.append(next_selected)
                    
        score += next_selected                   

        print(f"Your cards: {hand}, score: {score}.")
        print(f"Computer's first card: {computer_selected}")
        print(computer_score)
        if score > 21:
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            print(f"You lose with {score}")
            is_running = False
            return is_running
        if score <= 21 and computer_score <= 21:
            if score > computer_score:
                print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
                print(f"You win with {score} and computer got {computer_score}")
                is_running = False
                return is_running
            elif computer_score > computer_score:
                print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
                print(f"You lose with {score}")
                is_running = False
                return is_running
        if score == computer_score:
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            print("It's a draw")
            is_running = False
            return is_running
        
        else:
            computer_hand.append(computer_selected)
            computer_score += computer_selected
            another(score, computer_score, is_running)

while running:
    print(logo)
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    hand = []
    computer_hand = []
    score = 0
    computer_score = 0
    if start == "n":
        print("Goodbye :)")
        running = False
    else:
        for i in range(2):
            card = deal_card(cards)
            computer_card = deal_card(cards)
            selected_card = cards[card]
            selected_computer_card = cards[computer_card]
            hand.append(selected_card)
            computer_hand.append(selected_computer_card)
            score += selected_card
            computer_score += selected_computer_card
 
        print(f"Your cards: {hand}, score: {score}.")
        print(f"Computer's first card: {selected_computer_card}.")

        if score < 21:
            another(score, computer_score, running)
       