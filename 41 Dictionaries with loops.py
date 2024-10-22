# • Dictionary Definition:
# 	• Define a dictionary to store information about a website.
# 	• The dictionary should have keys for:
# 		○ Website's name.
# 		○ URL.
# 		○ Brief description.
# 		○ Five-star rating (optional).
# • User Input:
# 	• Use a loop to:
# 		○ Print the names of the keys.
# 		○ Ask the user to input values for each key.
# 		○ Store the user's input in the dictionary.
# • Display Dictionary:
# 	• Print out the entire dictionary using a loop.
# • Optional:
# 	• Use subroutines to organize the code and make it easier to understand.
# • Objective:
# Create a functional and user-interactive dictionary to store and display website information.

# Initialize a dictionary with placeholders for various attributes
dictionary = {"Name": None, "URL": None, "Brief description": None, "Five-Star Rating": None}

# Loop through the keys in the dictionary to collect user input
for x in dictionary:
    print("Provide", x)  # Prompt the user for each attribute
    value = input(">>>")  # Get user input
    dictionary[x] = value  # Store the input in the dictionary

# Print the contents of the dictionary in a formatted manner
for item, value in dictionary.items():
    print(f"{item}: {value}")  # Display each key-value pair

print("End of loop chief")  # Indicate the end of the process
