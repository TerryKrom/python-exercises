# a CMD to do list!
todo_list = []

while True:
    print('\n', '='*5, 'Menu', '='*5)
    print(f"Your tasks: \n{todo_list}")
    print("\nTo add a task enter 1\nTo remove a task enter 2\nTo exit enter 3\n")
    action = int(input("Enter the code: "))

    if action == 3:
        print("See you later!")
        break
    elif action == 1:
        task = input("Enter the task: ")
        todo_list.append(task)
        print(f"Task '{task}' added.")
    elif action == 2:
        task_to_remove = input("What do you want to remove? ")
        if task_to_remove in todo_list:
            todo_list.remove(task_to_remove)
            print(f"Task '{task_to_remove}' removed.")
        else:
            print("Task not found!")
    else:
        print("Invalid input. Please enter 1, 2, or 3.")