import os  # To execute system commands (like clearing the terminal)
import time  # To add delays between actions
import random  # To generate random numbers for rolling dice
import pygame  # Import pygame to handle sound playback

# Function to simulate rolling a six-sided dice
def sixRoll():
    sixvalue = random.randint(1, 6)  # Generate a random number between 1 and 6
    return sixvalue  # Return the rolled value


# Function to simulate rolling a twelve-sided dice
def twuelveRoll():
    twuelvevalue = random.randint(1, 12)  # Generate a random number between 1 and 12
    return twuelvevalue  # Return the rolled value


# Function to simulate rolling an eight-sided dice
def eightRoll():
    eightvalue = random.randint(1, 8)  # Generate a random number between 1 and 8
    return eightvalue  # Return the rolled value


# Function to calculate a character's health stat
def healthstat():
    A = sixRoll()  # Roll a six-sided dice
    B = twuelveRoll()  # Roll a twelve-sided dice
    health = (A * B) / 2 + 10  # Calculate health based on dice rolls
    return health  # Return the health value


# Function to calculate a character's strength stat
def strengthstat():
    A = sixRoll()  # Roll a six-sided dice
    B = eightRoll()  # Roll an eight-sided dice
    strength = (A * B) / 2 + 12  # Calculate strength based on dice rolls
    return strength  # Return the strength value

# Function to play a sound using pygame
def play_sound(sound_file):
    pygame.mixer.init()  # Initialize the pygame mixer
    pygame.mixer.music.load(sound_file)  # Load the sound file
    pygame.mixer.music.play()  # Play the sound


sound_file = "./Support Files/sword-battle.mp3"  # Path to the sound file for the battle

os.system("cls")  # Clear the terminal screen
print("⚔️Generate your legends⚔️")  # Display message to generate characters

# Collect details for the first character
name1 = input("Name your legend:\n")
type1 = input("Character type: Warrior, Mage, Elf etc\n")

# Display the first character's stats
print("May your name go down in legend ")
print(name1, "the", type1)
health1 = healthstat()  # Calculate the first character's health
print("Health:", health1)
strength1 = strengthstat()  # Calculate the first character's strength
print("Strength:", strength1)
time.sleep(2)  # Pause for 2 seconds
os.system("cls")  # Clear the terminal

# Collect details for the second character
name2 = input("Name your 2nd legend:\n")
type2 = input("Character type: Warrior, Mage, Elf etc\n")

# Display the second character's stats
print("May your name go down in legend ")
print(name2, "the", type2)
health2 = healthstat()  # Calculate the second character's health
print("Health:", health2)
strength2 = strengthstat()  # Calculate the second character's strength
print("Strength:", strength2)
time.sleep(2)  # Pause for 2 seconds
os.system("cls")  # Clear the terminal

i = 1  # Initialize round counter
print("⚔️Its time to battle⚔️")  # Display the start of the battle

# Battle loop that continues until one player's health reaches zero
while True:
    play_sound(sound_file)  # Play battle sound
    damage = abs(strength1 - strength2) + 1  # Calculate damage based on strength difference
    print("Round", i)  # Display the current round
    P1 = sixRoll()  # Player 1 rolls a six-sided dice
    print("Player 1 rolled", P1)
    P2 = sixRoll()  # Player 2 rolls a six-sided dice
    print("Player 2 rolled", P2)

    # If Player 1 rolls higher
    if P1 > P2:
        print("P1 rolled higher")
        health2 = health2 - damage  # Player 2 takes damage
        print("Player 2 took damage, Health:", health2)
        if health2 <= 0:  # Check if Player 2's health is 0 or below
            print("Player 2 died")
            break  # End the battle if Player 2 dies

    # If Player 2 rolls higher
    elif P1 < P2:
        print("P2 rolled higher")
        health1 = health1 - damage  # Player 1 takes damage
        print("Player 1 took damage, Health", health1)
        if health1 <= 0:  # Check if Player 1's health is 0 or below
            print("Player 1 died")
            break  # End the battle if Player 1 dies

    # If both players roll the same
    else:
        print("Tie")

    time.sleep(3)  # Pause for 3 seconds before the next round
    os.system("cls")  # Clear the terminal
    i = i + 1  # Increment the round counter

# Key Concepts and Brief Explanation:
# Randomized Stats: The character's health and strength are calculated using random dice rolls (sixRoll, eightRoll, twuelveRoll) to simulate RPG-like stat generation.
# Battle Loop: A continuous loop where two characters roll dice, and the one with the higher roll deals damage to the other until one player's health reaches zero.
# Damage Calculation: Damage is based on the absolute difference between the two characters' strengths, ensuring that even minor differences impact the battle.
# Sound Effect: The sound file (sword-battle.mp3) plays during each round of the battle to add an immersive experience.
# Round System: The game increments the round counter and keeps going until one player dies, printing the outcome for each round and updating player health.