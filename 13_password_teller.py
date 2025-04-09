import random

# Data pools
char = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ["!","@","$","#","%","^","&","*","_","/"]

# Getting user inputs
password_length = int(input("Enter password length: "))
char_input = int(input("Enter how many alphabets in password: "))
numbers_input = int(input("Enter how many numbers in password: "))
symbols_input = int(input("Enter how many symbols in password: "))

if char_input + symbols_input + numbers_input != password_length:
    print("Error: Total characters don't match the password length!")
else:
    password_list = []

    for i in range(char_input):
        password_list.append(random.choice(char))

    for i in range(numbers_input):
        password_list.append(str(random.choice(numbers)))

    for i in range(symbols_input):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)  


    # Convert list to string
    password = "".join(password_list)
    print("Your password is:", password)