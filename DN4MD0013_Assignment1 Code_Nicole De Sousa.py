# Task Tracker Tool
# Name: Nicole De Sousa

# Create the data structure (dictionary)
tasks = {}  # Key = task_id, Value = task detailstask_id = int

print("Simple Task Tracker — menu")
# Create a simple menu loop
while True:
    print("\n1 Add task")
    print("2 Mark task complete")
    print("3 Retrieve task by ID")
    print("4 Get next task by priority")
    print("5 Exit")
    choice = input("Choose (1-5): ").strip()

    # Add-task option (store a task record)
    if choice == "1":
        task_id = input("Task ID: ").strip()
        if task_id in tasks:
            print("That ID already exists.")
        else:
            desc = input("Description: ").strip()
            p_text = input("Priority (1 = highest): ").strip()
            try:
                priority = int(p_text)
                tasks[task_id] = {
                    "id": task_id,
                    "description": desc,
                    "priority": priority,
                    "status": "open",
                }
                print("Task added.")
            except ValueError:
                print("Priority must be a number. Task not added.")

    # Mark a task as complete
    elif choice == "2":
        task_id = input("Task ID to complete: ").strip()
        if task_id not in tasks:
            print("Task not found.")
        else:
            tasks[task_id]["status"] = "complete"
            print("Task marked complete.")

    # Retrieve a task by ID
    elif choice == "3":
        task_id = input("Task ID to retrieve: ").strip()
        if task_id not in tasks:
            print("Task not found.")
        else:
            t = tasks[task_id]
            print("\nFOUND:")
            print(t)
            # Optional clearer output
            print("ID:", t["id"])
            print("Description:", t["description"])
            print("Priority:", t["priority"])
            print("Status:", t["status"])

    # Get the next task by priority
    elif choice == "4":
        next_task = None
        for t in tasks.values():
            if t["status"] == "open":
                if next_task is None or t["priority"] < next_task["priority"]:
                    next_task = t
        if next_task is None:
            print("No open tasks.")
        else:
            print("\nNEXT TASK:")
            print(next_task)
            print("ID:", next_task["id"])
            print("Description:", next_task["description"])
            print("Priority:", next_task["priority"])
            print("Status:", next_task["status"])  # will always be 'open' here

    # Exit cleanly
    elif choice == "5":
        print("Goodbye.")
        break
    else:
        print("Invalid option.")
    
