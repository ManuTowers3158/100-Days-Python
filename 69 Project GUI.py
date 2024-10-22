# This script creates a simple interactive story using Tkinter. 
# The user is presented with a series of scenes and choices that lead to different outcomes.
# Images and text are updated based on user input.

from PIL import Image, ImageTk  # Import necessary modules for image handling
import tkinter as tk  # Import the Tkinter module for GUI
from pathlib import Path  # Import Path from pathlib for better path management

# Function to change the scene based on user input (button clicks)
def changeScene(value):
    global stage  # Track the current stage of the story
    global button1  # Reference to button1 for updating its text
    global button2  # Reference to button2 for updating its text
    global canvas  # Reference to the canvas for updating images
    global text  # Reference to the text label for updating scene text

    # Variables to hold updated content for the scene
    title_text = None
    scene_text = None
    botton1_text = None
    botton2_text = None
    image_scene = None

    value = int(value)
    print(f"Button {value} pressed")

    # Update content based on the current stage and user input
    if value == 1 and stage == 0:
        title_text = "Scene2"
        scene_text = "¿Estas dispuesto a hacer el esfuerzo necesario para ser quien tienes que ser?"
        botton1_text = "A huevo"
        botton2_text = "No me quedo en mi cama"
        image_scene = "./Support Files/Images_GUI_Project/2.jpeg"

    elif value == 2 and stage == 0:
        title_text = "Scene3"
        scene_text = "Aunque te caigas, nunca es tarde hoy puedes salir del hoyo"
        botton1_text = "A huevo me levanto y creo en mi"
        botton2_text = "No es muy dificil"
        image_scene = "./Support Files/Images_GUI_Project/3.jpg"

    elif value == 1 and stage == 1:
        title_text = "Good Ending"
        scene_text = "Bien, Ganaste"
        botton1_text = "start again"
        botton2_text = " "
        image_scene = "./Support Files/Images_GUI_Project/4.jpg"

    elif value == 2 and stage == 1:
        title_text = "Bad Ending"
        scene_text = "Perdiste"
        botton1_text = "start again"
        botton2_text = " "
        image_scene = "./Support Files/Images_GUI_Project/5.jpg"

    elif stage == 2:
        stage = -1  # Reset stage to initial
        title_text = "Scene1"
        scene_text = "Si el pasado puede doler, pero puedes huir de el o aprender"
        botton1_text = "Aprender"
        botton2_text = "Huir"
        image_scene = "./Support Files/Images_GUI_Project/1.png"

    # Update the title
    title = tk.Label(text=title_text)
    title.grid(row=1, column=2, sticky="ew")  # Align to the center

    # Update the image for the scene
    canvas.delete("all")  # Clear any previous images
    image = Image.open(image_scene)  # Open the selected image
    image = image.resize((300, 300))  # Resize the image to fit in the canvas
    tk_image = ImageTk.PhotoImage(image)
    canvas.create_image(150, 150, image=tk_image)  # Display the image on the canvas
    canvas.image = tk_image  # Keep a reference to avoid garbage collection

    # Update the scene text
    text.grid_forget()  # Remove the old text widget
    text = tk.Label(window, height=1, width=200, text=scene_text)
    text.grid(row=3, column=2)  # Display the new text

    # Update the buttons with new text
    button1.grid_forget()  # Remove the old button1
    button2.grid_forget()  # Remove the old button2
    button1 = tk.Button(text=botton1_text, command=lambda: changeScene("1"))
    button1.grid(row=4, column=2)
    button2 = tk.Button(text=botton2_text, command=lambda: changeScene("2"))
    button2.grid(row=5, column=2)

    # Move to the next stage of the story
    stage += 1
    if stage == 2:
        button2.grid_forget()  # Hide button2 if we reach the end of the story

# Initialization
image = None
oldcharacter = None
image_num = 0
stage = 0  # Initial stage of the story
window = tk.Tk()
window.title("Story")  # Set the window title
window.geometry("500x400")  # Set the window size

# Configure grid for centering content
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_columnconfigure(4, weight=1)

# Title
title = tk.Label(text="The choice is always yours")
title.grid(row=0, column=2, sticky="ew")

# Scene
title = tk.Label(text="Scene1")
title.grid(row=1, column=2, sticky="ew")

# Canvas for images
canvas = tk.Canvas(window, width=300, height=150)
canvas.grid(row=2, column=2)

# Load and display the first image
tk_image = ImageTk.PhotoImage(file="Support Files/Images_GUI_Project/1.png")
canvas.create_image(150, 150, image=tk_image)
canvas.image = tk_image  # Keep a reference to avoid garbage collection

# Scene text
text = tk.Label(window, height=1, width=100, text="Si el pasado puede doler, pero puedes huir de el o aprender")
text.grid(row=3, column=2)

# Buttons to make choices in the story
button1 = tk.Button(text="Aprender", command=lambda: changeScene("1"))
button1.grid(row=4, column=2)
button2 = tk.Button(text="Huir", command=lambda: changeScene("2"))
button2.grid(row=5, column=2)

# Start the Tkinter main event loop
tk.mainloop()
