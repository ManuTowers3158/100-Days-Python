# This script is a number guessing game where the user tries to guess a randomly generated number between 1 and 100.
# It tracks the number of attempts per round and provides a total score over multiple games.

import random, os, time  # Import required modules

totalAttempts = 0  # Initialize total attempts across all rounds


# Function to handle the main guessing game
def game():
    attempts = 0  # Initialize attempts for this round
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    while True:
        guess = int(input("Pick a number between 1 and 100: "))  # User inputs their guess

        # Provide feedback if the guess is too high, too low, or just right
        if guess > number:
            print("Too high")
            attempts += 1  # Increment the attempts for this round
        elif guess < number:
            print("Too low")
            attempts += 1
        else:
            print("Just right!")  # User guessed correctly
            print(f"{attempts} attempts this round")  # Display number of attempts for this round
            return attempts  # Return the attempts count to update the total score


# Main game loop
while True:
    # Display menu options for the user
    menu = int(input("1: Guess the random number game \n2: Total Score\n3: Exit\n>"))

    if menu == 1:  # If the user chooses to play the game
        totalAttempts += game()  # Call the game function and add attempts to total score
    elif menu == 2:  # If the user chooses to see the total score
        print(f"You've had {totalAttempts} attempts")  # Display total attempts
    else:
        break  # Exit the game
