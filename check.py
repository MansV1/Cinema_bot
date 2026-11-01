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
"
)"فيلم
Scene Cinemas بوت إشعارات أفﻼم
Page 2 of 5
if not movies:
مفيش أفﻼم اتقرأت"(sys.exit
)"
seen = set(json.load(open(FILE))) if os.path.exists(FILE) else None
if seen is not None:
for href in movies.keys() - seen:
requests.get(
f"https://api.telegram.org/bot{TOKEN}/sendMessage"
,
params={"chat
_
id": CHAT
_
ID,
"text": f"فيلم جديد نزل: {movies[href]}\n{urljoin(URL,
href)}"},
)
json.dump(sorted((seen or set()) | set(movies)), open(FILE,
"w"),
ensure
_
ascii=False)
