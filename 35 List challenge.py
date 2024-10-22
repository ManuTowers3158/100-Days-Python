import os  # Import the os module to use system commands (like clearing the terminal)
import time  # Import the time module to add delays

# Define a function to print the current list of items in 'my_agenda'
def printList():
    print()  # Print a blank line for spacing
    # Loop through each item in 'my_agenda' and print it
    for item in my_agenda:
        print(item)
    print()  # Print another blank line for spacing

# Define a function to check for duplicates in 'my_agenda'
def check_duplicates(item):
    # If the item is already in the agenda
    if item in my_agenda:
        print("Item already in agenda")  # Inform the user
        time.sleep(2)  # Pause for 2 seconds
        return True  # Return True indicating a duplicate
    else:
        return False  # Return False indicating no duplicate

# Initialize an empty list to store agenda items
my_agenda = []

# Start an infinite loop for the to-do list manager
while True:
    os.system("cls")  # Clear the terminal screen
    print("To do list Manager")  # Print the title
    # Display the menu options and get the user's choice
    menu = input("What do you want to do?:\n1. View complete list\n2. Add an item\n3. Edit an item\n4. Remove an item\n5. Delete complete list\n>>> ")

    # If the user chooses to view the complete list
    if menu == "1":
        print("Your current agenda is: ")
        printList()  # Call the printList function to display the list
        time.sleep(3)  # Pause for 3 seconds before continuing

    # If the user chooses to add an item
    elif menu == "2":
        item = input("What do you want to add?: ")  # Prompt for the item to add
        # Check for duplicates before adding
        if check_duplicates(item) == False:
            my_agenda.append(item)  # Add the item to the list
            print("Item added")  # Confirm the addition
        else:
            continue  # Skip to the next iteration if the item is a duplicate
        time.sleep(1)  # Pause for 1 second

    # If the user chooses to edit an item
    elif menu == "3":
        print("Current agenda is:")
        printList()  # Display the current list
        item = input("What do you want to edit?: ")  # Prompt for the item to edit
        # If the item is found in the agenda
        if item in my_agenda:
            item35 = input("What do you want to replace it with?:")  # Prompt for the replacement
            # Check for duplicates before replacing
            if check_duplicates(item35) == False:
                my_agenda.remove(item)  # Remove the old item
                my_agenda.append(item35)  # Add the new item
                print("Item replaced")  # Confirm the replacement
                time.sleep(2)  # Pause for 2 seconds
            else:
                continue  # Skip to the next iteration if the new item is a duplicate
        else:
            print("Item not in agenda")  # Inform the user if the item is not found
            continue  # Skip to the next iteration

    # If the user chooses to remove an item
    elif menu == "4":
        print("Current agenda is:")
        printList()  # Display the current list
        item = input("What do you want to delete?: ")  # Prompt for the item to delete
        # If the item is found in the agenda
        if item in my_agenda:
            confirmation = input("Are you sure you want to delete it?:\n1.Yes\n2.No\n>>>")  # Confirm deletion
            if confirmation == "1":
                my_agenda.remove(item)  # Remove the item
                print("Item removed")  # Confirm removal
                time.sleep(2)  # Pause for 2 seconds
            else:
                continue  # Skip to the next iteration if the user chose not to delete

    # If the user chooses to delete the complete list
    elif menu == "5":
        my_agenda = my_agenda[:]  # Clear the agenda (reset the list)

    # If the user inputs an invalid option
    else:
        print("Option not valid")  # Inform the user of the invalid option

    # Ask if the user wants to continue (this part is missing in your code but is suggested for a complete loop)
    print("Would you like to continue?")
