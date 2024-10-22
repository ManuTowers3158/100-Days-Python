from getpass import getpass as input  # Import 'getpass' to safely hide input (used for player moves)

# Print the title of the game
print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()

# Ask players to select their move
print("Select your move (R, P or S)")
print()

# Get Player 1's move and hide the input (so Player 2 can't see it)
player1Move = input("Player 1 > ")
print()

# Get Player 2's move, also hidden from view
player2Move = input("Player 2 > ")
print()

# Check Player 1's move
if player1Move == "R":  # If Player 1 picked Rock
    # Compare Player 2's move with Player 1's Rock
    if player2Move == "R":
        print("You both picked Rock, draw!")
    elif player2Move == "S":
        print("Player1 smashed Player2's Scissors into dust with their Rock!")
    elif player2Move == "P":
        print("Player1's Rock is smothered by Player2's Paper!")
    else:
        print("Invalid Move Player 2!")  # Invalid move by Player 2

elif player1Move == "P":  # If Player 1 picked Paper
    # Compare Player 2's move with Player 1's Paper
    if player2Move == "R":
        print("Player2's Rock is smothered by Player1's Paper!")
    elif player2Move == "S":
        print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
    elif player2Move == "P":
        print("Two bits of paper flap at each other. Disappointing. Draw.")
    else:
        print("Invalid Move Player 2!")  # Invalid move by Player 2

elif player1Move == "S":  # If Player 1 picked Scissors
    # Compare Player 2's move with Player 1's Scissors
    if player2Move == "R":
        print("Player 2's Rock makes metal-dust out of Player1's Scissors")
    elif player2Move == "S":
        print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif player2Move == "P":
        print("Player1's Scissors make confetti out of Player2's paper!")
    else:
        print("Invalid Move Player 2!")  # Invalid move by Player 2

else:
    print("Invalid Move Player 1!")  # Invalid move by Player 1
