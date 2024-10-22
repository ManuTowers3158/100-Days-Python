import requests, json, os
import openai
import urllib.parse
from requests.auth import HTTPBasicAuth
#NEWS CREDENTIALS
newsKey = 'newskeys'
country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"
#OPEN AI CREDENTIALS
open_AI_key='Your Open AI key'
organization_ID = 'Your Open AI organization ID'
#SPOTIFY CREDENTIALS
clientId = 'Your Spotify Client ID'
clientSecret = 'Your Spotify Secret'


# Set your OpenAI organization and API key
openai.organization = organization_ID  # Replace with your actual organization ID
openai.api_key = open_AI_key

# Send a GET request to retrieve news articles in JSON format
result = requests.get(url)
data = result.json()

responses = []
songs = []
counter = 0

# Loop through articles and summarize the first 5
for article in data["articles"]:
    counter += 1
    if counter > 5:
        break

    # Create a prompt to summarize the article's URL in 4 words
    prompt = (f"""Summarise {article["url"]} in no more than 4 words.""")

    # Request a summary from OpenAI's ChatCompletion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model to use
        messages=[{"role": "user", "content": prompt}],
        temperature=0,  # Set to 0 for deterministic response
        max_tokens=20  # Limit the number of tokens in the response
    )

    # Extract and store the summary
    completion_text = response["choices"][0]["message"]["content"].strip()
    print(completion_text)
    responses.append(completion_text)

# Request an access token from Spotify API using client credentials
url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(clientId, clientSecret)
response = requests.post(url, data=data, auth=auth)
accessToken = response.json()["access_token"]

# Search Spotify for songs based on the summarized headlines
headers = {
    "Authorization": f"Bearer {accessToken}"
}

# Loop through the responses (summarized headlines)
for headline in responses:
    # Encode the headline for use in a URL
    encoded_headline = urllib.parse.quote(headline)

    # Construct the Spotify search URL
    url = "https://api.spotify.com/v1/search"
    search = f"?q={encoded_headline}&type=track"
    fullURL = f"{url}{search}"

    # Send a GET request to the Spotify API with the search query
    search_response = requests.get(fullURL, headers=headers)
    data = search_response.json()

    # Try to append the first song result, or add a placeholder if no result is found
    try:
        songs.append(data["tracks"]["items"][0])
    except (KeyError, IndexError):  # Handle cases where no tracks are found
        songs.append({"name": None, "preview_url": None})

# Display the top 5 songs found along with their corresponding headlines
for i in range(5):
    if songs[i]["name"] is not None:
        print(responses[i])  # Print the summarized headline
        print(songs[i]["name"])  # Print the name of the song
        print(songs[i]["preview_url"])  # Print a preview URL of the song
        print()
