import json
from datetime import datetime

def load_todo_list():
    try:
        with open("todo_list.json", "r") as file:
            todo_list = json.load(file)
    except FileNotFoundError:
        todo_list = []
    return todo_list

def save_todo_list(todo_list):
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file, indent=2)

def display_todo_list(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task['description']} - {task['date']}")

def add_task(todo_list, description):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = {"description": description, "date": timestamp}
    todo_list.append(task)
    print(f"Task added: {description}")

def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task removed: {removed_task['description']}")
    else:
        print("Invalid task index. Please enter a valid index.")

def update_task(todo_list, task_index, new_description):
    if 1 <= task_index <= len(todo_list):
        todo_list[task_index - 1]["description"] = new_description
        print(f"Task updated: {new_description}")
    else:
        print("Invalid task index. Please enter a valid index.")

def main():
    print("Welcome to the To-Do List App!")

    while True:
        todo_list = load_todo_list()

        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. View To-Do List")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            add_task(todo_list, description)
            save_todo_list(todo_list)

        elif choice == "2":
            task_index = int(input("Enter task index to remove: "))
            remove_task(todo_list, task_index)
            save_todo_list(todo_list)

        elif choice == "3":
            task_index = int(input("Enter task index to update: "))
            new_description = input("Enter new task description: ")
            update_task(todo_list, task_index, new_description)
            save_todo_list(todo_list)

        elif choice == "4":
            display_todo_list(todo_list)

        elif choice == "0":
            print("Exiting the To-Do List App. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
