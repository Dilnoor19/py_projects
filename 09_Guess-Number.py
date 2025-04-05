import random

def guess_the_number():
    number = random.randint(1, 100)
    guess = None
    while guess != number:
        guess = int(input("Guess the number (between 1 and 100): "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congrats! You've guessed the correct number!")
