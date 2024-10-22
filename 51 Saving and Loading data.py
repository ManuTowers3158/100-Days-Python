# # Day 51 Challenge Requirements
#
# - **Objective:**
#   - Enhance the to-do list manager from Day 35 by adding auto-save and auto-load functionalities.
#
import os, time  # Import necessary modules for system commands and delays


def printList():
    # Print each item in the agenda
    print()
    for item in my_agenda:
        print(item)
    print()


def check_duplicates(item):
    # Check if an item is already in the agenda
    if item in my_agenda:
        print("Item already in agenda")  # Inform the user
        time.sleep(2)  # Pause for 2 seconds
        return True
    else:
        return False


my_agenda = []  # Initialize an empty agenda
f = open("Support Files/my agenda.txt", "r")  # Open the agenda file for reading
my_agenda = eval(f.read())  # Load existing agenda items
f.close()  # Close the file

while True:
    os.system("cls")  # Clear the console
    print("To do list Manager")
    menu = input(
        "What do you want to do?:\n1. View complete list\n2. Add an item\n3. Edit an item\n4. Remove an item\n5. Delete complete list\n6. Exit\n>>> ")

    if menu == "1":
        # View current agenda
        print("Your current agenda is: ")
        printList()
        time.sleep(3)

    elif menu == "2":
        # Add a new item to the agenda
        item = input("What do you want to add?: ")
        if not check_duplicates(item):
            my_agenda.append(item)  # Add the item if it's not a duplicate
            print("Item added")
        time.sleep(1)

    elif menu == "3":
        # Edit an existing item in the agenda
        print("Current agenda is:")
        printList()
        item = input("What do you want to edit?: ")
        if item in my_agenda:
            item35 = input("What do you want to replace it with?:")
            if not check_duplicates(item35):
                my_agenda.remove(item)  # Replace the item
                my_agenda.append(item35)
                print("Item replaced")
                time.sleep(2)
        else:
            print("Item not in agenda")

    elif menu == "4":
        # Remove an item from the agenda
        print("Current agenda is:")
        printList()
        item = input("What do you want to delete?: ")
        if item in my_agenda:
            confirmation = input("Are you sure you want to delete it?:\n1.Yes\n2.No\n>>> ")
            if confirmation == "1":
                my_agenda.remove(item)  # Remove the item
                print("Item removed")
                time.sleep(2)

    elif menu == "5":
        my_agenda = []  # Clear the entire agenda

    elif menu == "6":
        # Save the agenda to the file and exit
        f = open("Support Files/my agenda.txt", "w")
        f.write(str(my_agenda))  # Write the current agenda to the file
        f.close()
        break

    else:
        print("Option not valid")  # Inform the user of invalid option





