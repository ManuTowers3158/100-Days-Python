# User Input:
#
# Ask the user to type in any sentence.
# Colored Ratchet Mechanism:
#
# Implement a system where:
# When the user types in an 'R', every letter from that point forward should be red.
# When the user types in a 'B', every letter from that point forward should be blue.
# The color effect should not be turned off until another trigger is detected.
# Space Detection (Extra Points):
#
# Turn off the color and revert to normal text every time a space is detected.
# Only the words containing the specified letters ('R' or 'B') should be colorized.
# Output:
#
# Produce a sentence that visually appears as a multi-colored string based on the rules above.
# Purpose:
#
# Practice detecting and handling individual letters within a string using a loop.
# print("Pikachu is a","\33[33myellow","\33[0mPokemon.")
# print("Charizard is a","\33[31mred","\33[0mPokemon.")
# print("Bulbasur is a","\33[32mgreen","\33[0mPokemon.")
# print("Squirtle is a","\33[34mblue","\33[0mPokemon.")

#target= ["y","b","g","r"]
myString = input("Type something >>> ")  # Get user input

# Loop through each letter in the input string
for letter in myString:
    if letter == " ":
        print('\033[0m', end='')  # Reset to default color for spaces
    if letter == "y":
        print('\033[33m', end='')  # Change color to yellow
        print(letter, end='')  # Print letter without space
    if letter == "b":
        print('\033[34m', end='')  # Change color to blue
        print(letter, end='')  # Print letter without space
    if letter == "g":
        print('\033[32m', end='')  # Change color to green
        print(letter, end='')  # Print letter without space
    if letter == "r":
        print('\033[31m', end='')  # Change color to red
        print(letter, end='')  # Print letter without space
    else:
        print(letter, end='')  # Print all other letters in default color

