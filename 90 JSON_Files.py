import requests, json

# Loop to generate 10 random users
for num_persons in range(1, 11):
    # Fetch random user data from the Random User API
    result = requests.get("https://randomuser.me/api/")
    user = result.json()  # Convert the response to JSON format

    # Loop through the "results" list in the returned JSON (even though there's only one person per request)
    for person in user["results"]:
        # Extract the user's first and last name
        name = f"""{person["name"]["first"]} {person["name"]["last"]}"""

        # Print the user number and their name
        print(num_persons, name)

        # Fetch the user's profile picture using the URL in the JSON response
        picture = requests.get(person["picture"]["medium"])

        # Define the path and filename where the picture will be saved (in Images_random_users folder)
        path = f"""Support Files/Images_random_users/{num_persons} {name}.jpg"""

        # Open the file in write-binary mode and save the picture content
        with open(path, "wb") as f:
            f.write(picture.content)  # Write the binary content of the picture to the file


