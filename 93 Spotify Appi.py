import os
from flask import Flask, render_template, jsonify, request
import requests
from requests.auth import HTTPBasicAuth

#SPOTIFY CREDENTIALS
# clientId = 'Your Spotify Client ID'
# clientSecret = 'Your Spotify Secret'


# Set the path to the custom templates folder
template_dir = os.path.join(os.path.abspath('Support Files'), 'templates')

# Initialize the Flask app with the custom template folder
app = Flask(__name__, template_folder=template_dir)

# Serve the HTML page
@app.route('/')
def index():

    return render_template('93_Spotify_Api.html')


# Endpoint to get tracks from the Spotify API
@app.route('/get_tracks', methods=['GET'])
def get_tracks():
    # clientId = os.getenv("SPOT_CLIENT_ID")
    # clientSecret = os.getenv("SPOT_CLIENT_SECRET")

    # Get access token
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    auth = HTTPBasicAuth(clientId, clientSecret)
    response = requests.post(url, data=data, auth=auth)
    accessToken = response.json()["access_token"]

    # Search for the artist
    artist = request.args.get('artist').lower()
    artist = artist.replace(" ", "%20")
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {accessToken}"}
    search = f"?q=artist%3A{artist}&type=track&limit=5"
    fullURL = f"{url}{search}"

    # Get the track data
    response = requests.get(fullURL, headers=headers)
    data = response.json()

    # Extract track info
    tracks = [{"name": track["name"], "preview_url": track["preview_url"]} for track in data["tracks"]["items"]]
    return jsonify(tracks)  # Return the track data as JSON

if __name__ == "__main__":
    app.run(debug=True)
