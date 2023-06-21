import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar?islemci=Amd%20Ryzen%209"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all('li',{'class':'column'},limit=1)

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get('href').text.strip()
    oldprice = li.find('div',{'class':'proDetail'}).find_all('a')[0].text.strip().strip('TL')
    newprice =  li.find('div',{'class':'proDetail'}).find_all('a')[1].text.strip().strip('TL')
    
    print(name,link,oldprice,newprice)