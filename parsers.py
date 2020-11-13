# This file contains parsing algorithms. Parser methods download HTML pages
# to isolate tags including source links, headlines, and date.

# Keywords:
#   * query - identical with user input on the search bar. It is treated
#     as the main keyword for search results.
#   * tag - and mark that points our an HTML element. E. g.: '<a>', '<title>', etc.
#   * tag -> string - represents plain text inside a tag. E. g.: '<a> Text </a>'.

import bs4 as bs # beautfiulSoup module to isolate HTML tags
from urllib.request import urlopen, Request

from News import News
from Site import Site

def querize(query):
    new_query = query

    new_query = new_query.strip() # to trim header and trailer whitespaces
    new_query = " ".join(new_query.split()) # to remove duplicate spaces in the middle
    new_query = new_query.replace(' ', '+') # replacing all spaces with '+' sign
                                    # as most search engines use '+' as
                                    # a separator instead of space.
    return new_query

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910'
HEADERS = {'User-Agent' : USER_AGENT}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Parsing algorithm for 'BBC Azerbaijan' news
def parseBBCAz(query):
    query = querize(query)

    request = Request('https://www.bbc.com/azeri/search?q=' + query, None, HEADERS)
    source = urlopen(request)
    file = bs.BeautifulSoup(source, 'lxml')

    # in search results BBC Azerbaijani uses <a class="hard-news-unit__headline-link"> tag for headline and links
    # and <div class="date date--v2"> for date.
    news_tags = file.find_all('a', class_='hard-news-unit__headline-link', href=True)
    date_tags = file.find_all('div', class_='date date--v2')

    site = Site('BBC Az') # to create a Site object to store the news results in a list form

    # to store source links, headlines, and dates in the Site object
    for i in range(len(news_tags)): 
        tag = news_tags[i]
        date = date_tags[i]
        site.results.append(News(tag['href'], tag.string, date.string, '00:00'))

    # to print for debugging
    for r in site.results:
        print(r.source + '|' + r.headline + '|' + r.date)

    return site

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     
# Parsing algorithm for 'Azadliq Radiosu' news
# TODO: edit date format
def parseAzadliq(query):
    query = querize(query)

    request = Request('https://www.azadliq.org/s?k=' + query, None, HEADERS)
    source = urlopen(request)
    file = bs.BeautifulSoup(source, 'lxml')

    source_tags = file.find_all('a', class_='img-wrap img-wrap--t-spac img-wrap--size-3 img-wrap--float img-wrap--xs', href=True)
    headline_tags = file.find_all('h4', class_='media-block__title media-block__title--size-3')
    date_tags = file.find_all('span', class_='date date--mb date--size-3')

    site = Site('Azadliq Radiosu')
    
    for i in range(len(source_tags)): 
        source = source_tags[i]
        headline = source['title']
        date = date_tags[i]
        site.results.append(News('https://www.azadliq.org' + source['href'], headline, date.string, '00:00'))

    for r in site.results:
        print(r.source + '|' + r.headline + '|' + r.date)

    return site

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
# Parsing algorithm for 'Meydan TV' news
# INCOMPLETE: Wrong HTML file is retrieved while searching
def parseMeydanTV(query):
    query = querize(query)

    request = Request('https://www.meydan.tv/az/search/?query=' + query, None, HEADERS)
    source = urlopen(request)
    file = bs.BeautifulSoup(source, 'lxml')
    
    print(file)
    li_tags = file.find_all('li')
    print(li_tags)
    news_tags = list()
    date_tags = list()

    for li in li_tags:
        divs = li.find_all('div')
        print(divs)
        print('----------------')
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Parsing algorithm for 'Report Az' news
def parseReportAz(query):
    query = querize(query)

    request = Request('https://www.report.az/search?query=' + query, None, HEADERS)
    source = urlopen(request)
    file = bs.BeautifulSoup(source, 'lxml')

    news_tags = file.find_all('a', class_='title', href=True)
    date_tags = file.find_all('div', class_='news-date')

    site = Site('Report.az')

    for i in range(len(news_tags)): 
        tag = news_tags[i]
        date = date_tags[i]
        site.results.append(News("https://report.az/" + tag['href'], tag.get_text().strip(), date.get_text().strip(), '00:00'))

    # to print for debugging
    for r in site.results:
        print(r.source + '|' + r.headline + '|' + r.date)

    return site
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Parsing algorithm for 'QafqazInfo' news
def parseQafqazInfo(query):
    query = querize(query)

    request = Request('https://qafqazinfo.az/news/search?keyword=' + query, None, HEADERS)
    source = urlopen(request)
    file = bs.BeautifulSoup(source, 'lxml')

    news_tags = file.find_all('a', class_='https://qafqazinfo.aznews/search', href=True)

    site = Site('QafqazInfo')

    for i in range(len(news_tags)): 
        tag = news_tags[i]
        site.results.append(News(tag['href'], tag.get_text().strip(), '00.00.0000', '00:00'))

    for r in site.results:
        print(r.source + '|' + r.headline + '|' + r.date)

    return site
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Parsing Algorithm for Lent.az
def parseLentAz(query):
    query = querize(query)

    request = Request('https://www.lent.az/axtar?q=' + query, None, HEADERS)
    source = urlopen(request)
    file = bs.BeautifulSoup(source, 'lxml')

    print(file)
    
    news_tags = file.find_all('a', class_='link-ln-news')
    date_tags = file.find_all('div', class_='pull-right')

    site = Site('Lent.az')

    print(date_tags[0].get_text())

    for i in range(len(news_tags)): 
        tag = news_tags[i]
        date = date_tags[i]
        site.results.append(News('https://www.lent.az' + tag['href'], tag.get_text().strip(), date.get_text().strip(), '00:00'))
        
    # to print for debugging
    for r in site.results:
       print(r.source + '|' + r.headline + '|' + r.date)

    return site
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Parsing Algorithm for Real TV
def parseRealTV(query):
    query = querize(query)
    
    request = Request('https://www.realtv.az/search/?text=' + query, None, HEADERS)
    source = urlopen(request)
    file = bs.BeautifulSoup(source, 'lxml')
    
    parent_tags = file.find_all('h4', class_='card-title gel-pica-bold')
    news_tags = list()

    site = Site("Real TV")
    
    for tag in parent_tags:
        news_tags.append(tag.find('a', href=True))
    
    for i in range(len(news_tags)): 
        tag = news_tags[i]
        site.results.append(News('https://www.lent.az' + tag['href'], tag.get_text().strip(), ' ', '00:00'))

    for r in site.results:
       print(r.source + '|' + r.headline + '|' + r.date)

    return site

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Parsing Algorithm for Eastnews.org
def parseEastNews(query):
    query = querize(query)
    
    request = Request('https://eastnews.org/search?query=' + query, None, HEADERS)
    source = urlopen(request)
    file = bs.BeautifulSoup(source, 'lxml')
    
    parent = file.find('div', class_='col-1')
    news_tags = parent.find_all('a', {'style' : 'color:#000'}, href=True)

    site = Site("Eastnews.org")

    for i in range(len(news_tags)): 
        tag = news_tags[i]
        site.results.append(News(tag['href'], tag.get_text().strip(), ' ', '00:00'))

    for r in site.results:
       print(r.source + '|' + r.headline + '|' + r.date)

    return site

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Parsing Algorithm for Apa.az
def parseApaAz(query):
    query = querize(query)

    request = Request('https://apa.az/az/search?q=' + query, None, HEADERS)
    source = urlopen(request)
    file = bs.BeautifulSoup(source, 'lxml')

    parent = file.find('div', class_='row block category')

    source_tags = parent.find_all('a', href=True)
    headline_tags = parent.find_all('p')
    date_tags = parent.find_all('span', class_='date')

    site = Site("Apa.az")

    for i in range(len(source_tags)): 
        source = source_tags[i]
        headline = headline_tags[i]
        date = date_tags[i]
        site.results.append(News('https://www.apa.az' + source['href'], headline.get_text(), date.get_text(), '00:00'))

    for r in site.results:
       print(r.source + '|' + r.headline + '|' + r.date)

    return site
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Parsing Algorithm for Musavat.az
def parseMusavatAz(query):
    query = querize(query)
    
    request = Request('https://musavat.com/search?text=' + query, None, HEADERS)
    source = urlopen(request)
    file = bs.BeautifulSoup(source, 'lxml')

    parent = file.find('div', class_= 'row block-news')

    source_tags = parent.find_all('a', class_= 'block', href=True)
    headline_tags = parent.find_all('strong')
    date_tags = parent.find_all('span', class_= 'pull-left')

    site = Site('Musavat.az')

    for i in range(len(source_tags)):
        source = source_tags[i]
        headline = headline_tags[i]
        date = date_tags[i]
        site.results.append(News('https://www.musavat.az' + source['href'], headline.get_text(), date.get_text(), '00:00'))

    for r in site.results:
       print(r.source + '|' + r.headline + '|' + r.date)

    return site

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Parsing Algorithm for 'Metbuat.az'
def parseMetbuatAz(query):
    query = querize(query)

    request = Request('https://metbuat.az/news/search?q=' + query, None, HEADERS)
    source = urlopen(request)
    file = bs.BeautifulSoup(source, 'lxml')

    parent = file.find('div', class_='col-sm-8 col-md-9 col-lg-9')

    source_tags = parent.find_all('a', class_ = 'news_box')
    headline_tags = parent.find_all('h4', class_ = 'news_box_ttl')
    date_tags = parent.find_all('span', class_ = 'news_box_date')

    site = Site('Musavat.az')

    for i in range(len(source_tags)):
        source = source_tags[i]
        headline = headline_tags[i]
        date = date_tags[i]
        site.results.append(News('https://metbuat.az' + source['href'], headline.get_text(), date.get_text(), '00:00'))

    for r in site.results:
       print(r.source + '|' + r.headline + '|' + r.date)

    return site
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

