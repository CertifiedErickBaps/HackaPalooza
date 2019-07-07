import requests
from bs4 import BeautifulSoup

URL = "https://www.google.com/maps/place/Veracruz"

headers = {
    "User Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

page.requests.get(URL, headers=headers);

soup =  BeautifulSoup(page.content, 'html.parser') 

locatin = soup.find(class="section-embed-map-input")

print(locatin)