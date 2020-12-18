from flask import Flask, request, render_template, redirect, jsonify
from flask_mongoalchemy import MongoAlchemy

import os, json

from parsers import *




app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/intermediate', methods=['GET', 'POST'])
def intermediate():
    query = request.form['keyword']
    return redirect('/search?query=' + query)

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args['query']
    sites = loadSites(query)
    
    data_dict = createSiteDict(sites)

    return render_template('search.html', sites=sites, news_list=data_dict)
    
    

def loadSites(query):
    sites = list()
    sites.append(parseReportAz(query))
    #sites.append(parseQafqazInfo(query))
    #sites.append(parseLentAz(query))
    #sites.append(parseRealTV(query))
    #sites.append(parseEastNews(query))
    sites.append(parseApaAz(query))
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


def newsToDict(news):
    newsDict = {'source' :  str(news.getSource()),
        'headline' : str(news.getHeadline()),
        'date' : str(news.getDate())}
        
    return newsDict

def createNewsList(site):
    news_list = []
    
    for news in site.getResults():
        news_list.append(newsToDict(news))
        
    return news_list
    
    
def createSiteDict(sites):
    siteDict = {}
    
    for site in sites:
        siteDict.update({ site.getName() : str(createNewsList(site))})
        
    return siteDict

        
