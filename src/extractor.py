# importing modules 
import urllib.request  
from bs4 import BeautifulSoup as bs
import lxml
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

#url = "https://oldschool.runescape.wiki/w/Chicken"
#url = "https://oldschool.runescape.wiki/w/Cow"
url = "https://oldschool.runescape.wiki/w/Chest_(Barrows)"


r = requests.get(url, headers=headers)# allow_redirects=True
   
values = []
soup = bs(r.content, "lxml")

heading_tags = ["h1", "h2", "h3"]
for tags in soup.find_all("tbody"):

    if(tags.text[2:6] == "Item"):
        print(tags, "\n\n")
   
print("\n\n\n\n\n\n\n")

for i in soup.find_all('tr', style="text-align:center"):
    print(i, "\n")
print(len(soup.find_all('tr', style="text-align:center")))