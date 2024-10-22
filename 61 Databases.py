# This script simulates a simple Twitter-like interface where the user can add tweets and view them,
# using TinyDB to store tweets with timestamps in a JSON file.

import time
from tinydb import TinyDB, Query
import datetime
import os

# Define the path to the "Support Files" folder and the tweeter.json file
base_directory = "Support Files"
db_file = os.path.join(base_directory, 'tweeter.json')

# Ensure the "Support Files" folder exists
if not os.path.exists(base_directory):
    os.makedirs(base_directory)  # Create the directory if it doesn't exist

# Initialize the TinyDB database at the specified location
db = TinyDB(db_file)
User = Query()  # Create a TinyDB query object

today = datetime.datetime.now()  # Get the current date and time

# Main loop to manage the tweet interface
while True:
    os.system("cls")  # Clear the terminal screen ("cls" for Windows, "clear" for Unix)
    print("***************Twitter*************")

    # Display the menu and prompt user for input
    menu = int(input("1. Add a tweet\n2. View Tweets\n>>> "))

    if menu == 1:  # Option to add a new tweet
        os.system("cls")
        tweet = input("Cual es su Tweet mi compa\n>>>")  # Prompt user for tweet content
        print(f"{today}: {tweet}")  # Display the tweet with the current timestamp

        # Insert a tweet record with a timestamp into the TinyDB database
        db.insert({'timestamp': f'{today}', 'tweet': f'{tweet}'})

    elif menu == 2:  # Option to view stored tweets
        os.system("cls")
        records = db.all()  # Retrieve all tweet records from the database
        count = 0  # Initialize a counter to keep track of displayed tweets

        # Display the tweets in reverse order (most recent first)
        for record in reversed(records):
            timestamp = record["timestamp"]
            tweet = record["tweet"]
            print(f"date: {timestamp}, Tweet: {tweet}")  # Print each tweet with its timestamp
            count += 1

            # After displaying 10 tweets, prompt user to load older tweets
            if count >= 10:
                display = int(input("Would you like to continue loading older tweets?\n1.Yes\n2.No\n>>> "))
                if display == 1:  # If the user wants to continue, clear the screen and reset the counter
                    os.system("cls")
                    count = 0
                    continue
                else:
                    break  # Stop displaying tweets if the user chooses not to continue

        time.sleep(3)  # Wait 3 seconds before returning to the menu
