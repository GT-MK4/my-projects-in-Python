task = []

while True:

print("\n--- TO DO LIST MENU ---")

print("1: Add task")

print("2: View task")

print("3: Delete task")

print("4: Exist")



choice = input("Select a option (1-4):")



if choice == "1":

    # Add new task

    new_task = input("Enter your task: ")

    task.append(new_task)

    print("Task added sucessfully")



elif choice == "2":

    # View task

    if not task:

        print("list empty")

    else:

        print("\nYour current Task")

        for index, task in enumerate:

            print(f"{index}. {task}")

elif choice == "3":

    # View task

    if not task:

        print("nothing to delete")

    else:

        print("\nChoose number of the task to delete: ")

        for index, task in enumerate(task, 1):

            print(f"{index}. {task}")

        try:

            task_num = int(input("Task number: "))

            removed = task.pop(task_num - 1)

            print(f"Deleted: '{removed}'")

        except (ValueError, IndexError):

            print("Invalid number")



elif choice == "4":

    # Exit or stop script

    print("Exiting...")

    break



else:

    print("Invalid choice")``