# Define the function 'AreaTriangle' that calculates the area of a triangle
# It takes two arguments: base and height
def AreaTriangle(base, height):
    # Calculate the area of the triangle using the formula (base * height) / 2
    area = (base * height) / 2
    # Return the calculated area
    return area

# Ask the user to input the base of the triangle and convert it to an integer
b = int(input("Introduce base: "))

# Ask the user to input the height of the triangle and convert it to an integer
h = int(input("Introduce height:"))

# Call the 'AreaTriangle' function with the base and height provided by the user
# Store the returned area value in the variable 'area'
area = AreaTriangle(b, h)

# Print the calculated area
print("The area is: ", area)
