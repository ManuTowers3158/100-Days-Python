import os
import time
import datetime
from tinydb import TinyDB, Query

# Define the path to the "Support Files" folder and the diary.json file
base_directory = "Support Files"
db_file = os.path.join(base_directory, 'diary.json')

# Ensure the "Support Files" folder exists
if not os.path.exists(base_directory):
    os.makedirs(base_directory)

# Function to check the entered password against a predefined one
def contrasena(password):
    array1 = []  # List to store characters of the entered password
    array2 = []  # List to store characters of the correct password
    password_def = ["manuguapo1234"]  # Predefined correct password

    # Convert entered password to list of characters
    for i in password:
        array1.append(i)
    print(array1)  # Debugging print to check entered password list

    # Convert predefined password to list of characters
    for i in password_def[0]:
        array2.append(i)
    print(array2)  # Debugging print to check predefined password list

    flag = True  # Initialize flag for password check
    # Compare characters of entered and predefined passwords
    for i in range(len(array2)):
        try:
            if array1[i] != array2[i]:  # If any character does not match
                flag = False
        except:  # In case the entered password is shorter than the correct password
            flag = False
    if flag == True:  # If all characters match, return True
        return True
    else:
        return False  # Return False if the password is incorrect


# Main loop for password entry and log menu
while True:
    password_user = input("Por favor introducir contraseña:\n>>> ").lower().strip().replace(" ", "")  # Get and sanitize user input
    print(password_user)

    if contrasena(password_user) == True:  # If the password is correct
        db = TinyDB(db_file)  # Initialize TinyDB for storing log entries in Support Files
        os.system("cls")  # Clear the screen

        # Inner loop for the log management menu
        while True:
            os.system("cls")
            print("************Bitacora del Capitán**********")
            print("                  M       M")
            print("                  MM     MM")
            print("                  M M   M M")
            print("                  M  M M  M")
            print("                  M   M   M")
            print("                  M       M")
            print("                  M       M")
            print()
            # Display options for the user
            menu = int(input("            1. Add an Entry \n            2. View previous Entries\n>>> "))

            if menu == 1:  # If the user chooses to add a new log entry
                os.system("cls")
                today = datetime.datetime.now()  # Get the current date and time
                print()
                while True:
                    entry = input("Que quiere escribir Capitan:\n>>> ")  # Get the log entry
                    print(f"{today}:{entry}")
                    # Insert a log entry with a timestamp into the TinyDB database
                    db.insert({'timestamp': f'{today}', 'entry': f'{entry}'})
                    print("Log saved")
                    time.sleep(2)  # Pause briefly
                    menu3 = int(input("Desea agregar otra entry?\n1. Yes\n2. No\n>>> "))  # Ask if the user wants to add another entry
                    if menu3 == 1:
                        os.system("cls")  # Clear the screen to add another entry
                    else:
                        break  # Exit the log entry addition loop

            if menu == 2:  # If the user chooses to view previous entries
                os.system("cls")
                print("Previous Entries:")
                records = db.all()  # Retrieve all entries from the database
                for record in records:  # Loop through each log entry
                    timestamp = record["timestamp"]
                    entry = record["entry"]
                    print(f"Stardate: {timestamp}, Entry: {entry}")  # Display the timestamp and entry
                    menu2 = int(input("Would you like to continue loading previous entries?\n1.Yes\n2.No\n>>> "))  # Ask if the user wants to load more entries
                    if menu2 == 1:
                        os.system("cls")
                        continue
                    else:
                        break  # Exit the view entries loop
    else:
        print("Contraseña incorrecta")  # If the password is incorrect, prompt again
