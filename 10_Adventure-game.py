def adventure_game():
    print("Welcome to the Adventure Game!")
    print("You're in a dark forest. There are two paths ahead.")
    print("1. Go left")
    print("2. Go right")

    choice = input("Which path will you take (1 or 2)? ")

    if choice == "1":
        print("You encounter a wild bear! Run!")
    elif choice == "2":
        print("You find a hidden treasure chest! Congratulations!")
    else:
        print("Invalid choice. Game over.")

adventure_game()
