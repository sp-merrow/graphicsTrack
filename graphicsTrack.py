from bs4 import BeautifulSoup as bs
import requests
rows = []

page = requests.get('https://www.nowinstock.net/computers/videocards/nvidia/rtx3060/')
parsed = bs(page.text, 'html.parser')
trackTable = parsed.find(id='trackerContent')

stock = trackTable.find_all(class_='stockStatus')
sites = trackTable.find_all('a')
del sites[len(sites)-1]

for site, stock in zip(sites, stock):
    if stock.text=='Out of Stock':
        continue

    cardInfo = site.text.split(': ')
    siteName = cardInfo[1][:-1]
    cardName = cardInfo[0]
    
    print(f'The {cardName} is in stock at {siteName}!')
