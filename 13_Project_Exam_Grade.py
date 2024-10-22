import random
# Print the introduction to the exam grade calculator
print("Exam grade calculator \n")
print("Name of the exam: Computer Science")
print("Max. Possible Score: 100")

# Ask the user to input their score, convert it to a float, and store it in the variable 'score'
score = float(input("Your score is:"))

# Determine the grade based on the score
if score >= 90:
    note = "A+"  # If the score is 90 or above, the grade is A+
elif score >= 80:
    note = "A-"  # If the score is between 80 and 89, the grade is A-
elif score >= 70:
    note = "B"  # If the score is between 70 and 79, the grade is B
elif score >= 60:
    note = "C"  # If the score is between 60 and 69, the grade is C
elif score >= 50:
    note = "D"  # If the score is between 50 and 59, the grade is D
else:
    note = "F"  # If the score is below 50, the grade is F (Fail)

# Print the user's score and their corresponding grade
print("Your score is", score, "Which means you got a:", note)
