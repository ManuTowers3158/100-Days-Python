
import time
import os
def prettyPrint(list2D):
    # Print a formatted 2D list
    print()
    for row in list2D:
        for item in row:
            print(f"{item:^10}", end=" | ")  # Center each item in a field of width 10
        print()  # New line after each row
    print()

todolist = []  # Initialize an empty to-do list
todolist_priority = []  # List to hold prioritized tasks

while True:
    # Display menu options
    menu = int(input("1. Add\n2. View\n3. Edit\n4. Remove\n>>> "))
    if menu == 1:
        # Adding a new task
        item = input("Task Name: ")
        duedate = input("Due Date: ")
        priority = input("Priority: ")
        row = [item, duedate, priority]  # Create a new task record
        todolist.append(row)  # Add the task to the to-do list
        os.system("cls")
        print("Tarea agregada jefe")  # Confirm addition
        time.sleep(1)

    if menu == 2:
        # Viewing tasks
        menu2 = int(input("1. View by creation date\n2. View by priority\n>>> "))
        if menu2 == 1:
            os.system("cls")
            prettyPrint(todolist)  # Print tasks by creation date
            time.sleep(1)
        if menu2 == 2:
            # View tasks by priority
            todolist_priority = []  # Reset priority list
            for row in range(len(todolist)):
                priority = todolist[row][2]
                if priority in ["High", "Medium", "Low"]:  # Group tasks by priority
                    todolist_priority.append(todolist[row])

            os.system("cls")
            prettyPrint(todolist_priority)  # Print prioritized tasks
            time.sleep(1)

    if menu == 3:
        # Editing an existing task
        os.system("cls")
        prettyPrint(todolist)  # Display current tasks
        edit = input("Which task do you want to edit?\n>>> ")
        for row in range(len(todolist)):
            task = todolist[row][0]
            if edit == task:
                # Prompt for which aspect to change
                menu3 = int(input("What do you want to change?\n1. Task Name \n2. Due Date\n3. Priority\n>>> "))
                if menu3 == 1:
                    NTaskName = input("New Task name\n>>> ")
                    todolist[row][0] = NTaskName  # Update task name
                if menu3 == 2:
                    NDuedate = input("New Task due date\n>>> ")
                    todolist[row][1] = NDuedate  # Update due date
                if menu3 == 3:
                    NPriority = input("New Task Priority\n>>> ")
                    todolist[row][2] = NPriority  # Update priority
                print("Tarea modificada jefe\n")  # Confirm modification

    if menu == 4:
        # Removing a task
        os.system("cls")
        prettyPrint(todolist)  # Display current tasks
        Removeitem = input("Which task do you want to remove?\n>>> ")
        for row in todolist:
            if Removeitem in row:  # Check for the task to remove
                todolist.remove(row)  # Remove the task
                os.system("cls")
                print("Tarea quitada jefe")  # Confirm removal
                time.sleep(1)
