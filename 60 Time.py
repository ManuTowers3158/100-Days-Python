# This script calculates the number of days left until a specified event date, input by the user, and displays a message depending on the countdown.

import datetime  # Import the datetime module for working with dates

print("***********Event Countdown***********")
print("Jefe Maestro introduzca la fecha de ese dia especial que tanto espera")  # Prompt the user for the event date

# Get day, month, and year from user input
day = int(input("Dia: "))
month = int(input("Mes: "))
year = int(input("Año: "))

# Create a date object for the event date
event = datetime.date(year, month, day)
print(event)  # Print the event date for confirmation

# Get today's date
today = datetime.date.today()
print(today)  # Print today's date for confirmation

# Calculate the difference between the event date and today's date
delta = event - today
flag = delta.days  # Get the number of days until the event

# Check if the event is today
if flag == 0:
    print("Jefe es hoy es hooooy")  # Event is today
else:
    print("Jefe faltan todavia", delta.days, "dias")  # Print how many days are left
    print("Tendremos que esperar mas!")  # Display a waiting message if the event is in the future
