# Initialize the attempt counter to 0
attempt = 0

# Set the target number that the player needs to guess
target_number = 3158

# Start an infinite loop to repeatedly ask the player for their guess
while True:
    # Increment the attempt counter by 1 for each guess
    attempt = attempt + 1

    # Ask the player to input their guess, and convert the input to an integer
    guessing_number = int(input("What is your number?: "))

    # If the guessed number is higher than the target number
    if guessing_number > target_number:
        print("Too high")  # Tell the player their guess is too high
        continue  # Restart the loop and ask for another guess

    # If the guessed number is lower than the target number
    elif guessing_number < target_number:
        print("Too Low")  # Tell the player their guess is too low
        continue  # Restart the loop and ask for another guess

    # If the guessed number matches the target number
    elif guessing_number == target_number:
        # Print a success message and tell the player how many attempts they made
        print("Yes, correct! That is the number, you guessed it in", attempt, "attempts")
        exit()  # Exit the program once the correct number is guessed


