# Define a function 'newPrint' that takes two arguments: 'color' and 'word'
def newPrint(color, word):
    # If the color is red, print the word in red
    if color == "red":
        print("\033[31m", word, sep="", end="")  # \033[31m sets the color to red

    # If the color is green, print the word in green
    elif color == "green":
        print("\033[32m", word, sep="", end="")  # \033[32m sets the color to green

    # If the color is blue, print the word in blue
    elif color == "blue":
        print("\033[34m", word, sep="", end="")  # \033[34m sets the color to blue

    # If the color is not red, green, or blue, reset to default color
    else:
        print("\033[0m", word, sep="", end="")  # \033[0m resets to the default color


# Print a title for the subroutine
print("Super Subroutine")

# Print a message without changing the line (using 'end=""' to avoid a new line)
print("With my ", end="")

# Call the 'newPrint' function to print "new program" in red
newPrint("red", "new program")

# Call the 'newPrint' function to reset the color and print the rest of the sentence
newPrint("reset", " I can just call the color")
