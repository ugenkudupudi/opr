import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/global/in-en/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&N=-1&isNodeId=1'
filename = "details.csv"
f= open(filename,"w")
headers= "brand, product_name, shipping\n"
f.write(headers)

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"item-container"})

#container = containers[0]

for container in containers:	
	print(container.div.div.a["href"])
	print("------------------------------------------------------------")
	f.write(container.div.div.a["href"]+ "\n")
	
f.close();
