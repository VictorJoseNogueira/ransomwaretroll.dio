from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.google.com/search?client=opera-gx&q=temperatura&sourceid=opera&ie=UTF-8&oe=UTF-8').content

soup = BeautifulSoup(site, 'lxml')

temperatura = soup.xpath('//*[@id="wob_tm"]')

print(temperatura)