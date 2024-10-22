 ### Day 48 Challenge Requirements
#
# - **Objective:**
#   - Create a program to manage a high score table for a video game.
#
# - **User Input:**
#   - Prompt the user to enter their three-letter initials.
#   - Prompt the user to enter their score, which should be a number out of about 100,000.
#
# - **Data Storage:**
#   - Save both the initials and the score into a text file named `hi.score`.
#   - Use append mode to add new entries to the file.
#   - If the file doesn’t exist, the program should create it.

f = open("Support Files/highscore.txt", "a+")  # Open the highscore file in append mode

x = True  # Control variable for the loop
while x:
    name = input("Enter three letter initials\n>>> ")  # Get user initials
    score = input("Enter score\n>>> ")  # Get user score
    f.write(f"{name}  {score}\n")  # Write the initials and score to the file

    cl = int(input("Do you want to enter another score?\n1. Yes\n2. No\n>>> "))  # Prompt for continuation
    if cl == 2:
        x = False  # Exit the loop if the user chooses not to continue

f.close()  # Close the file
