from unittest import result
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from main import year, date_input

scope =  "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
        show_dialog=True,
        cache_path="spotify_billboard_100/token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

with open("spotify_billboard_100/song_list.txt", mode="r") as file:
    song_list = file.readlines()

song_list = [song.strip('\n') for song in song_list]

song_uris_list = []

for song_title in song_list[:100]:
    results = sp.search(q=f"track:{song_title} year:{year}", limit=1)
    results = results['tracks']['items']
    if len(results) > 0:
        song_uris_list.append(results[0]['uri'])

# print(song_uris_list)

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)
playlist_id = playlist_id['id']

sp.user_playlist_add_tracks(user=user_id,playlist_id=playlist_id, tracks=song_uris_list)
