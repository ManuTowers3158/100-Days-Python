def prettyPrint(listofshame):
    # Print each record in a formatted manner
    for row in listofshame:
        for item in row:
            print(f"{item:^10}", end=" | ")  # Center each item in a field of width 10
        print()  # New line after each row

listofshame = []  # Initialize an empty list to store records

while True:
    menu = input("Would you like to add or remove a record? a/r ")  # Prompt for action
    if(menu.strip().lower()[0] == "a"):  # Check if the user wants to add a record
        name = input("What is your name? ")
        age = input("What is your age? ")
        pref = input("What is your Computer platform? ")
        row = [name, age, pref]  # Create a record
        listofshame.append(row)  # Add the record to the list (important line)
    else:  # If the user wants to remove a record
        name = input("What is the name of the record to delete?\n>>> ")

        # Loop through the list to find and remove the record
        for row in listofshame:
            if name in row:  # Check if the name matches
                listofshame.remove(row)  # Remove the matching row

    exit = input("Exit? y/n: ")  # Prompt to exit
    if(exit.strip().lower()[0] == "y"):  # Check if the user wants to exit
        break  # Exit the loop

    prettyPrint(listofshame)  # Print the current list of records
