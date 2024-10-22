import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

from_email = 'example@gmail.com'  # Replace with your email
to_email = 'example@gmail.com'  # Replace with recipient email
subject = 'Price Alert: DJI Neo Fly Drone' # Replace with your subject
#email_password = 'oqgd ecfo jkfy jkrv' #replace with your email api password
email_password = os.getenv('EMAIL_PASSWORD')


# Function to get the product price
def get_price():
    # URL of the product page to scrape
    url = 'https://www.wexphotovideo.com/dji-neo-fly-more-combo-3187357/'

    # Send a GET request to the webpage
    response = requests.get(url)

    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the price from the HTML using the 'span' tag with class 'price wex-red'
    price_text = soup.find('span', class_='price wex-red').text.strip()

    # Remove the pound symbol and commas, then convert the price to a float
    price_value = float(price_text.replace('£', '').replace(',', ''))

    # Return the price as a float value
    return price_value


# Function to send an email if the price is below the threshold
def send_email(price):
    # Construct the email message with the current price
    message = f'The price of the DJI Neo Fly More Combo is now £{price}. It\'s below £400, grab it now!'

    # Create a MIMEMultipart email object
    msg = MIMEMultipart()
    msg['From'] = from_email  # Sender's email address
    msg['To'] = to_email  # Recipient's email address
    msg['Subject'] = subject  # Email subject

    # Attach the plain text message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Send the email through the SMTP server
    try:
        # Connect to the Gmail SMTP server on port 587
        server = smtplib.SMTP('smtp.gmail.com', 587)  # You can replace with another SMTP server if necessary
        server.starttls()  # Start TLS encryption
        server.login(from_email, email_password)  # Login to the sender's email account
        server.sendmail(from_email, to_email, msg.as_string())  # Send the email
        server.quit()  # Close the connection to the server
        print(f"Email sent to {to_email}")  # Confirmation message
    except Exception as e:
        # Print an error message if the email fails to send
        print(f"Failed to send email: {e}")


# Main function to check the price and send an email if necessary
def check_price_and_alert():
    # Call the get_price function to retrieve the current product price
    price = get_price()

    # Print the current price for information
    print(f"Current Price: £{price}")

    # Check if the price is below the threshold of £400
    if price < 400:
        # Send an alert email if the price is below the threshold
        send_email(price)
    else:
        # Print a message if the price is still above the threshold
        print("Price is still above £400.")


# Call the main function if the script is run as the main program
if __name__ == "__main__":
    check_price_and_alert()
