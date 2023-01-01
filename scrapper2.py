import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Saudi_Arabia"

response = requests.get(url)
response = response.content
soup = BeautifulSoup(response,'html.parser')
print(soup)
paragraph = soup.find_all('p')[0:5]
print(paragraph)
div = soup.find_all('a')[0:4]
print(div)

Petroleum = soup.find_all(text="Petroleum")
print(Petroleum)
Wahhabi  = soup.find_all(text="Wahhabi")
print(Wahhabi)

MBS = soup.find_all(text="Mohammed bin Salman")
print(MBS)

Corruption = soup.find_all(text="corrupt")
print(Corruption)
