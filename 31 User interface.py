# Define a function 'colorChange' that returns ANSI color codes based on the color argument
def colorChange(color):
    if color == "red":
        return "\033[31m"  # Return ANSI code for red
    elif color == "white":
        return "\033[0m"  # Return ANSI code to reset to default (white)
    elif color == "blue":
        return "\033[34m"  # Return ANSI code for blue
    elif color == "yellow":
        return "\033[33m"  # Return ANSI code for yellow
    elif color == "green":
        return "\033[32m"  # Return ANSI code for green
    elif color == "purple":
        return "\033[35m"  # Return ANSI code for purple

# Create a title string using multiple color changes in the title
title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}={colorChange('yellow')} Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="

# Print the centered title with color changes applied
print(f"            {title:^35}")

# Print the radio station name with fire and play emojis, reset to default color (white) afterward
print(f"🔥▶️\t{colorChange('white')}Radio Manu")

# Print the band name "Queen" in yellow
print(f"\t\t{colorChange('yellow')}Queen")

# Define three strings for buttons or commands: prev, next, and pause
prev = "prev"
next = "next"
pause = "pause"

# Print 'prev' left-aligned (default white color)
print(f"{colorChange('white')}{prev:<35}")

# Print 'next' center-aligned and in green
print(f"{colorChange('green')}{next:^35}")

# Print 'pause' right-aligned and in purple
print(f"{colorChange('purple')}{pause:>35}")
