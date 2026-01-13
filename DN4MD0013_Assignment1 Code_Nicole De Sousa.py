# Starting with an empty dictionary for tasks
tasks = {}

# This function is for adding a task to the tasks dictionary. This will be used when the user picks option '1. Add task'.
def add_task():
    # Asks the user to input an integer to be the Task ID number for this task.
    task_id = int(input("Enter Task ID (unique number): "))
    while task_id in tasks:
        # This is a validation check to see if the Task ID already exists. I used a while loop, so it will keep asking the user to input a Task ID until they pick a unique one that hasn't been used already. 
        print("Error: Task ID already exists.\n")
        task_id = int(input("Enter Task ID (unique number): "))

    # This asks the user to input a description of the task.
    description = input("Enter Task Description: ")

    # This stores the 3 priorities.
    valid_priorities = ["high", "medium", "low"]
    priority = input("Enter Priority (high/medium/low): ").lower()
    while priority not in valid_priorities:
         # This is a validation check to ensure the user inputs a correct priority level. I used a while loop, so it will keep asking the user to input a priority until they pick high/medium/low.
        print("Incorrect priority! Please enter 'high', 'medium', or 'low'.")
        priority = input("Enter Priority (high/medium/low): ").lower()

    # This stores the open or closed status. 
    valid_statuses = ["open", "close"]
    status = input("Enter Status (open/close): ").lower()
    while status not in valid_statuses:
        # This is a validation check to ensure the user inputs either open or closed for a status. 
        print("Invalid status! Please enter 'open' or 'close'.")
        status = input("Enter Status (open/close): ").lower()

    # Store the task details in the dictionary.
    tasks[task_id] = {
        "ID": task_id,
        "description": description,
        "priority": priority,
        "status": status
    }
    print(f"Task {task_id} added successfully!\n")

# This function pulls all the current tasks.
def view_tasks():
    if not tasks:
        # If there are no tasks, it will output the below message to let users know.
        print("\nNo tasks available.")
        return
    print("\nCurrent Tasks:")
    # This will output the list of tasks. 
    for task_id, task_info in tasks.items():
        print(f"ID: {task_id}, Description: {task_info['description']}, "
              f"Priority: {task_info['priority']}, Status: {task_info['status']}")

#This function marks Tasks as complete by changing their status from open to close.
def mark_complete():
    task_id = int(input("Enter Task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "close"
        print(f"Task {task_id} marked as complete.\n")
    else:
        # This is a validation message, if the user inputs an incorrect task ID. 
        print("Task ID not found.\n")

#This function retrieves a task by asking the user to input the ID.
def retrieve_by_id():
    task_id = int(input("Enter Task ID to retrieve: "))
    if task_id in tasks:
        task = tasks[task_id]
        print(f"\nTask Details: ID: {task['ID']}, Description: {task['description']}, "
              f"Priority: {task['priority']}, Status: {task['status']}\n")
    else:
          # This is a validation message, if the user inputs an incorrect task ID. 
        print("Task ID not found.\n")

# This function retrieves the next task by priority status. It looks for tasks that are still 'open' and picks the one with the highest priority
def next_task():
    # Filter open tasks
    open_tasks = [task for task in tasks.values() if task["status"] == "open"]
    if not open_tasks:
        print("No open tasks available.\n")
        return

    # Sort by priority: high > medium > low
    priority_order = {"high": 1, "medium": 2, "low": 3}
    open_tasks.sort(key=lambda t: priority_order[t["priority"]])

    next_task = open_tasks[0]
    print(f"\nNext Task: ID: {next_task['ID']}, Description: {next_task['description']}, "
          f"Priority: {next_task['priority']}, Status: {next_task['status']}\n")

# This is the main loop which will keep running until the user picks option 6 to exit. 
while True:
    print("Welcome to Task Tracker 2.0")
    print("\nOptions:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Complete")
    print("4. Retrieve Task by ID")
    print("5. Retrieve Next Task by Priority")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        retrieve_by_id()
    elif choice == "5":
        next_task()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
