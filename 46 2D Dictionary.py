pokedex = {}  # Initialize an empty dictionary to store Pokémon data

def prettyPrint2():
    # Print the Pokémon data in a formatted manner
    for key, value in pokedex.items():  # Loop through each Pokémon
        print(key, end=":\n")  # Print Pokémon name
        for subkey, subvalue in value.items():  # Loop through each attribute
            print(f"  {subkey}: {subvalue}")  # Print attribute and value

while True:
    # Prompt for Pokémon details
    Pokemon = input("Pokemon: ")  # Get Pokémon name
    Region = input("Region: ")  # Get region
    Type = input("Type: ")  # Get type
    Move = input("Move: ")  # Get move
    pokedex[Pokemon] = {"Region": Region, "Type": Type, "Move": Move}  # Store data
    prettyPrint2()  # Print current pokedex
