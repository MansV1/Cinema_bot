import requests, json, os, sys
from urllib.parse import urljoin
from bs4 import BeautifulSoup
URL = "https://cfc.scenecinemas.com/home"
TOKEN = os.environ["TOKEN"]
CHAT
_
ID = os.environ["CHAT
_
ID"]
FILE = "seen.json"
html = requests.get(URL, timeout=20, headers={"User-Agent":
"Mozilla/5.0"}).text
soup = BeautifulSoup(html,
"html.parser")
movies = {}
for a in soup.select('a[href*="/movie-details/"]'):
name = a.get("title") or a.get
_
text(strip=True)
if name:
movies[a["href"]] = name
print("
"لقيت
, len(movies),
"فيلم")
