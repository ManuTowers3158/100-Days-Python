# Initialize a dictionary to store Pokémon attributes
pokemon = {"Name": None, "Type": None, "Special Move": None, "Hability": None, "HP": None}

# Loop through the keys in the dictionary to collect user input for Pokémon attributes
for x in pokemon:
    print("Enter", x)  # Prompt the user for each attribute
    value = input(">>> ")  # Get user input
    pokemon[x] = value  # Store the input in the dictionary

# Loop through the dictionary to print the Pokémon details
for item, value in pokemon.items():
    # Set text color based on Pokémon type
    if pokemon["Type"] == "Electric":
        print('\033[33m', end='')  # Set color to yellow for Electric type

    elif pokemon["Type"] == "Water":
        print('\033[34m', end='')  # Set color to blue for Water type

    elif pokemon["Type"] == "Grass":
        print('\033[32m', end='')  # Set color to green for Grass type

    elif pokemon["Type"] == "Fire":
        print('\033[31m', end='')  # Set color to red for Fire type
    else:
        print('\033[0m', end='')  # Reset to default color for other types

    print(f"{item}: {value}")  # Print each key-value pair from the Pokémon dictionary
