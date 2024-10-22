# Day 56 Challenge Requirements
# Objective:
# Organize a list of songs from a CSV file into artist-specific directories, creating a structured file system based on song and artist data.


# This script reads a CSV file of artists and their songs, creates directories for each artist,
# and stores the artist's songs in a text file inside their respective directory.

import os
import csv

# Function to print a list of unique artists
def printList():
    print()
    aux_list = []  # Temporary list to hold unique artists
    for artist in artists_list:
        if artist != "Artist":  # Skip header or invalid artist entry
            if artist not in aux_list:  # Add only unique artists
                print(artist)
                aux_list.append(artist)
    print()
    return aux_list  # Return list of unique artists

# Function to format and print a 2D list (optional feature, not used directly in the script)
def prettyPrint(list2D):
    print()
    for row in list2D:
        for item in row:
            print(f"{item:^10}", end=" | ")  # Print each item centered with a separator
            break  # Only print the first item (artist name)
        print()
    print()


base_directory = "Support Files"
artists_directory = os.path.join(base_directory, "artists_directory")

# Ensure the 'artists_directory' exists, create it if not
if not os.path.exists(artists_directory):
    os.makedirs(artists_directory)

# Open the CSV file containing artists and their songs
f = open("./Support Files/Songs_Artists.csv", "r")
artists_list = []  # List to store all artist names
artists_songs = []  # List to store rows of artist and song data
reader = csv.reader(f)  # CSV reader object

# Read each row in the CSV and store the artist and song data
for row in reader:
    artist, song = row[0], row[1]  # Extract artist and song
    artists_list.append(artist)  # Add artist to the list
    artists_songs.append(row)  # Add the row (artist, song) to the songs list

artists = printList()  # Call the function to print and get the unique artists

# Loop through each unique artist
for artist in artists:
    songs = []  # List to store songs of the current artist
    artist_dir = os.path.join(artists_directory, artist)  # Define path to artist's folder

    # Create a directory for the artist if it doesn't exist
    if not os.path.exists(artist_dir):
        os.mkdir(artist_dir)

    # Collect songs for the current artist
    for row in artists_songs:
        if row[0] == artist:  # Match artist name with the current artist
            songs.append(row[1])  # Add the song to the list

    print(songs)  # Print the list of songs for debugging

    # Write the artist's songs to a text file in their folder
    with open(f'{artist_dir}/{artist}_songs.txt', "a+") as f:
        f.write(str(songs))  # Save the song list as a string

f.close()  # Close the CSV file
