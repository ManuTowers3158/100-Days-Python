import schedule, time ,os
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail = 'example@gmail.com'
password = os.getenv('EMAIL_PASSWORD')


def sendMail():
    # Get the email content by rolling the die and selecting a random quote
    email = roll_die_and_get_quote()

    # Define the SMTP server and port for Gmail
    server = "smtp.gmail.com"
    port = 587

    # Establish a connection to the Gmail SMTP server
    s = smtplib.SMTP(host=server, port=port)

    # Start TLS encryption for secure communication
    s.starttls()

    # Log in to the email account using the stored credentials
    s.login(mail, password)

    # Create a new email message using MIMEMultipart
    msg = MIMEMultipart()
    msg["To"] = "example@gmail.com"  # Replace with the recipient's email address
    msg["From"] = mail  # Sender's email address
    msg["Subject"] = "Daily quote"  # Subject of the email

    # Attach the randomly selected quote as the email body in HTML format
    msg.attach(MIMEText(email, 'html'))

    # Send the email message through the SMTP connection
    s.send_message(msg)

    # Delete the message object to free up memory
    del msg


# Dictionary containing daily quotes mapped to a die roll (1-5)
daily_quotes = {
    1: "Las personas exitosas siempre buscan oportunidades para ayudar a los demás.",
    2: "La clave del éxito es enfocar nuestra mente consciente en las cosas que deseamos, no en las que tememos.",
    3: "Desarrolla una actitud de gratitud y da gracias por todo lo que te sucede.",
    4: "Tu habilidad para disciplinarte, establecer metas claras y trabajar en ellas cada día hará más por garantizar tu éxito que cualquier otro factor.",
    5: "Haz lo que puedas donde estés, con lo que tienes y no te preocupes por el resto."
}


# Function to simulate rolling a die and return a random quote from daily_quotes
def roll_die_and_get_quote():
    # Simulate rolling a die with 5 sides (numbers 1-5)
    die_number = random.randint(1, 5)

    # Return the quote corresponding to the rolled die number
    return daily_quotes[die_number]


# Call the roll_die_and_get_quote function to select and display a random quote
selected_quote = roll_die_and_get_quote()
print(f"The selected quote is: {selected_quote}")


# Function to print a message and send the email
def printMe():
    print("Toi mandando el email")  # Print a message indicating the email is being sent
    sendMail()  # Call the sendMail function to send the email


# Schedule the printMe function to run every 1 second
schedule.every(1).seconds.do(printMe)

# Infinite loop to keep the scheduler running and check for pending tasks
while True:
    # Run any scheduled tasks that are pending
    schedule.run_pending()

    # Sleep for 1 second before checking again
    time.sleep(1)
