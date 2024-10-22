# This script creates a simple calculator using the Tkinter library.
# The calculator can perform basic arithmetic operations like addition, subtraction, multiplication, and division.

import tkinter as tk  # Import the Tkinter module

# Create the main window for the calculator
window = tk.Tk()
window.title("Calculator")  # Set the window title
window.geometry("300x400")  # Set the window size

# Initialize variables for storing the current answer and the last entered number
answer = 0
lastNumber = 0

# Function to handle number inputs
def InputBox(value):
    global answer
    answer = f"{answer}{value}"  # Append the new number to the current answer
    answer = int(answer)  # Convert the result back to an integer
    Result["text"] = answer  # Update the result display

# Function to store the last number and operator when an operation button is pressed
def calcAnswer(thisOp):
    global answer, lastNumber, operator
    if thisOp == "+":  # If the operator is addition
        lastNumber = answer  # Store the current answer
        answer = 0  # Reset the answer
        operator = "+"  # Set the operator
        Result["text"] = answer  # Update the display
    elif thisOp == "-":  # If the operator is subtraction
        lastNumber = answer
        answer = 0
        operator = "-"
        Result["text"] = answer
    elif thisOp == "*":  # If the operator is multiplication
        lastNumber = answer
        answer = 0
        operator = "*"
        Result["text"] = answer
    elif thisOp == "/":  # If the operator is division
        lastNumber = answer
        answer = 0
        operator = "/"
        Result["text"] = answer

# Function to calculate the final result based on the selected operator
def calculation():
    global answer, lastNumber, operator
    if operator == "+":  # Perform addition
        total = lastNumber + answer
        answer = total
        Result["text"] = answer  # Update the display
    elif operator == "-":  # Perform subtraction
        total = lastNumber - answer
        answer = total
        Result["text"] = answer
    elif operator == "*":  # Perform multiplication
        total = lastNumber * answer
        answer = total
        Result["text"] = answer
    elif operator == "/":  # Perform division
        total = lastNumber / answer
        answer = total
        Result["text"] = answer

#******Result Box**********
Result = tk.Label(text=answer)  # Create a label to display the result
Result.grid(row=0, column=2)  # Place the result display in the grid

#*****Number Buttons**********
one_bot = tk.Button(height=1, width=1, text="1", command=lambda: InputBox(1))
one_bot.grid(row=2, column=1)

two_bot = tk.Button(height=1, width=1, text="2", command=lambda: InputBox(2))
two_bot.grid(row=2, column=2)

three_bot = tk.Button(height=1, width=1, text="3", command=lambda: InputBox(3))
three_bot.grid(row=2, column=3)

four_bot = tk.Button(height=1, width=1, text="4", command=lambda: InputBox(4))
four_bot.grid(row=3, column=1)

five_bot = tk.Button(height=1, width=1, text="5", command=lambda: InputBox(5))
five_bot.grid(row=3, column=2)

six_bot = tk.Button(height=1, width=1, text="6", command=lambda: InputBox(6))
six_bot.grid(row=3, column=3)

seven_bot = tk.Button(height=1, width=1, text="7", command=lambda: InputBox(7))
seven_bot.grid(row=4, column=1)

eight_bot = tk.Button(height=1, width=1, text="8", command=lambda: InputBox(8))
eight_bot.grid(row=4, column=2)

nine_bot = tk.Button(height=1, width=1, text="9", command=lambda: InputBox(9))
nine_bot.grid(row=4, column=3)

zero_bot = tk.Button(height=1, width=1, text="0", command=lambda: InputBox(0))
zero_bot.grid(row=5, column=2)

#*****Operation Buttons**********
sum_bot = tk.Button(height=1, width=1, text="+", command=lambda: calcAnswer("+"))
sum_bot.grid(row=2, column=4)

res_bot = tk.Button(height=1, width=1, text="-", command=lambda: calcAnswer("-"))
res_bot.grid(row=3, column=4)

mult_bot = tk.Button(height=1, width=1, text="*", command=lambda: calcAnswer("*"))
mult_bot.grid(row=4, column=4)

div_bot = tk.Button(height=1, width=1, text="/", command=lambda: calcAnswer("/"))
div_bot.grid(row=5, column=4)

# Button to trigger the calculation of the final result
equals_bot = tk.Button(height=1, width=1, text="=", command=calculation)
equals_bot.grid(row=6, column=4)

# Start the Tkinter main event loop
tk.mainloop()
