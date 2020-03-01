import sys
import requests
from bs4 import BeautifulSoup

urlt = sys.argv[1]
response = requests.get(urlt)
soup = BeautifulSoup(response.text, 'html.parser')
scrapedLyric = soup.find(class_='lyrics').get_text()
scrapedLyric = scrapedLyric.replace('\n', '<br>')
scrapedLyric = scrapedLyric.replace("'", '@')
scrapedLyric = scrapedLyric.encode('ascii' , 'replace')
scrapedLyric = scrapedLyric[8:]
print(scrapedLyric)
