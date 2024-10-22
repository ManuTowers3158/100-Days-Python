import requests
from bs4 import BeautifulSoup
import openai
import os


# Retrieve organization ID and API key from environment variables
organization_ID = os.getenv('OPENAI_ORGANIZATION_ID')
open_AI_key = os.getenv('OPENAI_API_KEY')

# Set OpenAI organization and API key
openai.organization = organization_ID
openai.api_key = open_AI_key


# Define the URL to scrape (Wikipedia page of Seto Kaiba)
url = 'https://en.wikipedia.org/wiki/Seto_Kaiba'

# Send a GET request to the URL and retrieve the HTML content of the page
response = requests.get(url)
html = response.text  # Store the HTML content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the main content area of the article using the 'mw-parser-output' class
article = soup.find_all("div", {"class": "mw-parser-output"})[0]

# Extract all the paragraph tags <p> from the article content
content = article.find_all("p")

# Initialize an empty string to hold the extracted text
text = ""
for p in content:
    text += p.text  # Append the text from each paragraph to the text string

# Generate a prompt for the OpenAI API, asking to summarize the extracted text in 2 paragraphs
prompt = f"Summarise the text in 2 paragraphs\n {text}"

# Make a call to the OpenAI GPT-3.5 API to get a summary of the extracted text
response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model to use
        messages=[{"role": "user", "content": prompt}],  # Use the prompt as the user message
        temperature=0,  # Set the temperature for deterministic output
        max_tokens=100  # Limit the number of tokens in the response
    )

# Print the summarized response generated by GPT-3.5
print(response["choices"][0]["message"]["content"].strip())
print()

# Find the list of references at the bottom of the article (in an <ol> tag with class 'references')
refs = soup.find("ol", {"class": "references"})

# If references are found, loop through and print the first 5 references
if refs:
    for index, ref in enumerate(refs.find_all("li"), start=1):  # Enumerate starting at 1
        if index > 5:  # Stop after printing 5 references
            break
        # Print each reference with its index, and remove any '^' symbols
        print(f"{index}. {ref.text.replace('^', '')}")



