# Ask the user to provide a number for the multiplication table quiz and store it in 'number_for_table'
number_for_table = int(input("Provide a number for your multiplication table quiz: "))

# Initialize a points counter to 0
points = 0

# Start a loop that iterates from 1 to 10 (for the multiplication table)
for i in range(1, 11):
    # Display the current multiplication question
    print("What is", number_for_table, "x", i)

    # Calculate the correct answer for the current multiplication
    correct_answer = number_for_table * i

    # Get the user's answer and convert it to an integer
    answer = int(input("Answer: "))

    # Check if the user's answer is correct
    if answer == correct_answer:
        print("That is right boss ")
        # Increment the points by 1 if the answer is correct
        points = points + 1
    else:
        # If the answer is wrong, print the correct answer
        print("Nope, the correct answer is:", correct_answer)
        continue  # Move to the next iteration (next multiplication question)

# After the loop, print the total number of points obtained
print("You obtained", points, "points")

# If the user got all 10 points, print a special congratulatory message
if points == 10:
    print("Nice, you are the Master Chief")
