import sys
import requests
from bs4 import BeautifulSoup

def lyricScraper(song):
    urlt = song
    response = requests.get(urlt)
    soup = BeautifulSoup(response.text, 'html.parser')
    scrapedLyric = soup.find(class_='kkHBOZ')
    scrapedLyric = str(scrapedLyric)
    scrapedLyric = scrapedLyric.replace('<br/>', '\n')
    soup = BeautifulSoup(scrapedLyric, 'html.parser')
    scrapedLyric = soup.find(class_='kkHBOZ').get_text()
    scrapedLyric = scrapedLyric.replace('\n', '<br>')
    return scrapedLyric
