import requests, json
from datetime import datetime

def format_date(date_str):
    # Convert a date string (YYYY-MM-DD format) to a datetime object
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    # Format the date with a suffix for the day (e.g., "10th", "1st")
    day = int(date_obj.strftime("%d"))  # Extract the day as an integer
    suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")  # Handle special suffixes
    return date_obj.strftime(f"%B {day}{suffix}, %Y")  # Return the date in "Month day(suffix), Year" format


def get_temperature_emoji(temp):
    # Return an emoji based on the temperature range
    if temp < 10:
        return "❄️"  # Cold temperature
    elif temp > 20:
        return "🔥"  # Hot temperature
    else:
        return ""  # No emoji for moderate temperature


def display_daily_temperatures(data):
    # Extract relevant temperature data from the JSON response
    dates = data['daily']['time']
    max_temps = data['daily']['temperature_2m_max']
    min_temps = data['daily']['temperature_2m_min']

    # Loop through each day's data to display the formatted temperatures
    for i in range(len(dates)):
        formatted_date = format_date(dates[i])  # Format the date
        max_temp_emoji = get_temperature_emoji(max_temps[i])  # Get emoji for max temp
        min_temp_emoji = get_temperature_emoji(min_temps[i])  # Get emoji for min temp

        # Display the temperatures with emojis and formatted date
        print(f"Day: {formatted_date}")
        print(f"  Max Temperature: {max_temps[i]}°C {max_temp_emoji}")
        print(f"  Min Temperature: {min_temps[i]}°C {min_temp_emoji}")
        print("-" * 30)  # Separator for readability


# Set the location and timezone for the weather API request
timezone = "GMT"
latitude = 48.766
longitude = 11.433

# Request weather data from the Open-Meteo API
result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&"
                      f"longitude={longitude}&daily=weathercode,temperature_2m_max,"
                      f"temperature_2m_min&timezone={timezone.upper()}")

# Parse the API response as JSON
user = result.json()

# Display the daily temperature data
display_daily_temperatures(user)
