import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import json


load_dotenv()
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

# authenticating with spotify
spotify_auth = spotipy.Spotify(
    auth_manager = SpotifyClientCredentials(
        client_id = client_id,
        client_secret = client_secret
    )
)

def get_playlist_track(playlist_link):
    results = spotify_auth.playlist_tracks(playlist_link)
    tracks = results['items']
    while results['next']:
        results = spotify_auth.next(results)
        tracks.extend(results['items'])
    return tracks

def parse_tracks(tracks):
    song_list = []
    for item in tracks:
        track = item['track']
        song = {
            'title': track['name'],
            'artist': track['artists'][0]['name'],
            'spotify_song_link': track['external_urls']['spotify']
        }
        song_list.append(song)
    return song_list

def save_to_json(song_list, filename="songs.json"):
    with open(filename, 'w') as file:
        json.dump(song_list, file, indent=3)
        
        
if __name__ == '__main__':
    playlist_link = input("Enter Spotify Playlist link:\n")
    tracks = get_playlist_track(playlist_link)
    song_list = parse_tracks(tracks)
    save_to_json(song_list)
    print(f"Successfully saved all {len(song_list)} songs to file!")
