import requests

link = "https://www.w3schools.com/"

url = requests.get(link)

print(url.content)
