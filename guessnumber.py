from random import randint
from guessnumberlogo import logo

easy_level_turns = 10
hard_level_turns = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You've got it ! The number is {answer}.")

def set_difficulty():
    level = str(input("Choose a difficulty. Type \"easy\" or \"hard\": ")).lower()
    if level =="easy":
        return easy_level_turns
    else:
        return hard_level_turns

def game():
    print(logo)
    print("Welcome to a Number Guessing game!")
    print("I'm thinking of a number between 1 to 100.\n")
    answer = randint(1, 100)
    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("\nYou've run out of guesses, you lose !")
            return
        elif guess != answer:
            print("guess again !")

game()