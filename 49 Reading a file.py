# ### Day 49 Challenge Requirements
#
# - **Objective:**
#   - Develop a program to read from a high score file and identify the highest scorer automatically.
#
# - **File Reading:**
#   - Read data from the `High.score` file created in the previous day’s challenge.
#
# - **Data Processing:**
#   - Split each read line to extract two elements: the user's initials and their score.
#   - Convert the score from a string to an integer for comparison.
#
def prettyPrint(list2D):
    # Print a formatted 2D list
    for row in list2D:
        for item in row:
            print(f"{item:^10}", end=" | ")  # Center each item
            break  # Exit after the first item
        print()  # New line after each row

list_scores = []  # Initialize a list to hold scores

f = open("Support Files/highscore.txt", "r")  # Open the highscore file in read mode
while True:
    contents = f.readline().strip()  # Read a line and strip whitespace
    if contents == "":
        break  # Exit if no more lines to read
    contents = contents.split("  ")  # Split the line into components
    list_scores.append(contents)  # Append to the list

# Convert scores to integers
for x in range(len(list_scores)):
    list_scores[x][1] = int(list_scores[x][1])

# Sort the list by score in descending order
list_scores.sort(key=lambda x: x[1], reverse=True)

print("Highest Score:")
# Print the highest score
for item in list_scores[0]:  # Access the first item in the sorted list
    print(f"{item:^10}", end=" | ")  # Print each item centered

f.close()  # Close the file
