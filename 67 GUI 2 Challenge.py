# This script creates a Tkinter GUI application where the user can input a character name.
# Based on the input, the application looks for images in a corresponding folder and displays them sequentially.

from PIL import Image, ImageTk  # Import the necessary modules for image handling
import tkinter as tk
import os
from pathlib import Path  # Import Path from pathlib for better path management


# Function to change the displayed image when the button is pressed
def changeImage():
    print("Button pressed")
    global oldcharacter
    global image_num

    # Get the user input from the text box and strip any leading/trailing spaces
    character = text.get("1.0", "end").strip()
    character = str(character)

    # Check if the character input has changed since the last input
    if character != oldcharacter:
        newtype = True
        print("New Type")
    else:
        newtype = False
        print("Same Character")

    if character != " ":  # If the input is not empty or just a space
        oldcharacter = character  # Update oldcharacter to the current input

        # Define the base directory path using Path from pathlib
        base_directory = Path("./Support Files/Images folder GUI II")
        file_path = base_directory / character  # Create the path to the character's folder

        # Check if the path exists and is a directory
        if file_path.exists() and file_path.is_dir():
            # List all .JPG files in the directory
            image_files = list(file_path.glob("*.JPG"))
            print(image_files)
            if image_files:  # If there are images in the folder
                if newtype:  # Reset the image number if it's a new character
                    image_num = 0
                else:  # Move to the next image in the folder if it's the same character
                    image_num += 1
                    if image_num >= len(image_files):  # Loop back to the first image if out of range
                        image_num = 0

                # Load the selected image
                image = Image.open(image_files[image_num])
                image = image.resize((300, 300))  # Resize the image to fit in the canvas
                tk_image = ImageTk.PhotoImage(image)

                # Display the image on the canvas
                canvas.create_image(150, 150, image=tk_image)
                canvas.image = tk_image  # Keep a reference to avoid garbage collection
            else:
                print(f"No images found in {file_path}")  # No images found message
        else:
            print(f"The path {file_path} does not exist or is not a directory.")  # Path not found message


# Initialize variables
image = None
oldcharacter = None
image_num = 0

# Create the main Tkinter window
window = tk.Tk()
window.title("Displaying Images Characters")  # Set the window title
window.geometry("300x400")  # Set the window size

# Create a label widget
hello = tk.Label(text="Type a Character")
hello.grid(row=0, column=1)

# Create a text box for user input
text = tk.Text(window, height=1, width=25)
text.grid(row=1, column=1)

# Create a button that triggers the image display based on user input
button = tk.Button(text="View Images", command=changeImage)
button.grid(row=2, column=1)

# Create a canvas to display the images
canvas = tk.Canvas(window, width=300, height=150)
canvas.grid(row=3, column=1)

# Start the Tkinter main event loop
tk.mainloop()
