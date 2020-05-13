import sys
import requests
from bs4 import BeautifulSoup

def lyricScraper(song):
    urlt = song
    response = requests.get(urlt)
    soup = BeautifulSoup(response.text, 'html.parser')
    scrapedLyric = soup.find(class_='lyrics').get_text()
    scrapedLyric = scrapedLyric.replace('\n', '<br>')
    scrapedLyric = scrapedLyric[8:]
    return scrapedLyric
