# Start an infinite loop that will keep running until explicitly stopped
while True:
    # Print a message indicating that the code is running
    print("This code is running")

    # Ask the user if they want to continue and store the input in 'go_again'
    go_again = input("Do you want to continue?")

    # If the user inputs "No", break the loop and stop running the code
    if go_again == "No":
        break  # Exit the loop

# This message is printed once the loop is broken (after the user says "No")
print("Oh man I was having a great time")
