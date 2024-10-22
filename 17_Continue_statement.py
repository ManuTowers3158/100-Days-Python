# Start an infinite loop that will keep running until the player either wins or dies
while True:
    # Ask the player to choose a direction (left or right)
    print("Do you want to go to the left or to the right")

    # Capture the player's choice and store it in 'direction'
    direction = input("<")

    # If the player chooses "Left", print the message that they fell into a trap and break the loop (ending the game)
    if direction == "Left":
        print("You fall into a trap, you are now dead")
        break  # Exit the loop

    # If the player chooses "Right", continue the loop (restart the loop, nothing happens)
    elif direction == "Right":
        continue  # Go back to the top of the loop, asking for the direction again

    # If the player inputs anything else, print a winning message and exit the program
    else:
        print("You are genius, you won")
        exit()  # Terminate the entire program

# After the loop ends, this message is printed (only if the player falls into the trap)
print("Thanks for playing")

