# Create the data structure (dictionary)
tasks = {} # Key = task_id, Value = task detailstask_id = int

#The below print line will introduce the Task Tracker 2.0 to the user
print("Welcome to Task Tracker 2.0 :)")

# Create a simple menu loop
while True:
    #This introduces the Menu Options
    print("Menu Options: ")
    #This lets user know option 1 will allow them to Add a task.
    print("\n1 Add task")
    #This lets user know option 2 will allow them to mark a task as complete
    print("2 Mark task complete")
    #This lets user know option 3 will allow them to retrieve a task.
    print("3 Retrieve task by ID")
    #This lets user know option 4 will let them get the next task by highest priority. 
    print("4 Get next task by priority")
    #This lets user know option 5 will end  the software.
    print("5 Exit")
    # 'Choice' is created as a variable and the user input will be stored as it's value.
    choice = input("Choose (1-5): ").strip()

 # This IF statement will run if the user inputs 1. Add-task option (store a task record).
    if choice == "1":
        # 'task_id' is a new variable and the user input will be stored as it's value.
        task_id = input("Task ID: ").strip()
        # This IF statement checks if the user's input for task ID already exists in the dictionary.
        if task_id in tasks:
           # If it task ID already exists, system will out this message to let the user know. 
           print("That ID already exists.")
        # If the task ID doesn't already exist, the system will proceed with this ELSE statement.
        else:
            # 'desc' is a new variable and the user will input it's value (This is the description of the task).
            desc = input("Description: ").strip()
            # 'p_text' is a new variable and the user will input it's value (This is the priority of the task).
            p_text = input("Priority (1 = highest): ").strip()
            try:
                # This checks that the priority the user inputted is an integer.
                priority = int(p_text)
                # This then stores the user inputs in the tasks dictionary linking the description, priority and status to the task id.
                tasks[task_id] = {
                    "id": task_id,
                    "description": desc,
                    "priority": priority,
                    # Staus is set to 'Open' by default as user will only ever enter an open task to begin with. 
                    "status": "open",
                }
                # It will output the below to let the user know this has been sucessfully added.
                print("Task added.")
            # This except is a check to see if the Priority entered was a number. If not it will output the below message to let the user know this and inform them the task was not added.
            except ValueError:
                print("Priority must be a number. Task not added.")
     
     # This elif statement will run if the user inputs 2. Mark a task as complete. 
    elif choice == "2":
         # 'task_id' is a variable and the user input will be stored as it's value.
         task_id = input("Task ID to complete: ").strip()
         # If the task id inputted by the user is not within 'tasks' dictionary, it will output the below message to let the user know the task doesn't exist.
         if task_id not in tasks:
            print("Task not found.")
         else:
             # If the task id inputted does exist, it will update the status to 'complete' and output the below message to let the user know the action is completed. 
             tasks[task_id]["status"] = "complete"
             print("Task marked complete.")

 # This elif statement will run if the user inputs 3. Retrieve a task by ID.
    elif choice == "3":
        # 'task_id' is a variable and the user input will be stored as it's value.
        task_id = input("Task ID to retrieve: ").strip()
        # If the task id inputted by the user is not within 'tasks' dictionary, it will output the below message to let the user know the task doesn't exist.
        if task_id not in tasks:
           print("Task not found.")
        else:
        # If the task id inputted by the user does exist within tasks dictionary, it will store it to variable 't' and then use that varible to output the related data below.
            t = tasks[task_id]
            print("\nFOUND:")
            print(t)
 # Optional clearer output
            # This will print the id linked to variable t
            print("ID:", t["id"])
            # This will print the description linked to variable t
            print("Description:", t["description"])
            # This will print the priority linked to variable t
            print("Priority:", t["priority"])
            # This will print the id linked to variable t
            print("Status:", t["status"])

 # This elif statement will run if the user inputs 4. Get the next task by priority
    elif choice == "4":
       # This assigned None to a new variable called next_task.
       next_task = None
       for t in tasks.values():
           # This checks all the tasks and if their status is set to open.
           if t["status"] == "open":
               if next_task is None or t["priority"] < next_task["priority"]:
                   # This stores the highest priority task value to 'next_task' variable.
                   next_task = t
       # If there are no open tasks it will output the below to let the user know.             
       if next_task is None:
           print("No open tasks.")
       else:
           # If there are open tasks with high priority, it will print the below to inform the user of the task. 
           print(next_task)
           print("ID:", next_task["id"])
           print("Description:", next_task["description"])
           print("Priority:", next_task["priority"])
           print("Status:", next_task["status"]) # will always be 'open' here
    # Exit 

 # This elif statement will run if the user inputs 5. Exit the software.
    elif choice == "5":
      # It will print Goodbye as a message to the user before ending the program.
      print("Goodbye.")
      break
    else:
      # If the user inputs an option that is not numbers 1-5, it will output the below message to let them know they have entered an invalid option.
      print("Invalid option.")
