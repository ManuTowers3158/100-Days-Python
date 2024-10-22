# This script creates a simple Tkinter window that displays an image.
# Upon clicking a button, the displayed image changes to a new one.

from PIL import Image, ImageTk  # Import the necessary modules for handling images
import tkinter as tk  # Import the Tkinter module

# Create the main window
window = tk.Tk()
window.title("Images API")  # Set the window title
window.geometry("300x400")  # Set the window size

# Function to change the displayed image when the button is clicked
def changeImage():
    canvas.itemconfig(container, image=newImage)  # Update the canvas with the new image

# Create a label widget
hello = tk.Label(text="Hello world")
hello.pack()  # Display the label in the window

# Create a button that triggers the image change when clicked
button = tk.Button(text="Click me!", command=changeImage)
button.pack()  # Display the button in the window

# Create a canvas widget to hold the image
canvas = tk.Canvas(window, width=300, height=150)
canvas.pack()

# Load the first image and scale it down (using subsample)
image = tk.PhotoImage(file="./Support Files/pikachu.png")  # Load the initial image
image = image.subsample(5)  # Scale down the image by a factor of 5

# Load the second image that will replace the first one
newImage = tk.PhotoImage(file="./Support Files/Ferrari.png")  # Load the new image
newImage = newImage.subsample(5)  # Scale down the new image by a factor of 5

# Display the initial image in the canvas
container = canvas.create_image(150, 80, image=image)

# Start the Tkinter main event loop
tk.mainloop()
