# Define a function 'printList' to display the items in the to-do list
def printList():
    print()  # Print a blank line for spacing
    # Loop through each item in 'my_agenda' and print it
    for item in my_agenda:
        print(item)
    print()  # Print another blank line for spacing


# Initialize an empty list 'my_agenda' to store to-do items
my_agenda = []

# Start an infinite loop to continuously manage the to-do list
while True:
    # Display the menu prompt and ask the user what they want to do
    print("To do list Manager")
    menu = input("Do you want to View, Add or Edit the To Do list: ")

    # If the user chooses to view the to-do list
    if menu == "View":
        print("Your current agenda is: ")
        printList()  # Call the 'printList' function to display the list

    # If the user chooses to add a new item to the to-do list
    elif menu == "Add":
        item = input("What do you want to add?: ")  # Ask what the user wants to add
        my_agenda.append(item)  # Add the item to the to-do list

    # If the user chooses to edit an existing item in the to-do list
    elif menu == "Edit":
        print("Current agenda is:")
        printList()  # Display the current to-do list

        # Ask the user which item they want to edit
        item = input("What do you want to edit?: ")

        # If the item exists in the to-do list
        if item in my_agenda:
            # Ask if the user wants to replace or delete the item
            edit = input("Do you want to Replace or Delete it?:")

            # If the user wants to replace the item
            if edit == "Replace":
                my_agenda.remove(item)  # Remove the old item
                item35 = input("What do you want to replace it with?:")  # Ask for the replacement
                my_agenda.append(item35)  # Add the new item to the list
            # If the user wants to delete the item
            else:
                my_agenda.remove(item)  # Remove the item from the list

