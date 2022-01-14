from unicodedata import name
from urllib import response
import requests
from bs4 import BeautifulSoup

date_input = input("YYYY-MM-DD: ")
year = date_input.split("-")[0]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_input}/")
response.raise_for_status()
data = response.text

# with open("spotify_billboard_100/cache.html", encoding="utf8") as file:
#     data = file.read()

soup = BeautifulSoup(data, "html.parser")

# with open("spotify_billboard_100/cache1.html", encoding="utf8", mode="w") as file:
#     file.write(soup.prettify())

songs = soup.select(selector="li.lrv-u-width-100p ul li h3#title-of-a-story:first-of-type")

song_list = []

for song in songs[:100]:
    song_list.append(song.getText().strip())

# print(song_list)
# print(len(song_list))

with open("spotify_billboard_100/song_list.txt", encoding="utf8", mode="w") as file:
    file.write("\n".join(song_list))

# print(song_list)