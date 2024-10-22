# This script simulates a secure captain's log system where the user can create entries and view past entries.
# It uses TinyDB to store usernames and hashed passwords with salts for security, and allows users to add or view diary entries.

import hashlib  # Import hashlib for password hashing
import time  # Import time for delays
from tinydb import TinyDB, Query  # Import TinyDB for database handling
import datetime  # Import datetime for timestamping entries
import os  # Import os for system operations (e.g., clearing screen)
import random  # Import random for generating salts

# Initialize TinyDB to store user credentials in 'Secret_Diary.json'
db = TinyDB('./Support Files/Secret_Diary.json')
User = Query()
#User Manu
#password:Mamnu

# Check if the database is empty (i.e., no users have been created)
if len(db) == 0:
    print("Welcome to Star Fleet")
    user = input("Enter New User Name: ")  # Prompt for a new username
    password = input("New Password: ")  # Prompt for a new password
    salt = random.randint(0, 1000)  # Generate a random salt for password security
    print(f"User: {user}, Password: {password}, Salt: {salt}")

    # Combine the password and salt, then hash it using SHA-256
    newPassword = f"{password}{salt}"
    newPassword = hashlib.sha256(newPassword.encode()).hexdigest()
    print(newPassword)

    # Insert the new user record into the database
    db.insert({'name': user, 'password': newPassword, 'salt': salt})
else:
    # If users already exist, prompt for login
    while True:
        user = input("Enter username: ")  # Prompt for username
        result = db.search(User.name == user)  # Search for the user in the database
        ans = input("Enter Password: ")  # Prompt for password

        # Retrieve the user's salt and hashed password
        salt = result[0]['salt']
        password_original = result[0]["password"]

        # Combine the entered password with the salt and hash it
        newPassword = f"{ans}{salt}"
        newPassword = hashlib.sha256(newPassword.encode()).hexdigest()

        # Compare the entered password's hash with the stored hash
        if newPassword == password_original:
            # Successful login, start the captain's log
            while True:
                os.system("cls")  # Clear the screen
                print("************Bitacora del Capitán**********")
                print("                  M       M")
                print("                  MM     MM")
                print("                  M M   M M")
                print("                  M  M M  M")
                print("                  M   M   M")
                print("                  M       M")
                print("                  M       M")
                print()
                print("Welcome aboard Captain Torres, starting captain's log")

                # Menu for adding/viewing log entries
                menu = int(input("            1. Add an Entry \n            2. View previous Entries\n>>> "))
                db = TinyDB('diary.json')  # Use 'diary.json' to store captain's log entries

                if menu == 1:
                    # Adding a new entry
                    os.system("cls")
                    today = datetime.datetime.now()  # Get the current date and time
                    while True:
                        entry = input("Que quiere escribir Capitan:\n>>> ")  # Prompt for a new log entry
                        print(f"{today}: {entry}")

                        # Insert the log entry into the database
                        db.insert({'timestamp': f'{today}', 'entry': f'{entry}'})
                        print("Log saved")
                        time.sleep(2)

                        # Ask if the user wants to add another entry
                        menu3 = int(input("Desea agregar otra entry?\n1. Yes\n2. No\n>>> "))
                        if menu3 == 1:
                            os.system("cls")
                        else:
                            break

                if menu == 2:
                    # Viewing previous entries
                    os.system("cls")
                    print("Previous Entries:")
                    records = db.all()  # Retrieve all entries from the database

                    for record in records:
                        timestamp = record["timestamp"]
                        entry = record["entry"]
                        print(f"Stardate: {timestamp}, Entry: {entry}")

                        # Ask if the user wants to continue viewing more entries
                        menu2 = int(input("Would you like to continue loading previous entries?\n1.Yes\n2.No\n>>> "))
                        if menu2 == 1:
                            os.system("cls")
                            continue
                        else:
                            break
        else:
            # Incorrect password entered
            print("Contraseña incorrecta")
