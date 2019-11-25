
import sys
import requests
from bs4 import BeautifulSoup
from csv import writer
from google.cloud import translate_v2 as translate

urlt = sys.argv[1]
response = requests.get(urlt)
soup = BeautifulSoup(response.text, 'html.parser')
scrapedLyric = soup.find(class_='lyrics').get_text()

def translate_text(text, target='es', format_='text'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target, format_='text')
    return result['translatedText']
tran1 = translate_text(scrapedLyric)

def translate_text2(text, target='ja', format_='text'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target, format_='text')
    return result['translatedText']
tran2 = translate_text2(tran1)

def translate_text3(text, target='lt', format_='text'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target, format_='text')
    return result['translatedText']
tran3 = translate_text3(tran2)

def translate_text4(text, target='ml', format_='text'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target, format_='text')
    return result['translatedText']
tran4 = translate_text4(tran3)

def translate_text5(text, target='zh-TW', format_='text'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target, format_='text')
    return result['translatedText']
tran5 = translate_text5(tran4)

def translate_text6(text, target='en', format_='text'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target, format_='text')
    return result['translatedText']
tran6 = translate_text6(tran5)

tranPrint = tran6
tranPrint = tranPrint.replace('\n', '<br>')
tranPrint = tranPrint.encode('utf-8' , 'replace')
tranPrint = tranPrint[8:]
#print(tranPrint.decode('utf-8'))
print(tranPrint)
