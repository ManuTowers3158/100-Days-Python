import random  # Import the random module for random selections
import os  # Import the os module for system commands

charactersdict = {}  # Initialize an empty dictionary to store character data

def prettyPrint2():
    # Print detailed information for each character
    for key, value in charactersdict.items():
        print(key, end=":\n")  # Print character name
        for subkey, subvalue in value.items():
            print(f"  {subkey}: {subvalue}")  # Print each attribute
    print()

def prettyPrint3():
    # Print the names of all characters
    print("Characters")
    for key in charactersdict.keys():
        print(key)  # Print character names
    print()

x = True  # Control variable for the loop
while x:
    os.system("cls")  # Clear the console
    # Gather character attributes from user input
    Character = input("Name: ")
    Speed = input("Speed: ")
    Intellect = input("Intelligence: ")
    Magic = input("Magic: ")
    Strenght = input("Strenght: ")

    # Store character attributes in the dictionary
    charactersdict[Character] = {
        "Speed": Speed,
        "Intellect": Intellect,
        "Magic": Magic,
        "Strenght": Strenght
    }
    prettyPrint2()  # Print character details

    # Check if the user wants to continue
    x = input("Quieres continuar?\n 1:y 2:n\n>>>") == "1"

prettyPrint3()  # Print the list of characters
Pickup = input("Choose your character\n>>>")  # User selects their character

# Randomly select an enemy character
Enemypickup = random.randint(0, len(charactersdict) - 1)
enemy_name = list(charactersdict.keys())[Enemypickup]  # Get the enemy character name
Pickup2 = enemy_name  # Assign enemy character

print("Enemy:", enemy_name)  # Display the enemy character

category = input("Choose a category:\n1:Speed \n2:Intellect\n3:Magic\n4:Strenght\n>>>")
if category == "1":
    os.system("cls")
    # Speed contest logic
    print("Speed Contest")
    print(Pickup, "Speed:", charactersdict[Pickup]["Speed"])
    print(Pickup2, "Speed:", charactersdict[Pickup2]["Speed"])
    speed1 = int(charactersdict[Pickup]["Speed"])
    speed2 = int(charactersdict[Pickup2]["Speed"])
    # Determine the winner based on speed
    if speed1 > speed2:
        print(Pickup, "Wins")
    elif speed1 < speed2:
        print(Pickup2, "Wins")
    else:
        print("Tie")

elif category == "2":
    print("Intellect Contest")
elif category == "3":
    print("Magic Contest")
elif category == "4":
    print("Strenght Contest")
