print("Ticket Generator !")
person_height = int(input("What is your height?\n"))
bill = 0

if person_height > 150:
    person_age = int(input("What is your age ?\n"))
    if person_age >= 12:
        bill = 7
        print("Child fare, you have to pay $7")
    elif person_age >= 18:
        bill = 12
        print("Adult fare, you have to pay $12")
    elif person_age >= 45:
        print("Senior Citizen has no fare to pay !")
    else:
        print("false age, sorry you are not allowed for ride")
    want_photo = input("Do you want photos ? Y or N\n").lower()
    if want_photo == "y":
        bill += 3
            
    print(f"You have to pay: ${bill}")
else:
    print("Sorry you have to grow height !")
    
