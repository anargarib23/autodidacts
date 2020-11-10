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

    
                         
        
    
