# Print a message asking the user for their first name
print("What is your name?")

# Capture the user's input for their name and store it in the variable 'my_name'
my_name = input("Name: ")

# Check if the input name is 'Manuel'
if my_name == "Manuel":
    # If the name is 'Manuel', print a welcome message for the chief
    print("Welcome chief")

# Check if the input name is 'Henry'
elif my_name == "Henry":
    # If the name is 'Henry', print a welcome message with a nickname
    print("Welcome Henmbry")

# If the name is neither 'Manuel' nor 'Henry', this block will execute
else:
    # Print a message telling the user to get off Manuel's laptop
    print("get out of Manuel´s Laptop")
