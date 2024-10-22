
# Initialize variables
days_python = 10  # Set the number of days to 10 for this example (replace with 30 for 30 days of challenges)
day = 0  # Initialize day variable


# Define a function 'newPrint' that prints text in specified colors (red, green, blue, or reset to default)
def newPrint(color, word):
    if color == "red":
        print("\033[31m", word, sep="", end="")  # Print in red
    elif color == "green":
        print("\033[32m", word, sep="", end="")  # Print in green
    elif color == "blue":
        print("\033[34m", word, sep="", end="")  # Print in blue
    else:
        print("\033[0m", word, sep="", end="")  # Reset to default color


# Loop through each day, asking the user for their opinion of each day
for day in range(1, days_python):
    # Ask the user for their opinion on the current day
    opinion = input("What is your opinion of day {}? ".format(day))

    # Format a response string based on the user's input
    response = f"So, you thought day {day} was, {opinion}"

    # Print the response, centered to 50 characters, in red using 'newPrint'
    newPrint("red", f"{response:^50}")

    # Reset the text color back to default and print a newline
    newPrint("reset", "\n")


