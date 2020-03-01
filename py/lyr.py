import mysql.connector
import sys
import requests
import pytz
import configparser
from bs4 import BeautifulSoup
from csv import writer
from google.cloud import translate_v2 as translate
from datetime import datetime

config = configparser.ConfigParser()
config.read('/home/vladfranco2/sirencfg/config.ini')

mydb = mysql.connector.connect(
    host = config['data']['host'],
    user = config['data']['user'],
    passwd = config['data']['pass'],
    db = config['data']['db']
)

urlt = sys.argv[1]

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

    tranPrint = translate_recur(scrapedLyric, count)
    tranPrint = tranPrint.replace('\n', '<br>')
    tranPrint = tranPrint.replace("'", '@')
    tranPrint = tranPrint.encode('ascii' , 'replace')
    tranPrint = tranPrint[8:]
    print(tranPrint)
    tranPrint = tranPrint.decode('ascii')
    cursor = mydb.cursor()
    cursor.execute("insert into lyrics(songurl, songlyrics) values ('%s','%s')" % (urlt, tranPrint))
    mydb.commit()
    cursor.close()
else:
    cursor = mydb.cursor()
    cursor.execute("select songlyrics from lyrics where songurl = '%s'" % urlt)
    result = cursor.fetchall()
    for song in result:
        songlyrics = song[0]
        songlyrics = songlyrics.encode('ascii', 'replace')
        print(songlyrics)
