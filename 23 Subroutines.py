# Define a function 'rolldice' that takes one argument 'i'
def rolldice(i):  # When Parentheses has a blank in the function means it does not need any argument
    import random  # Import the random module to generate random numbers inside the function

    # Generate a random integer between 1 and 6 (simulating a dice roll)
    number = random.randint(1, 6)

    # Print the value of 'i' along with the dice number
    print("In Dice",i, "we´ve got:", number)


# Loop through the numbers 1 to 9 (inclusive) and call 'rolldice' with each value of 'i'
for i in range(1, 10):
    rolldice(i)  # Call the 'rolldice' function with 'i' as the argument
