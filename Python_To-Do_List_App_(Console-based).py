def display_menu():
    print("\n==== To-Do List Menu ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for idx, (task, completed) in enumerate(tasks, 1):
            status = "✓" if completed else "✗"
            print(f"{idx}. [{status}] {task}")

def add_task(tasks):
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append((task, False))
        print("Task added.")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter the task number to remove: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            print(f"Removed task: {removed[0]}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_completed(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter the task number to mark as completed: "))
        if 1 <= idx <= len(tasks):
            task, _ = tasks[idx - 1]
            tasks[idx - 1] = (task, True)
            print(f"Marked '{task}' as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()