# An object of the 'News' class store data about a single news page
# Instance variables of class:
#   *source - the URL address of the page [string]
#   *headline - the headline of the news page [string]
#   *date - the date the news has been published [string or date]
#   *time - the time the news has been published [string or time]

# TODO: determine the types of the variables 'date' and 'time'

class News():
    def __init__(self, source, headline, date, time):
        self.source = source
        self.headline = headline
        self.date = date
        self.time = time

    def getSource(self):
        return self.source

    def setSource(self, source):
        self.source = source

    def getHeadline(self):
        return self.headline

    def setHeadline(self, headline):
        self.headline = headline

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    def getTime(self):
        return self.time
    
    def setTime(self, time):
        self.time = time
