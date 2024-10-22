# Day 43 Challenge Requirements
# Objective:
#
# Create a bingo card that will make my nan very happy.
# Bingo Card Structure:
#
# The bingo card should be a two-dimensional list.
# Randomly generate a series of numbers between 0 and 90.
# Allocate these numbers to each place within the 2D list.
# Ensure the numbers are in numerical order.
# The center square should contain the word "Bingo" instead of a number.
# Random Number Generation:
#
# Use random number generation to fill the bingo card.
# Display:
#
# Each time the program runs, present the bingo card with different random numbers.
# Output:
#
# The bingo card should be displayed on the screen with the generated numbers and the center square marked as "Bingo".
# Notes:
# This challenge involves generating and organizing random numbers in a structured format.
# The project should be able to run multiple times, each time displaying a newly generated bingo card.

import random  # Import the random module for generating random numbers

print("Random Bingo Card generator")  # Print the title of the program

# Example random numbers (can be generated dynamically)
randomnumbers = [52, 78, 49, 85, 44, 25, 34, 60]  # List of random numbers

randomnumbers_arranged = []  # List to hold the sorted numbers

# Loop to sort the random numbers in ascending order
for y in range(len(randomnumbers)):
    prev = 99  # Initialize previous number to a high value
    for x in range(len(randomnumbers)):
        num = randomnumbers[x]  # Get the current number
        if num < prev:  # If current number is less than the previous
            min = num  # Update the minimum number found
        else:
            continue  # Skip to the next iteration
        prev = num  # Update previous number

    # Append the smallest number to the arranged list and remove it from the original list
    randomnumbers_arranged.append(min)
    randomnumbers.remove(min)

# Insert the word "BINGO" into the arranged list
randomnumbers_arranged.insert(4, "BINGO")  # Insert "BINGO" at index 4
print(randomnumbers_arranged)  # Print the arranged list with "BINGO"

# Initialize a 3x3 Bingo card
bingo_card = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Assign numbers from the arranged list to the Bingo card
bingo_card[0][0] = randomnumbers_arranged[0]
bingo_card[0][1] = randomnumbers_arranged[1]
bingo_card[0][2] = randomnumbers_arranged[2]
bingo_card[1][0] = randomnumbers_arranged[3]
bingo_card[1][1] = randomnumbers_arranged[4]
bingo_card[1][2] = randomnumbers_arranged[5]
bingo_card[2][0] = randomnumbers_arranged[6]
bingo_card[2][1] = randomnumbers_arranged[7]
bingo_card[2][2] = randomnumbers_arranged[8]  # Fixed index from [2][1] to [2][2]

# Print the Bingo card
print("Bingo card")
for x in range(3):
    print(bingo_card[x])  # Print each row of the Bingo card

# print(randomnumbers_arranged)