import random  # Import the random module to generate random numbers

# List of random greetings
Saludos_random = ["Hello there", "Konichiwa", "Arigato gosaimas!", "Holi crayoli", "General Kenobi"]

# Loop through each greeting in the 'Saludos_random' list
for saludo in Saludos_random:
    # Generate a random number between 0 and 4 (since there are 5 items in the list)
    rnum = random.randint(0, 4)

    # Print the generated random number
    print(rnum)

    # Use the random number to print a random greeting from the list
    print(Saludos_random[rnum])
