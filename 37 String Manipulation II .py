# Star Wars Name Generator
print("STAR WARS NAME GENERATOR")

# Get the user's first name and strip any leading/trailing spaces
first = input("First Name: ").strip()

# Get the user's last name and strip any leading/trailing spaces
last = input("Last Name: ").strip()

# Get the user's mother's maiden name and strip spaces
maiden = input("Mum's maiden name: ").strip()

# Get the user's birth city and strip spaces
city = input("City where you were born: ").strip()

# Generate the Star Wars name by combining parts of the inputs
# - First 3 letters of the first name, capitalized
# - First 2 letters of the last name, lowercase
# - First 2 letters of the maiden name, capitalized
# - Last 3 letters of the birth city, lowercase
name = f"{first[:3].title()}{last[:2].lower()}{maiden[:2].title()}{city[-3:].lower()}"

# Print out the generated Star Wars name
print(f"Your Star Wars name is {name}")
