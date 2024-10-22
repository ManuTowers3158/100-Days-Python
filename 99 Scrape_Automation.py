import requests
from bs4 import BeautifulSoup
import os
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Schedule the email to be sent every 1 second (adjust as necessary)
import schedule
import time

mail = 'example@gmail.com'
password = os.getenv('EMAIL_PASSWORD')
# Wikipedia URL containing the table of 2024 films
url = "https://en.wikipedia.org/wiki/2024_in_film"  # Replace with the correct URL if necessary

# Get the page content from the URL
response = requests.get(url)
html = response.text  # Store the HTML content of the page

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the specific table with the class 'wikitable sortable'
table = soup.find('table', {'class': 'wikitable sortable'})

# Initialize a list to hold the extracted movie data
movies = []

# Extract all the rows from the table body
rows = table.find('tbody').find_all('tr')

# Initialize a variable to hold the distributor in case of rowspan (merged cells)
distributor_holder = None

# Loop through each row, starting from the second row (skipping headers)
for row in rows[1:]:
    # Extract the columns (th or td tags)
    columns = row.find_all(['th', 'td'])

    # Check if the row has 4 columns (complete data for rank, title, distributor, gross)
    if len(columns) == 4:
        # Extract data from each column
        rank = columns[0].get_text(strip=True)  # Movie rank
        title = columns[1].get_text(strip=True)  # Movie title
        distributor = columns[2].get_text(strip=True)  # Distributor name
        domestic_gross = columns[3].get_text(strip=True)  # Domestic gross earnings

        # Store the distributor to reuse if necessary (for rows with missing distributor)
        distributor_holder = distributor

        # Append the movie data to the movies list as a dictionary
        movies.append({
            'Rank': rank,
            'Title': title,
            'Distributor': distributor,
            'Domestic Gross': domestic_gross
        })

    # Check if the row has 3 columns (missing distributor due to rowspan)
    elif len(columns) == 3:
        # Extract data, leaving out distributor (will reuse distributor_holder)
        rank = columns[0].get_text(strip=True)
        title = columns[1].get_text(strip=True)
        domestic_gross = columns[2].get_text(strip=True)

        # Append the movie data with the previous distributor
        movies.append({
            'Rank': rank,
            'Title': title,
            'Distributor': distributor_holder,  # Reuse the previous distributor
            'Domestic Gross': domestic_gross
        })

    else:
        # Print a message for rows with insufficient columns (neither 3 nor 4 columns)
        print(f"Skipping row due to insufficient columns: {columns}")

# Print the extracted movie data to the console for verification
for movie in movies:
    print(movie)


# Function to format the extracted movie data for pretty output
def pretty_print(movies):
    # Create a list to hold the formatted output
    output = []

    # Add the header to the output with appropriate spacing
    output.append(f"{'Rank':<5} {'Title':<35} {'Distributor':<20} {'Domestic Gross':>15}")
    output.append("-" * 80)  # Add a separator line

    # Loop through the movie list and format each movie's details
    for movie in movies:
        rank = movie['Rank']  # Rank of the movie
        title = movie['Title']  # Title of the movie
        distributor = movie['Distributor']  # Distributor of the movie

        # Clean up the Domestic Gross field by removing anything inside brackets
        gross = movie['Domestic Gross'].split('[')[0].strip()

        # Append the formatted movie details to the output list
        output.append(f"{rank:<5} {title:<35} {distributor:<20} {gross:>15}")

    # Join the output list into a single string with <br> for HTML line breaks
    return "<br>".join(output)


# Call the pretty_print function to format and display the movie list
pretty_print(movies)


def sendMail():
    # Use the pretty_print function to generate a formatted list of movies
    email_content = pretty_print(movies)

    # Define the SMTP server and port for Gmail
    server = "smtp.gmail.com"
    port = 587

    # Create an SMTP connection to the email server
    s = smtplib.SMTP(host=server, port=port)

    # Start TLS encryption for secure email transfer
    s.starttls()

    # Log in to the email account with the provided credentials
    s.login(mail, password)

    # Create a new email message using MIMEMultipart
    msg = MIMEMultipart()
    msg["To"] = "example@gmail.com"  # Recipient email (replace "example" with actual recipient)
    msg["From"] = mail  # Sender email
    msg["Subject"] = "Daily Movie List"  # Email subject

    # Attach the formatted movie list to the email in HTML format
    msg.attach(MIMEText(email_content, 'html'))

    # Send the email message through the SMTP connection
    s.send_message(msg)

    # Close the SMTP connection
    s.quit()

    # Delete the email message object to free up memory
    del msg


# Schedule the sendMail function to run every 1 second
schedule.every(1).seconds.do(sendMail)

# Infinite loop to keep the script running and checking for pending scheduled tasks
while True:
    # Run the scheduled task if it's pending
    schedule.run_pending()

    # Sleep for 1 second before checking again
    time.sleep(1)
