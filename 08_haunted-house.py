import random

def haunted_house_game():
    print("Welcome to The Haunted House!")
    print("You find yourself in front of an old, eerie house. Do you dare to enter?")

    choice1 = input("Type 'yes' to enter or 'no' to run away: ").strip().lower()
    
    if choice1 == 'no':
        print("You run away, never to know what mysteries lie within. Game over.")
        return

    print("You step inside and see two doors: one on your left and one on your right.")
    choice2 = input("Which door do you choose? Type 'left' or 'right': ").strip().lower()
    
    if choice2 == 'left':
        print("You enter the left room and find out ! It looks friendly.")
        choice3 = input("Do you want to 'talk' to the ghost or 'run' away? ").strip().lower()
        
        if choice3 == 'talk':
            print("The ghost tells you about the history of the house. You gain valuable knowledge! You win!")
        else:
            print("You run back to the entrance. The ghost follows you, and you never escape! Game over.")
    
    elif choice2 == 'right':
        print("You enter the right room and see a treasure chest!")
        choice3 = input("Do you want to 'open' the chest or 'leave' it alone? ").strip().lower()
        
        if choice3 == 'open':
            if random.choice([True, False]):
                print("Congratulations! You found a pile of gold! You win!")
            else:
                print("The chest is a trap! You are caught inside. Game over.")
        else:
            print("You leave the chest alone and exit the house safely. But you missed out on treasure! Game over.")
    
    else:
        print("Invalid choice. The game ends here.")

# Start the game
haunted_house_game()
