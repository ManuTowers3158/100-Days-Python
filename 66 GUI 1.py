# This script creates a basic Tkinter window with a label, a text input box, and three buttons.
# The label gets updated with the value entered in the text box upon button click.

import tkinter as tk  # Import the Tkinter module

# Create the main window for the application
window = tk.Tk()
window.title("Hello world")  # Set the window title
window.geometry("300x300")  # Set the window size

label = 0  # Initialize the label value to 0

# Function to update the label with the value entered in the text box
def updateLabel():
    global label  # Use the global label variable
    number = text.get("1.0", "end")  # Get the value from the text box (from line 1, character 0)
    number = int(number)  # Convert the value to an integer
    label += number  # Add the entered number to the label value
    hello["text"] = label  # Update the label text with the new value

# Create the label widget and place it in the grid
hello = tk.Label(text=label)
hello.grid(row=0, column=1)

# Create a text box for input and place it in the grid
text = tk.Text(window, height=1, width=25)
text.grid(row=1, column=1)

# Create three buttons, each using the updateLabel function when clicked
button = tk.Button(text="Click me!", command=updateLabel).grid(row=2, column=0)
button = tk.Button(text="Button 2", command=updateLabel).grid(row=2, column=1)
button = tk.Button(text="Button 3!", command=updateLabel).grid(row=2, column=2)

# Start the Tkinter main event loop
tk.mainloop()
