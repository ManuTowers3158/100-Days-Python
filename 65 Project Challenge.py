# This script defines a basic character class structure, and extends it to include specific roles such as player and enemy types 
# (orc and vampire). Each class has its own attributes and a method to display its details.

# Base class for general character attributes
class character:
    name = None  # Character's name
    health = None  # Character's health points
    magic = None  # Character's magic points

    # Constructor to initialize the character class
    def __init__(self, name, health, magic):
        self.name = name
        self.health = health
        self.magic = magic

    # Method to print a summary of the character's details
    def Summary(self):
        print(f"Character: {self.name}\nHealth: {self.health},\nMagic: {self.magic}\n")


# Player class inheriting from the character class
class player(character):
    number_lives = None  # Number of lives the player has
    alive_status = None  # Status of whether the player is alive or dead

    # Constructor to initialize the player class with additional number of lives
    def __init__(self, name, health, magic, number_lives):
        self.name = name
        self.health = health
        self.magic = magic
        self.number_lives = int(number_lives)  # Convert lives to integer

        # Determine if the player is alive based on the number of lives
        if self.number_lives > 0:
            self.alive_status = "Alive Bitch"
        else:
            self.alive_status = "Killed"

    # Override method to print a summary of the player's details
    def Summary(self):
        print(
            f"Character: {self.name}\nHealth: {self.health},\nMagic: {self.magic},\nLives: {self.number_lives}\nStatus: {self.alive_status}\n")


# Enemy class inheriting from the character class
class enemy(character):
    day_time = None  # Attribute to store behavior based on time of day

    # Constructor to initialize the enemy class with additional attributes (type and strength)
    def __init__(self, name, health, magic, type, strength):
        self.name = name
        self.health = health
        self.magic = magic
        self.type = type  # Enemy type (e.g., Orc, Vampire)
        self.strength = strength  # Enemy strength

    # Override method to print a summary of the enemy's details
    def Summary(self):
        print(
            f"Character: {self.name}\nHealth: {self.health},\nMagic: {self.magic},\nType: {self.type}\nStrength: {self.strength}\n")


# Orc class inheriting from the enemy class
class orc(enemy):
    speed = None  # Orc speed attribute

    # Constructor to initialize the orc class with additional speed attribute
    def __init__(self, name, health, magic, type, strength, speed):
        self.name = name
        self.health = health
        self.magic = magic
        self.type = type
        self.strength = strength
        self.speed = speed  # Orc speed

    # Override method to print a summary of the orc's details
    def Summary(self):
        print(
            f"Character: {self.name}\nHealth: {self.health},\nMagic: {self.magic},\nType: {self.type}\nStrength: {self.strength}\nSpeed: {self.speed}\n")


# Vampire class inheriting from the enemy class
class vampire(enemy):
    day_time = None  # Time of day when the vampire is active

    # Constructor to initialize the vampire class with additional day_time attribute
    def __init__(self, name, health, magic, type, strength, day_time):
        self.name = name
        self.health = health
        self.magic = magic
        self.type = type
        self.strength = strength
        this.day_time = day_time  # Set vampire behavior based on day or night

    # Override method to print a summary of the vampire's details
    def Summary(self):
        print(
            f"Character: {self.name}\nHealth: {self.health},\nMagic: {self.magic},\nType: {self.type}\nStrength: {self.strength}\nBehavior: {self.day_time}\n")


# Creating and displaying various characters

Johny = character("Johny", "45", "72")
Johny.Summary()

Manu = player("Manu", "100", "89", "4")
Manu.Summary()

Orc1 = orc("Xonoth", "37", "29", "Orc", "57", "16")
Orc1.Summary()

Orc2 = orc("Ogol", "35", "26", "Orc", "62", "19")
Orc2.Summary()

Orc3 = orc("Bakh", "34", "31", "Orc", "59", "15")
Orc3.Summary()

vamp1 = vampire("Edward", "39", "40", "Vampire", "67", "Day")
vamp1.Summary()

vamp2 = vampire("Bella", "27", "58", "Vampire", "61", "Night")
vamp2.Summary()
