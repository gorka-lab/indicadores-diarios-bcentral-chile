import requests
from bs4 import BeautifulSoup
from datetime import date
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

result = requests.get("http://www.bcentral.cl", verify=False)

if result.status_code != 200:
    print("No se pudo establecer comunicación con la web")
    quit()

src = result.content

soup = BeautifulSoup(src, 'lxml')

div = soup.find_all("div", {"class": "tab-pane active", "id": "tab-1"})

tds = []

for table in div:
    td_tag = table.find_all("td")
    for td in td_tag:
        tds.append(td.text)

hoy = date.today()
indicadores = {'Fecha': str(
    hoy), "UF": tds[2], "UTM": tds[4], "Dolar": tds[6], "Euro": tds[8], "TCM": tds[10]}

print(indicadores)
