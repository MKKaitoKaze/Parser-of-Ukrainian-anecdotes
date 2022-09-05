import requests
from bs4 import BeautifulSoup

sites = requests.get("https://etnosvit.com/uk/anekdoty_uk.html").text
soup = BeautifulSoup(sites, 'lxml')

for i in soup.find_all("div", {"class": "sue-panel-content sue-content-wrap"}):
    print(i.text)
    print("____________")