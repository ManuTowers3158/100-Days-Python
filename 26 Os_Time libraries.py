import os  # Import the os module to use system commands (like clearing the screen)
import time  # Import the time module to add delays between prints

# Introduce a 1-second delay
time.sleep(1)

# Print a greeting message
print("Mi compaaaaaaaaaaaaaaa")

# Introduce another 1-second delay
time.sleep(1)

# Print another message
print("Muy buenos dias")

# Another 1-second delay
time.sleep(1)

# Print an encouraging message
print("Espero le este dando bien duro al modo guerra")

# Another 1-second delay
time.sleep(1)

# Clear the screen using the "cls" command on Windows systems
os.system("cls")

# Introduce a short delay after clearing the screen
time.sleep(0.1)

# Ask the user what they plan to do today
print("¿Que vas a hacer el día de hoy?")

# Add a 1-second delay before showing the options
time.sleep(1)

# Display a menu with options and get the user's response as an integer
menu = int(input("1: Ir al gym\n2: Estudiar\n3: Chambear\n4: Escribirle a mi ex\nRespuesta: "))

# Check if the user chose option 1 (Ir al gym)
if menu == 1:
    time.sleep(1)
    print("Muy bien mi compa muy bien, a darle que ladrillo a ladrillo se hace castillo")

# Check if the user chose option 2 (Estudiar)
elif menu == 2:
    time.sleep(1)
    print("Muy bien mi compa muy bien, a darle que ladrillo a ladrillo se hace castillo")

# Check if the user chose option 3 (Chambear)
elif menu == 3:
    time.sleep(1)
    print("Muy bien mi compa muy bien, a darle que ladrillo a ladrillo se hace castillo")

# If the user chose any other option (including option 4)
else:
    time.sleep(1)
    print("No mame mi compa, no mame, recuerde que usted es bien verga")
