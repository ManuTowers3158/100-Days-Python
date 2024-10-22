import time  # Import time for adding delays

def printList():
    # Function to print the current contact list with numbering
    counter = 1
    for name in Contact_List:
        print(f"{counter}: {name}")
        counter += 1

def check_duplicates(name):
    # Check if the name already exists in the contact list
    if name in Contact_List:
        print("Name already in agenda")  # Inform the user about the duplicate
        time.sleep(2)  # Pause for 2 seconds
        return True
    else:
        return False

Contact_List = []  # Initialize the empty contact list

while True:
    print("***Contact List***")  # Display the header
    First_Name = input("First Name: ").capitalize().strip()  # Get and format first name
    Last_Name = input("Last Name: ").capitalize().strip()  # Get and format last name
    Full_Name = First_Name + " " + Last_Name  # Combine names

    # Check for duplicates before adding
    if check_duplicates(Full_Name) == False:
        Contact_List.append(Full_Name)  # Add the full name to the list
        print("Name added")  # Confirm addition
    printList()  # Display current contacts
