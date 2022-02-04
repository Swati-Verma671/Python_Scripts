import requests
from bs4 import BeautifulSoup
import csv

print("Welcome to page scrapper. This will scrape all external and internal links of the given website to you.\n")
url=input("please give the website url:")
req=requests.get(url)##requesting the provided url
soup=BeautifulSoup(req.content,'html5lib')

##scraping all the links of the website
links=[]
for row in soup.findAll('a'):
    link={}
    link['link']=row.get('href')
    links.append(link)

##storing the output
filename='links.csv'
with open(filename,'w',newline='') as f:
    w=csv.DictWriter(f,['S.No.','link'])
    w.writeheader()
    for link in links:
        w.writerow(link)

