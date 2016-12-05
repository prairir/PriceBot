# an object for each individual item that it monitors


class Monitor(object):
    def __init__(self, author, url):
        self.prices = []
        self.author = author
        self.url = url

    #for testing
    def printMon(self):
        print(self.author)
        print(self.url)

    def getUrl(self):
        return self.url
