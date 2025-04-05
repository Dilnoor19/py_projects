'''
1 for Rock
-1 for paper
0 for sciccor

'''
import random

computer = random.choice([1,0,-1]) 
youstr = input("Enter your choice (r for rock, p for paper, s for scissors): ")
youdict = {"r": 1, "p": 2, "s": 0}  
reversedict = {1: "rock", 2: "paper", 0: "sciccor"}

you = youdict.get(youstr, None) 

print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if you is None:
    print("Invalid input! Please choose 'r', 'p', or 's'.")
else:
    if computer == you: 
        print("It's a tie!")
    elif (you == 1 and computer == 0)  or (you == 2 and computer == 1) or (you == 0 and computer == 2):
        print("You win!")
    else:
        print("You lose!")