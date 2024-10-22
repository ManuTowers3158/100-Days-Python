# Day 44 Challenge Requirements
# Objective:
#
# Build a simple bingo game using a previously generated bingo card.
# Bingo Card Generation:
#
# Randomly generate a bingo card as done in the previous lesson.
# Optionally, reuse the code from the last lesson to generate the card.
# User Interaction:
#
# Ask the user repeatedly within a loop what number comes up next.
# Check if the entered number exists on the bingo card.
# Marking Numbers:
#
# If the number exists on the bingo card, replace it with an "X" symbol.
# Winning Condition:
#
# If the entire bingo card is filled with "X"s, the user wins.
# Notify the user when they have won the game.
# Game Loop:
#
# Continue asking for numbers and updating the bingo card until the user wins.

import random  # Import the random module to generate random numbers

def prettyPrint(list2D):
    # Print a formatted 2D list
    print()
    for row in list2D:
        for item in row:
            print(f"{item:^10}", end=" | ")  # Center each item in a field of width 10
        print()  # New line after each row
    print()

print("Random Bingo Card generator")  # Print title for the Bingo card generator
randomnumbers = []  # Initialize an empty list for random numbers

# Generate 8 random numbers between 1 and 99
for x in range(8):
    generated_number = random.randint(1, 99)  # Generate a random number
    randomnumbers.append(generated_number)  # Add to the list of random numbers

randomnumbers_arranged = []  # List to hold the arranged random numbers

# Sorting mechanism to arrange numbers
prev = 99
for y in range(len(randomnumbers)):
    prev = 99
    for x in range(len(randomnumbers)):
        num = randomnumbers[x]
        if num < prev:
            min = num  # Update min if current number is smaller
        prev = num

    randomnumbers_arranged.append(min)  # Add the smallest number to the arranged list
    randomnumbers.remove(min)  # Remove the smallest number from the original list

randomnumbers_arranged.insert(4, "BINGO")  # Insert "BINGO" in the middle of the list
print(randomnumbers_arranged)  # Print the arranged random numbers

# Initialize a 3x3 Bingo card
bingo_card = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Fill the Bingo card with arranged random numbers
bingo_card[0][0] = randomnumbers_arranged[0]
bingo_card[0][1] = randomnumbers_arranged[1]
bingo_card[0][2] = randomnumbers_arranged[2]
bingo_card[1][0] = randomnumbers_arranged[3]
bingo_card[1][1] = randomnumbers_arranged[4]
bingo_card[1][2] = randomnumbers_arranged[5]
bingo_card[2][0] = randomnumbers_arranged[6]
bingo_card[2][1] = randomnumbers_arranged[7]
bingo_card[2][2] = randomnumbers_arranged[8]  # Fill the last cell

print("Bingo card")  # Print header for the Bingo card
prettyPrint(bingo_card)  # Print the Bingo card

# Game loop for user input
while True:
    cross = int(input("Tache un numero jefe\n>>> "))  # Prompt user for a number to cross out
    for row in range(3):
        for col in range(3):
            if bingo_card[row][col] == cross:  # Check if the number matches
                print("Bien mi compa")  # Confirm the match
                bingo_card[row][col] = "X"  # Replace the number with "X"

    prettyPrint(bingo_card)  # Print the updated Bingo card
    if bingo_card[2][2] == "X":  # Check if the last cell is crossed out
        print("Ya ganaste jefe maestro")  # Inform the user of victory
        break  # Exit the loop

