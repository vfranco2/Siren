import flask
import mysql.connector
import configparser
import random
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from scr import lyricScraper
from lyr import lyricTranslator

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['DEBUG'] = True;

#------------------
#API Requests
#------------------
@app.route('/sirencall/original', methods=['GET'])
def api_original():
    if 'song' in request.args:
        querySong = str(request.args['song'])
    else:
        return "Error: No song provided."
    scrapedLyr = lyricScraper(querySong)
    jsonedLyr = [{'lyrics': scrapedLyr}]
    return jsonify(jsonedLyr)

@app.route('/sirencall/improved', methods=['GET'])
def api_improved():
    if 'song' in request.args:
        querySong = str(request.args['song'])
    else:
        return "Error: No song provided."
    translatedLyr = lyricTranslator(querySong)
    jsonedLyr = [{'lyrics': translatedLyr}]
    return jsonify(jsonedLyr)

app.run(host='0.0.0.0',port='5000')
