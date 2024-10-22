# Greet the user and introduce the daily affirmation generator
print("Hello. Welcome to your daily affirmation generator.")

# Ask for the user's name and store it in the variable 'name'
name = input("What is your name? ")

# Check if the name is 'Manuel' (case-insensitive)
if name == "Manuel" or name == "manuel":
    # Ask for the day of the week (DOW)
    DOW = input("What is the day of the week? ")

    # Provide affirmations based on the day of the week
    if DOW == "monday" or DOW == "Monday":
        print("It is going to be a great Monday", name)
    if DOW == "tuesday" or DOW == "Tuesday":
        print("What a wonderful Tuesday it is", name)
    if DOW == "wednesday" or DOW == "Wednesday":
        print("Happy Hump Day", name)
    if DOW == "thursday" or DOW == "Thursday":
        print(name, "your week is almost over!")
    if DOW == "friday" or DOW == "Friday":
        print(name, "It's FRIDAY!")

# Check if the name is 'David' (case-insensitive)
elif name == "David" or name == "david":
    # Ask for the day of the week (DOW)
    DOW = input("What is the day of the week? ")

    # Provide affirmations based on the day of the week
    if DOW == "monday" or DOW == "Monday":
        print("It is going to be a great Monday", name)
    if DOW == "tuesday" or DOW == "Tuesday":
        print("You look great in that color", name)
    if DOW == "wednesday" or DOW == "Wednesday":
        print("You look chipper today", name)
    if DOW == "thursday" or DOW == "Thursday":
        print(name, "you are doing a great job!")
    if DOW == "friday" or DOW == "Friday":
        print(name, "it's FRIDAY!")

# If the user's name is not 'Manuel' or 'David', provide a generic message
else:
    print("I do not know your name, but I hope you are having a great day!")
