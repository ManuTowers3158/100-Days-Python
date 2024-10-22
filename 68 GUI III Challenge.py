# This script creates a Tkinter GUI that displays images based on user input (character name).
# If no images are found for the entered character, a "Character not Found" message is shown.

from PIL import Image, ImageTk  # Import necessary modules for image handling
import tkinter as tk  # Import the Tkinter module for GUI
from pathlib import Path  # Import Path from pathlib for better path management

# Function to change the displayed image when the button is pressed
def changeImage():
    print("Button pressed")
    global oldcharacter
    global image_num
    global notfound

    # Get user input from the text box and strip leading/trailing spaces
    character = text.get("1.0", "end").strip()
    character = str(character)

    # Determine if the input is different from the last one
    if character != oldcharacter:
        newtype = True
        print("New Type")
    else:
        newtype = False
        print("Same Character")

    # Proceed only if input is not empty
    if character != " ":
        oldcharacter = character  # Update oldcharacter to the current input

        # Define the base directory path using Path
        base_directory = Path("./Support Files/Images folder GUI II")
        file_path = base_directory / character  # Create the path to the character's folder

        # Check if the path exists and is a directory
        if file_path.exists() and file_path.is_dir():
            # List all .JPG files in the directory
            image_files = list(file_path.glob("*.JPG"))
            print(image_files)

            if image_files:  # If there are images in the folder
                if newtype:  # Reset image_num if it's a new character
                    image_num = 0
                else:  # Move to the next image if it's the same character
                    image_num += 1
                    if image_num >= 4:  # Reset to the first image if more than 4 images
                        image_num = 0

                # Show the canvas and hide the "Character not Found" message
                canvas.grid(row=3, column=1)
                notfound.grid_forget()

                # Load the selected image and resize it
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
            canvas.grid_forget()  # Hide the canvas
            notfound = tk.Label(text="Character not Found")  # Show the "Character not Found" message
            notfound.grid(row=3, column=1)

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

# Create a label to show "Character not Found" when no images are found
notfound = tk.Label(text="Character not Found")
notfound.grid(row=3, column=1)
notfound.grid_forget()  # Hide it initially

# Start the Tkinter main event loop
tk.mainloop()
