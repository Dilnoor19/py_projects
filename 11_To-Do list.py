def todo_list():
    tasks = []
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"'{task}' has been added to your to-do list.")
        elif choice == "2":
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f"'{task}' has been removed from your to-do list.")
            else:
                print(f"'{task}' not found in your to-do list.")
        elif choice == "3":
            if tasks:
                print("\nYour To-Do List:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
            else:
                print("Your to-do list is empty.")
        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")

todo_list()