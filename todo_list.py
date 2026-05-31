tasks = []

def show_tasks():
    if not tasks:
        print("\nYour To-Do List is empty!")
    else:
        print("\n--- Your Current Tasks ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

while True:
    print("\n1. View Tasks | 2. Add Task | 3. Delete Task | 4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        new_task = input("Enter the new task: ")
        if new_task.strip() != "":
            tasks.append(new_task)
            print(f"'{new_task}' added successfully.")
        else:
            print("Task cannot be empty!")
    elif choice == "3":
        show_tasks()
        if tasks:
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"'{removed}' deleted successfully.")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1 and 4.")