# Define the function 'whichcake' that takes three arguments: ingredient, base, and coating
def whichcake(ingredient, base, coating):
    # Check if the ingredient is "Chocolate"
    if ingredient == "Chocolate":
        print("mmm, chocolate cake is amazing")

    # Check if the ingredient is "Broccoli"
    elif ingredient == "Brocolli":
        print("WTF")  # Funny reaction for broccoli as an ingredient

    # If the ingredient is neither "Chocolate" nor "Broccoli"
    else:
        print("Oh ok all right!")  # Neutral response for other ingredients

    # Print the full description of the cake based on the user's choices
    print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")


# Ask the user to input their chosen ingredient
userIngredient = input("Name an ingredient:")

# Ask the user to input their chosen base for the cake
userBase = input("Name a type of base:")

# Ask the user to input their favorite cake topping
userCoating = input("Fave cake topping:")

# Call the function 'whichcake' with the user's inputs as arguments
whichcake(userIngredient, userBase, userCoating)

