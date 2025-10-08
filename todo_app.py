FILENAME = "todo_list.txt"


def load_tasks():
    """Loads tasks from the text file."""
    try:
        with open(FILENAME, 'r') as file:
            # Read all lines and strip newline characters
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        tasks = []
    return tasks


def save_tasks(tasks):
    """Saves the entire list of tasks to the text file, overwriting it."""
    with open(FILENAME, 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def display_tasks(tasks):
    """Displays all current tasks to the user."""
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("-----------------------\n")


def add_task(tasks):
    """Adds a new task to the list."""
    new_task = input("Enter the new task: ")
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"✅ Task '{new_task}' added successfully.")
    else:
        print("⚠️ Task cannot be empty.")


def remove_task(tasks):
    """Removes a task from the list based on its number."""
    if not tasks:
        print("⚠️ No tasks to remove.")
        return

    display_tasks(tasks)
    try:
        task_num_to_remove = int(input("Enter the task number to remove: "))
        if 1 <= task_num_to_remove <= len(tasks):
            # Adjust for 0-based index
            removed_task = tasks.pop(task_num_to_remove - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed_task}' removed successfully.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")
        print("===========================")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()