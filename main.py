from flask import Flask, request, render_template
from flask_mongoalchemy import MongoAlchemy

import os

from parsers import *




app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '1'

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args['search']
    sites = loadSites(query)

    return render_template('search.html', sites=sites)
    
    

def loadSites(query):
    sites = list()
    sites.append(parseReportAz(query))
    #sites.append(parseQafqazInfo(query))
    #sites.append(parseLentAz(query))
    #sites.append(parseRealTV(query))
    #sites.append(parseEastNews(query))
    #sites.append(parseApaAz(query))
    #sites.append(parseMusavatAz(query))
    #sites.append(parseMetbuatAz(query))
    #sites.append(parseAxarAz(query))
    #sites.append(parseMilliAz(query))
    #sites.append(parseQaynarInfo(query))
    #sites.append(parsePublikaAz(query))
    #sites.append(parseAzVision(query))
    #sites.append(parseFemidaAz(query))
    #sites.append(parseAzToday(query))
    #sites.append(parseOrduAz(query))
    #sites.append(parseTeleqraf(query))

    return sites




        
