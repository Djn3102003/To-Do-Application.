
#To_Do Application

tasks = []
next_id = 1


def add_task():
    global next_id

    description = input("Enter task description: ").strip()

    if description == "":
        print("Task description cannot be empty!")
        return

    task = {
        "id": next_id,
        "description": description,
        "status": "Pending"
    }

    tasks.append(task)
    print("Task added successfully!")
    print("Your Task ID is:", next_id)

    next_id += 1


def view_tasks():
    if not tasks:
        print("No tasks found. Please add a task first.")
        return

    print("\n===== YOUR TASKS =====")

    for task in tasks:
        print("--------------------")
        print("ID:", task["id"])
        print("Task:", task["description"])
        print("Status:", task["status"])


def find_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def update_task():
    try:
        task_id = int(input("Enter task ID to update: "))
        task = find_task(task_id)

        if task is not None:
            new_description = input(
                "Enter new task description: "
            ).strip()

            if new_description == "":
                print("Task description cannot be empty!")
            else:
                task["description"] = new_description
                print("Task updated successfully!")
        else:
            print("Error: Task ID not found!")

    except ValueError:
        print("Invalid input! Please enter a numeric ID.")


def complete_task():
    try:
        task_id = int(input("Enter task ID to complete: "))
        task = find_task(task_id)

        if task is not None:
            if task["status"] == "Pending":
                task["status"] = "Completed"
                print("Task marked as completed!")
            else:
                print("This task is already completed.")
        else:
            print("Error: Task ID not found!")

    except ValueError:
        print("Invalid input! Please enter a numeric ID.")


def delete_task():
    try:
        task_id = int(input("Enter task ID to delete: "))
        task = find_task(task_id)

        if task is not None:
            tasks.remove(task)
            print("Task deleted successfully!")
        else:
            print("Error: Task ID not found!")

    except ValueError:
        print("Invalid input! Please enter a numeric ID.")


def main():
    while True:
        print("\n===== TODO APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    add_task()

                case 2:
                    view_tasks()

                case 3:
                    update_task()

                case 4:
                    complete_task()

                case 5:
                    delete_task()

                case 6:
                    print("Thank you for using the TODO Application!")
                    break

                case _:
                    print("Invalid choice! Please select 1 to 6.")

        except ValueError:
            print("Invalid input! Please enter a number.")



main()
