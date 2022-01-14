from unicodedata import name
import requests
from bs4 import BeautifulSoup
import numpy as np

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()

data = response.text

soup = BeautifulSoup(data, "html.parser")

# print(soup.prettify())

print(soup.title)

article_titles = []
article_links = []
article_upvotes = []

article_tags = soup.find_all(name="a", class_="titlelink")
for tag in article_tags:
    article_titles.append(tag.getText())
    article_links.append(tag.get("href"))


upvotes = soup.find_all(name="span", class_="score")
for upvote in upvotes:
    article_upvotes.append(int(upvote.getText().split()[0]))

# print(article_titles)
# print(article_links)
# print(article_upvotes)

max_upvotes_idx = np.array(article_upvotes).argmax()
largest_number = max(article_upvotes)
idx = article_upvotes.index(largest_number)
print(article_titles[idx], article_links[idx])