# This file contains parsing algorithms. Parser methods download HTML pages
# to isolate tags including source links, headlines, and date.

# Keywords:
#   * query - identical with user input on the search bar. It is treated
#     as the main keyword for search results.
#   * tag - and mark that points our an HTML element. E. g.: '<a>', '<title>', etc.
#   * tag -> string - represents plain text inside a tag. E. g.: '<a> Text </a>'.

import bs4 as bs # beautfiulSoup module to isolate HTML tags
from urllib.request import urlopen

from News import News
from Site import Site

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Parsing algorithm for 'BBC Azerbaijan' news
def parseBBCAz(query):
    query = query.strip() # to trim header and trailer whitespaces
    query = " ".join(query.split()) # to remove duplicate spaces in the middle
    query = query.replace(' ', '+') # replacing all spaces with '+' sign
                                    # as most search engines use '+' as
                                    # a separator instead of space.
    
    source = urlopen('https://www.bbc.com/azeri/search?q=' + query) # search URL
    file = bs.BeautifulSoup(source, 'lxml') # to store the HTML data in the variable

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
    query = query.strip()
    query = " ".join(query.split())
    query = query.replace(' ', '+')

    source = urlopen('https://www.azadliq.org/s?k=' + query + '&tab=all&pi=1&r=any&pp=50')
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
def parseMeydanTv(query):
    query = query.strip()
    query = " ".join(query.split())
    query = query.replace(' ', '+')

    source = urlopen('https://www.meydan.tv/az/search/?query=' + query)
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
# INCOMPLETE: 403 ERROR
def parseReportAz(query):
    query = query.strip()
    query = " ".join(query.split())
    query = query.replace(' ', '+')

    source = urlopen('https://www.report.az/search?query=' + query)
    file = bs.BeautifulSoup(source, 'lxml')

    news_tags = file.find_all('a', class_='title', href=True)
    date_tags = file.find_all('div', class_='news-date')

    site = Site('Report.az')

    for i in range(len(news_tags)): 
        tag = news_tags[i]
        date = date_tags[i]
        site.results.append(News("https://report.az/" + tag['href'], tag.string, date.string, '00:00'))

    # to print for debugging
    for r in site.results:
        print(r.source + '|' + r.headline + '|' + r.date)

    return site
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#https://qafqazinfo.aznews/search

# Parsing algorithm for 'QafqazInfo' news
# INCOMPLETE: 403 ERROR
def parseQafqazInfo(query):
    query = query.strip()
    query = " ".join(query.split())
    query = query.replace(' ', '+')

    source = urlopen('https://qafqazinfo.az/news/search?keyword=' + query)
    file = bs.BeautifulSoup(source, 'lxml')

    news_tags = file.find_all('a', class_='https://qafqazinfo.aznews/search', href=True)

    site = Site('QafqazInfo')

    for i in range(len(news_tags)): 
        tag = news_tags[i]
        site.results.append(News(tag['href'], tag.string, '00.00.0000', '00:00'))

    for r in site.results:
        print(r.source + '|' + r.headline + '|' + r.date)

    return site
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
