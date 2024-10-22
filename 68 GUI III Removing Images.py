# This script creates a simple Tkinter window with a label and a button.
# Clicking the button hides or shows the label, alternating between states.

import tkinter as tk  # Import the Tkinter module

# Create the main window
window = tk.Tk()
window.title("Hello World")  # Set the window title
window.geometry("400x200")  # Set the window size

# Variable to track whether the label is currently visible
labelOn = True

# Function to hide or show the label when the button is clicked
def hideLabel():
    global labelOn  # Access the global variable to track the label's state
    if labelOn:
        hello.pack_forget()  # Hide the label
        labelOn = False  # Update the state to indicate the label is hidden
    else:
        button.pack_forget()  # Temporarily remove the button to avoid placement issues
        hello.pack()  # Show the label again
        button.pack()  # Repack the button after the label
        labelOn = True  # Update the state to indicate the label is visible

# Create the label widget
hello = tk.Label(text="Hello World!")
hello.pack()  # Display the label in the window

# Create the button widget to toggle label visibility
button = tk.Button(text="Click me!", command=hideLabel)
button.pack()  # Display the button in the window

# Start the Tkinter main event loop
tk.mainloop()
