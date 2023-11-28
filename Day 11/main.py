from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
running = True

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

        next_card = deal_card(cards)
        computer_card = deal_card(cards)

        next_selected = cards[next_card]
        computer_selected = cards[computer_card]

        hand.append(next_selected)
                    
        score += next_selected                   

        print(f"Your cards: {hand}, score: {score}.")
        print(f"Computer's first card: {computer_selected}")
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
       