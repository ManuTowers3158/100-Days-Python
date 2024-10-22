# Gather user input for contact details
name = input("Name: ").strip().capitalize()  # Prompt for name, remove extra spaces, and capitalize
dob = input("Date of Birth: ").strip()  # Prompt for date of birth
tel = input("Telephone number: ").strip()  # Prompt for telephone number
email = input("Email: ")  # Prompt for email
address = input("Address: ")  # Prompt for address

# Create a dictionary to store contact information
contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}

# Print the contact information in a formatted manner
print()
print(f"Name: {contact['name']}")
print(f"DoB: {contact['dob']}")
print(f"Tel: {contact['tel']}")
print(f"Email: {contact['email']}")
print(f"Address: {contact['address']}")
