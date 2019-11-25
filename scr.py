import sys
import requests
from bs4 import BeautifulSoup

urlt = sys.argv[1]
response = requests.get(urlt)
soup = BeautifulSoup(response.text, 'html.parser')
scrapedLyric = soup.find(class_='lyrics').get_text()
scrapePrint = scrapedLyric

scrapedLyric = scrapedLyric.replace('\n', '<br>')
scrapedLyric = scrapedLyric.encode('utf-8' , 'replace')
scrapedLyric = scrapedLyric[8:]
#print(scrapedLyric.decode('utf-8'))
print(scrapedLyric)
