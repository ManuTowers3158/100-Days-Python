# • User Prompt:
# 	• Prompt the user to type in a letter.
# • Letter Checking:
# 	• Check if the letter exists in the target word.
# • Display String:
# 	• Show a string with blanks for letters not yet guessed and reveal the guessed letters.
# • Tracking:
# 	• Maintain a running list of guessed letters.
# 	• Count how many times the user picks a letter not in the word.
# • Game Over Conditions:
# 	• End the game if the user picks more than six incorrect letters.
# 	• Declare victory if the user reveals all the letters in the word.
# • Additional Features (Optional):
# 	• Include ASCII art of hangman graphics.
# Enhance the appearance of the game, possibly using ASCII art for hangman graphics.
import random  # Import the random module for selecting a random word

Palabras = ["Pug", "Manu", "Crayoli", "Chemco", "Cheems"]  # List of possible words
Target = random.choice(Palabras)  # Randomly select a target word
Palabra_descubierta = []  # List to keep track of guessed letters

vidas = 3  # Set initial lives

# Main game loop
while True:
    Guess = input("Pon una letra:\n>>>")  # Prompt for a letter

    # Check for duplicate guesses
    if Guess not in Palabra_descubierta:
        Palabra_descubierta.append(Guess)  # Add the guessed letter
    else:
        print("Ya escogiste esa letra")  # Inform about the duplicate
        continue  # Skip to the next iteration

    # Check if the guess is incorrect
    if Guess not in Target:
        vidas -= 1  # Decrease lives
        if vidas == 0:  # Check for game over
            print("Se acabo mi compa")  # Inform the user
            break

    # If the guess is correct, display the current state of the word
    if Guess in Target:
        # Loop through target to display guessed letters
        for x in Target:
            if x in Palabra_descubierta:
                print(x, end='')  # Print correctly guessed letter
            else:
                print("_", end='')  # Print underscore for unguessed letters

    # Check if the player has won
    if all(letter in Palabra_descubierta for letter in Target):  # Check if all letters are guessed
        print("Very good acabas de ganar!")  # Inform the user of victory
        break  # Exit the loop

