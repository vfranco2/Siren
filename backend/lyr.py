import mysql.connector
import sys
import requests
import pytz
import configparser
from bs4 import BeautifulSoup
from csv import writer
from google.cloud import translate_v2 as translate
from datetime import datetime


def lyricTranslator(song):
    config = configparser.ConfigParser()
    config.read('/home/vladfranco2/sirencfg/config.ini')

    mydb = mysql.connector.connect(
        host = config['data']['host'],
        user = config['data']['user'],
        passwd = config['data']['pass'],
        db = config['data']['db']
    )

    urlt = song

    def translate_text(text, target, format_='text'):
        translate_client = translate.Client()
        result = translate_client.translate(text, target_language=target, format_='text')
        return result['translatedText']

    cursor = mydb.cursor()
    cursor.execute("select songurl from lyrics where songurl = '%s'" % (urlt))
    result = cursor.fetchall()

    if cursor.rowcount == 0:
        response = requests.get(urlt)
        soup = BeautifulSoup(response.text, 'html.parser')
        scrapedLyric = soup.find(class_='lyrics').get_text()
        languages = ['es', 'ja', 'lt', 'ml', 'zh-TW', 'en']
        count = 0
        def translate_recur(lyricText, counter):
            if counter < 5:
                newText = translate_text(lyricText, languages[counter])
                counter+=1
                return translate_recur(newText, counter)
            else:
                newText = translate_text(lyricText, languages[5])
                return newText

        translatedLyrics = translate_recur(scrapedLyric, count)
        translatedLyrics = translatedLyrics.replace('\n', '<br>')
        translatedLyrics = translatedLyrics.replace("'", '@')
        translatedLyrics = translatedLyrics[8:]
        cursor.execute("insert into lyrics(songurl, songlyrics) values ('%s','%s')" % (urlt, translatedLyrics))
        mydb.commit()
        cursor.close()
        mydb.close()
        translatedLyrics = translatedLyrics.replace('@', "'")
        return translatedLyrics
    else:
        cursor.execute("select songlyrics from lyrics where songurl = '%s'" % urlt)
        result = cursor.fetchall()
        cursor.close()
        mydb.close()
        for song in result:
            songLyrics = song[0]
            songLyrics = songLyrics.replace('@', "'")
            return songLyrics
