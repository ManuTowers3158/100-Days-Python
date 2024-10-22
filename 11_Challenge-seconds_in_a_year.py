# Set the number of minutes in an hour (60)
minutes = int(60)

# Calculate the number of seconds in an hour (60 minutes * 60 seconds)
hour = int(60 * minutes)

# Calculate the number of seconds in a day (24 hours * number of seconds in an hour)
day = int(24 * hour)

# Ask the user if the current year is a leap year
leap_year = input("Is this a leap year?: ")

# Check if the user input is 'Yes' (indicating a leap year)
if leap_year == "Yes":
    # If it is a leap year, calculate the total number of seconds in 366 days
    seconds_year = day * 366
else:
    # If it is not a leap year, calculate the total number of seconds in 365 days
    seconds_year = day * 365

# Print the total amount of seconds in the current year
print("The total amount of seconds in this year is:", seconds_year)
