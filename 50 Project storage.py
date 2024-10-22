# ### Day 50 Challenge Requirements
#
# - **Objective:**
#   - Create a program that allows users to add ideas to a text file and retrieve a random idea from it.
#
# - **Functionality:**
#   - **Add Idea:**
#     - Prompt the user to type in an idea.
#     - Save the typed idea to a text file named `my.ideas` in append mode, ensuring each idea is on a new line.
#   - **Load Random Idea:**
#     - Load the list of ideas from the file.
#     - Randomly select and display one idea to the user.
#     - Pause the display for a few seconds before clearing the screen and returning to the menu.


import os
import time
import random

x = True
ideas = []  # Initialize a list to store ideas

while True:
    os.system("cls")  # Clear the console
    print("Ideas")
    menu = input("Would you like to: \n1.Add an Idea\n2.Load an Idea\nX. Exit\n>>> ")

    if menu == "1":
        os.system("cls")
        idea = input("What is your idea?\n>>> ")  # Get the user's idea
        f = open("Support Files/Ideas.txt", "a+")  # Open file in append mode
        f.write(f"{idea}\n")  # Save the idea to the file
        f.close()  # Close the file
        print(f"your {idea} has been saved")  # Confirm saving

    elif menu == "2":
        os.system("cls")
        f = open("Support Files/Ideas.txt", "r")  # Open file in read mode
        ideas = []  # Reset the ideas list
        while True:
            contents = f.readline().strip()  # Read each line
            if contents == "":
                break  # Exit if no more lines

            ideas.append(contents)  # Add the line to the ideas list

        # Randomly select an idea to display
        idea_number = random.randint(0, (len(ideas) - 1))
        print(idea_number)
        print(f"{ideas[idea_number]:^10}")  # Print the selected idea centered

        f.close()  # Close the file
        time.sleep(3)  # Pause before continuing

    else:
        print("Nos vemos jefe sigale echando ganas")  # Exit message
        break  # Exit the loop

