import requests
from bs4 import BeautifulSoup

url = 'https://www.bcentral.cl'
site = requests.get(url)

if site.status_code != 200:
    print("Site is not available")
    quit()

soup = BeautifulSoup(site.content, 'html.parser')

data = soup.find_all('p', class_='mb-0 text-center')

items = []

for item in data:
    if item.span == None:
        items.append(item.string.strip())

indicadores = {'UF': items[0], 'UTM': items[1],
               'USD': items[2], 'EU': items[3]}

print(indicadores)
