# importing modules 
import urllib.request  
from bs4 import BeautifulSoup as bs
import lxml
import requests
import re


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

#url = "https://oldschool.runescape.wiki/w/Chicken"
#url = "https://oldschool.runescape.wiki/w/Cow"
url = "https://oldschool.runescape.wiki/w/Chest_(Barrows)"


r = requests.get(url, headers=headers)# allow_redirects=True
   

soup = bs(r.content, "lxml")



for i in soup.find_all('tr', style="text-align:center"):
   
    name = i.find("td", class_="item-col").text
    chance = i.find("td", class_=re.compile(r"^table-(?!n).*")).text
    print(name, chance, "\n")

    
   


    
