print("Welcome to treasure island !")
print("Your mission is to find treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go ? Type "Left" or "Right".').lower()

if choice1 =="left":
    choice2 = input('You\'ve come to a lake. Type "wait" to waiit for a boat or "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which colour do you choose ?").lower()
        if choice3 == "red":
            print("It's a room full of fire, Game Over !")
        elif choice3 == "yellow":
            print("You found the treasure, You Win !")
        elif choice3 == "blue":
            print("You enter a room of beasts, Game Over !")
        else:
            print("You choose a door that doesn't exist, Game Over !")
    else:
        print("You got attacked by an angry trout, Game Over !")
else:
    print("You fell into a hole, Game Over !")