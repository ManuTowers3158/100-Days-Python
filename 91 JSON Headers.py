import requests, json
import os
import time

# Path to save the JSON file containing the jokes
file_path = "Support Files/91 Jokes.json"

while True:
    os.system("cls")  # Clear the console screen (use "clear" for Linux/Mac)

    # Display menu options for the user
    menu = input("Would you like to read a new joke or view previous jokes?\n1. New Joke\n2. See previous Jokes\n>>> ")

    if menu == "1":
        os.system("cls")  # Clear the screen before showing a new joke

        # Fetch a new joke from the API (icanhazdadjoke.com)
        result = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        joke = result.json()  # Get the joke as a JSON object

        # Print the fetched joke
        print(joke["joke"])

        # Ask if the user wants to save the joke
        collect = input("Would you like to save the joke?\n1.Yes\n2.No\n>>> ")

        if collect == "1":

            # Initialize a list to hold jokes (either from file or as a new list)
            if os.path.exists(file_path):
                # If the file exists, read the existing jokes from the file
                with open(file_path, "r") as f:
                    try:
                        existing_jokes = json.load(f)  # Load existing jokes from JSON
                        if not isinstance(existing_jokes, list):
                            raise ValueError("The JSON file does not contain a list.")
                    except (json.JSONDecodeError, ValueError) as e:
                        # Handle case where file is empty or not in proper format
                        existing_jokes = []
            else:
                # If the file does not exist, start with an empty list
                existing_jokes = []

            # Append the new joke to the list
            existing_jokes.append(joke)
            print("Joke saved")

            # Write the updated list of jokes back to the file in JSON format
            with open(file_path, "w") as f:
                json.dump(existing_jokes, f, indent=4)

        else:
            print("OK Joke not saved")  # If user chose not to save the joke

    elif menu == "2":
        # Load and display previously saved jokes
        while True:
            # Load the JSON data from the file
            with open(file_path, "r") as f:
                jokes_list = json.load(f)

            # Print each joke, enumerating them for easier reference
            for index, joke_entry in enumerate(jokes_list, start=1):
                print(f"{index}. {joke_entry['joke']}")

            print()
            # Ask if the user wants to return to the main screen
            menu2 = input("Would you like to return to the main screen?\n1. Yes\n2. No\n>>> ")
            if menu2 == "1":
                break  # Break the loop and return to the main menu




