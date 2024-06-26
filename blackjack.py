from blackjacklogo import logo
import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponents has BLACKJACK 😱"
    elif user_score == 0:
        return "Win with BLACKJACK 😎"
    elif user_score > 21:
        return "You went over, you lose 😭"
    elif computer_score > 21:
        return "Opponent went over, you win 😁"
    elif user_score > computer_score:
        return "You win 😀"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User Cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer Card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = str(input("Type \"y\" to get another card, type \"n\" to pass: ")).lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nUser cards: {user_cards}, User score: {user_score}\nComputer cards: {computer_cards}, Computer score: {computer_score}")
    print(compare(user_score, computer_score))

while str(input("Do you want to play game of BLACKJACK? Type \"y\" or \"n\": ")) == "y":
    os.system('cls')
    play_game()