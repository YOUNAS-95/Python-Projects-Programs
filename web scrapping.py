import requests
from bs4 import BeautifulSoup
url="https://www.fiverr.com/"
y=requests.get(url)
Soup = BeautifulSoup(y.text,"lxml")
print(Soup)
# print(y.text)