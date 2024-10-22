# Ask the user for their favorite TV show and store the response in the variable 'tv_show'
tv_show = input("What is your favorite TV Show?")

# Check if the user's favorite TV show is 'Game of Thrones'
if tv_show == "Game of thrones":
    # If true, print a response acknowledging the user's choice
    print("Nice")

    # Ask the user who their favorite character is and store it in 'favcharacter'
    favcharacter = input("Who is your favorite character?")

    # Check if their favorite character is 'Jon Snow'
    if favcharacter == "Jon Snow":
        # If true, print a response appreciating their choice
        print("You know your stuff")
    else:
        # If the favorite character is not 'Jon Snow', express disagreement
        print("nee Jon Snow is the greatest")

# Check if the user's favorite TV show is 'pokemon'
elif tv_show == "pokemon":
    # If true, print a positive response
    print("Great deal")

# If the user's favorite TV show is neither 'Game of Thrones' nor 'pokemon'
else:
    # Print a neutral response acknowledging their choice
    print("Yeah that´s cool and all")

