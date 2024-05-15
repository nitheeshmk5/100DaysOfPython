from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()
KEY = os.getenv('KEY')
ID = os.getenv('CLIENT_ID')

#date = input('Enter a date to create a playlist (YYYY-MM-DD) : ')
date = '2005-07-05'
res = requests.get(url=f'https://www.billboard.com/charts/hot-100/{date}/')

content = res.text

soup = BeautifulSoup(content, 'html.parser')
song_names_list = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_list]

#print(song_names)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://en.wikipedia.org/wiki/HTTP_404",
        client_id=ID,
        client_secret=KEY,
        show_dialog=True,
        cache_path="token.txt",
        username='31losgrrl4jzhr56k7ljn4edndbe', 
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100 by python", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)