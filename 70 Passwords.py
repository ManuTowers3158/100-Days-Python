# This script checks the user's password against environment variables to grant access.
# There are two passwords: one for an admin (Captain Torres) and another for a regular user (Maquina de chambear).

import os  # Import the os module to access environment variables

# Retrieve admin and user passwords from environment variables
admin_password = os.getenv('API_KEY')  # Admin password stored in 'API_KEY'
user_password = os.getenv('API_KEY2')  # User password stored in 'API_KEY2'

# Debugging print statements to check the retrieved passwords (optional, remove in production)
print(admin_password)
print(user_password)

# Prompt the user to input a password
userPass = input("Password: ")

# Check if the input matches the admin password
if userPass == admin_password:
    print("Welcome aboard Captain Torres, all systems ready to engage")  # Admin access message

# Check if the input matches the user password
elif userPass == user_password:
    print("Welcome Maquina de chambear")  # User access message

# If the input doesn't match any of the passwords
else:
    print("Better luck next time")  # Failed access message
