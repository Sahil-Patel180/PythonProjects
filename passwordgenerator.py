import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
symbols = ["!","#","$","%","&","(",")","*","+",]
numbers = ["1","2","3","4","5","6","7","8","9","0"]

want_letters = int(input("How many letters you need ?\n"))
want_symbols = int(input("How many symbols you need ?\n"))
want_numbers = int(input("How many numbers you need ?\n"))

password_list = []
for char in range(1, want_letters + 1):
    password_list += random.choice(letters)

for sym in range(1, want_symbols + 1):
    password_list += random.choice(symbols)

for num in range(1, want_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
password = ""
for final in password_list:
    password += final
print(f"Your password is: {password}")