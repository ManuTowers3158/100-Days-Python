# Ask the user for their score, convert it to an integer, and store it in the variable 'myScore'
myScore = int(input("Your score: "))

# Check if the score is greater than 100,000
if myScore > 100000:
    # If the score is greater than 100,000, print "Winner!"
    print("Winner!")
else:
    # If the score is 100,000 or below, print "Try again" with a crying emoji
    print("Try again 😭")


