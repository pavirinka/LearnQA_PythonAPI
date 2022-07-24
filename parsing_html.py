import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_the_most_common_passwords"



resp = requests.get(url).text
soup = BeautifulSoup(resp,'lxml')
block = soup.find('div', id="mw-content-text")
table = block.find_all('table')[2].text
table_upd1=block.find_all('table')[2].text
table_upd1 =block.find_all('table',class_ ='wikitable')[2].text
print(table_upd1)
