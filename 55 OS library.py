# Simple To-Do List Manager that allows viewing, adding, editing, and removing items from an agenda list.
# The agenda is saved to a file upon exiting, and a backup is created.

import os, time  # Import necessary modules


# Function to print the current agenda
def printList():
    print()  # Print a blank line
    for item in my_agenda:  # Iterate through and print each item in the agenda
        print(item)
    print()


# Function to check for duplicate items in the agenda
def check_duplicates(item):
    if item in my_agenda:  # Check if the item already exists
        print("Item already in agenda")
        time.sleep(2)  # Pause for 2 seconds
        return True  # Return True if duplicate
    else:
        return False  # Return False if no duplicate


my_agenda = []  # Initialize an empty agenda list
files = os.listdir()  # Get a list of files in the current directory

# Check if a backup folder exists, if not, create it
if "backup" not in files:
    os.mkdir("backup")  # Create a backup directory

# Open and read the agenda from a file
f = open("Support Files/my agenda.txt", "r")
my_agenda = eval(f.read())  # Load the agenda content from the file
f.close()  # Close the file

# Move the original agenda file to the backup folder for recovery
os.rename('Support Files/my agenda.txt', "backup/recover")

# Main loop for the To-Do List Manager
while True:
    print("To do list Manager")  # Display menu
    menu = input(
        "What do you want to do?:\n1. View complete list\n2. Add an item\n3. Edit an item\n4. Remove an item\n5. Delete complete list\n6. Exit\n>>> ")

    if menu == "1":  # View the agenda
        print("Your current agenda is: ")
        printList()
        time.sleep(3)  # Pause to let the user see the agenda

    elif menu == "2":  # Add a new item to the agenda
        item = input("What do you want to add?: ")
        if check_duplicates(item) == False:  # Add item if not a duplicate
            my_agenda.append(item)
            print("Item added")
        else:
            continue  # Skip adding if duplicate
        time.sleep(1)  # Pause for a second

    elif menu == "3":  # Edit an existing item in the agenda
        print("Current agenda is:")
        printList()  # Show the current agenda
        item = input("What do you want to edit?: ")

        if item in my_agenda:  # Proceed if item exists
            item35 = input("What do you want to replace it with?:")
            if check_duplicates(item35) == False:  # Replace if the new item is not a duplicate
                my_agenda.remove(item)
                my_agenda.append(item35)
                print("Item replaced")
                time.sleep(2)  # Pause for 2 seconds
            else:
                continue

        else:
            print("Item not in agenda")
            continue

    elif menu == "4":  # Remove an item from the agenda
        print("Current agenda is:")
        printList()  # Show current agenda
        item = input("What do you want to delete?: ")

        if item in my_agenda:  # If item exists, confirm removal
            confirmation = input("Are you sure you want to Delete it?:\n1.Yes\n2.No\n>>>")
            if confirmation == "1":
                my_agenda.remove(item)  # Remove the item
                print("Item removed")
                time.sleep(2)  # Pause for 2 seconds
            else:
                continue

    elif menu == "5":  # Delete the entire agenda
        my_agenda = my_agenda = []  # Clear the agenda

    elif menu == "6":  # Exit the program
        f = open("Support Files/my agenda.txt", "w")  # Save the current agenda to the file
        f.write(str(my_agenda))
        f.close()  # Close the file and exit the loop
        break

    else:
        print("Option not valid")  # Handle invalid menu choices
