import requests, json, os
import openai
#NEWS CREDENTIALS
newsKey = 'newskeys'
country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"
#OPEN AI CREDENTIALS
open_AI_key='Your Open AI key'
organization_ID = 'Your Open AI organization ID'


# Set your organization and API key
openai.organization = organization_ID
openai.api_key = open_AI_key

# Send a GET request to retrieve news articles in JSON format
result = requests.get(url)
data = result.json()

counter = 0

# Loop through articles and summarize the first 5
for article in data["articles"]:
    counter += 1
    if counter > 5:  # Limit to 5 articles
        break

    # Create a prompt to summarize the article's URL in one sentence
    prompt = (f"""Summarise {article["url"]} in one sentence.""")

    # Request a summary from OpenAI's ChatCompletion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model to use
        messages=[{"role": "user", "content": prompt}],
        temperature=0,  # Set to 0 for deterministic responses
        max_tokens=20  # Limit the response length
    )

    # Print the summarized sentence
    print(response["choices"][0]["message"]["content"].strip())




