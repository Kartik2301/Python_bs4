from importlib.resources import contents
from statistics import mode
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

data = response.content

# with open("top_movies/cache.html", encoding="cp1252") as file:
#     data = file.read()

soup = BeautifulSoup(data, "html.parser")

tp_movies = soup.find_all(name="img")

top_movies_list = []

for movie in tp_movies:
    top_movies_list.append(movie.get("alt"))

top_movies_list = top_movies_list[1:len(top_movies_list)-3:2]
top_movies_list = top_movies_list[::-1]


with open("top_movies/top_movies.txt", mode="w", encoding="utf8") as file:
    file.write("\n".join(top_movies_list))