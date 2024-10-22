# This script defines two recursive functions: 
# 1. `reverse`: Prints decreasing sequences of "#" symbols.
# 2. `factorial`: Calculates the sum of integers from 0 to the given value using recursion (not a true factorial).

# Function to print a reverse pattern of "#" symbols
def reverse(value):
    if value <= 0:  # Base case: when value is 0 or less, stop recursion
        print("Done!")
        return
    else:
        for i in range(value):  # Print "#" symbols equal to the value
            print("#", end="")  # No newline after each symbol
        print()  # Print a newline after the row of "#"
        reverse(value - 1)  # Recursive call with the value decreased by 1

# Function to calculate a summation (not factorial) using recursion
def factorial(value):
    if value <= 0:  # Base case: when value is 0 or less, stop recursion
        print("Done!")
        return
    else:
        factorial_value = 0  # Initialize the summation variable
        for i in range(value + 1):  # Loop from 0 to the current value
            current_value = i  # Store the current value of the loop
            factorial_value = factorial_value + current_value  # Add the current value to the summation
        factorial(value - 1)  # Recursive call to continue with value - 1
    return factorial_value  # Return the final summation result

# Uncomment the line below to test the reverse function
# reverse(10)

# Call the factorial function with the value 50 and print the result
print(factorial(50))
