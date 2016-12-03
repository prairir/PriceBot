


class Monitor(object):
    def __init__(self, author, url):
        self.prices = []
        self.author = author
        self.url = url

    def printMon(self):
        print(self.author)
        print(self.url)

    def getUrl(self):
        return self.url
