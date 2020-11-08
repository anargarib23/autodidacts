# A 'Site' object is identified with a news website name and a list of found news

class Site:
    def __init__(self, name):
        self.name = name
        self.results = list()

    def setResults(self, foundResults): # to be used in parsing methods
        self.results = foundResults # 'foundResults' is a list of found news after parsing processes

    def getResults(self):
        return self.results
