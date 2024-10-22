import requests
from bs4 import BeautifulSoup

# URL of the Hacker News website
url = 'https://news.ycombinator.com/'

# Send a GET request to the URL and retrieve the HTML content of the page
response = requests.get(url)
html = response.text  # Store the HTML content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all the news article titles within <span> tags that have the class "titleline"
myLink = soup.find_all("span", {"class": "titleline"})

# List of keywords to search for in the article titles
things = ['python', 'AI', 'Machine Learning', 'Artificial Intelligence', 'code']

# Loop through each news title
for link in myLink:
    text = link.text  # Extract the text of the title
    textList = text.split()  # Split the title text into individual words
    containsWord = False  # Initialize a flag to track if a keyword is found

    # Loop through each word in the title
    for word in textList:
        # If the word (converted to lowercase) matches any word in the 'things' list
        if word.lower() in things:
            containsWord = True  # Set the flag to True if a keyword is found

    # If a keyword was found in the title, print the title and the associated link
    if containsWord:
        print(link.text)  # Print the article title

        # Find the <a> tag within the titleline to get the actual link
        myLink = link.find_all("a")

        # Print the href attribute (URL) of the first link in the list
        print(myLink[0]["href"])

