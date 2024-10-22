# Introduction to the 100 Days of Code quiz
print("100 Days of Code QUIZ")
print()

# Ask the user how many questions they can answer correctly
print("How many can you answer correctly?")

# First question: Ask the user what programming language they are using
ans1 = input("What language are we writing in?")

# Check if the user's answer is "python"
if ans1 == "python":
    print("Correct")
else:
    print("Nope🙈")  # If the answer is incorrect, print a "Nope" message

# Second question: Ask the user which lesson number this is, convert the input to an integer
ans2 = int(input("Which lesson number is this?"))

# Check if the lesson number is greater than 12
if(ans2 > 12):
    print("We're not quite that far yet")  # If the number is too high, print this message
# Check if the lesson number is exactly 12
elif(ans2 == 12):
    print("That's right!")  # If correct, print the success message
# If the lesson number is lower than 12
else:
    print("We've gone well past that!")  # If too low, print this message
