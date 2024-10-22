import os  # Import the os module to execute system commands (like clearing the terminal)
import time  # Import the time module to introduce delays

# Define a multi-line string 'spam' containing motivational messages
spam = "Quiérete a ti mismo, cree en ti mismo. Quiérete tanto que sepas que, al quererte, tienes el talento y la capacidad para lograr cualquier meta que te propongas. " \
       "Mantén siempre una actitud positiva. En la vida, te encontrarás con lo que esté en tu mente. Si piensas positivamente, tendrás energías positivas." \
       " A veces aspiramos a que muchos nos quieran cuando la mayoría de la gente no se quiere a sí misma. Quiérete mucho y cree mucho en lo que puedes lograr. Proponte metas muy altas, porque las vas a poder alcanzar. " \
       "Y si eventualmente te frustras o fracasas en ese empeño, descubrirás lo lejos que puedes llegar."

# Initialize an empty list to store email addresses
listofEmails = []

# Define a function 'prettyPrint' to display the list of emails
def prettyPrint():
    os.system("cls")  # Clear the terminal screen
    print("List of Emails")  # Print the header
    print()  # Print a blank line
    counter = 1  # Initialize a counter for numbering the emails

    # Loop through each email in the list and print it with a number
    for email in listofEmails:
        print(f"{counter}:{email}")  # Print the current email with its number
        counter += 1  # Increment the counter

    time.sleep(1)  # Pause for 1 second before proceeding
    # Optional loop with index (commented out)
    # for index in range(len(listofEmails)):
    #     print(f"{index}:{listofEmails[index]}")
    # time.sleep(1)

# Start an infinite loop for the main menu
while True:
    os.system("cls")  # Clear the terminal screen
    print("SPAMMER Inc.")  # Print the company name
    # Display the menu options and get the user's choice
    menu = input("1: Add email \n2: Remove email \n3: Show email\n4: Get SPAMMING\n>")

    # If the user chooses to add an email
    if menu == "1":
        email = input("Type the email you want to add?:\n> ")  # Prompt for the email address
        listofEmails.append(email)  # Add the email to the list

    # If the user chooses to remove an email
    elif menu == "2":
        print("Current agenda is:")  # Indicate the current list
        prettyPrint()  # Call the prettyPrint function to show the emails
        email = input("Which email do you want to remove?: ")  # Prompt for the email to remove
        listofEmails.remove(email)  # Remove the specified email from the list

    # If the user chooses to show the emails
    elif menu == "3":
        prettyPrint()  # Call the prettyPrint function to display the list of emails

    # If the user chooses to send spam emails
    elif menu == "4":
        # Loop through each email in the list
        for index in range(len(listofEmails)):
            print(f"Email {index + 1}:")  # Print the email number
            print()  # Print a blank line
            print(f"Dear {listofEmails[index]}")  # Address the email to the recipient
            print(spam)  # Print the spam message
            time.sleep(3)  # Pause for 3 seconds before sending the next email
            os.system("cls")  # Clear the terminal screen after each email

    # If the user inputs anything else, exit the loop
    else:
        break;  # Break the loop and exit

print("See you soon")  # Print a farewell message after exiting
