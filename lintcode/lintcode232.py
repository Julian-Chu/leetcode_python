
class TinyUrl:
    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def __init__(self):
        self.alnumtable = []
        for i in range(97 ,122):
            self.alnumtable.append(chr(i))
        for i in range(65 ,90):
            self.alnumtable.append(chr(i))
        for i in range(0 ,9):
            self.alnumtable.append(str(i))
        self.tableSize = len(self.alnumtable)
        self.long2short = {}
        self.short2long = {}

    def longToShort(self, url):
        if url in self.long2short:
            return self.long2short[url]

        shortUrl = self.generateRandomShortUrl()
        while shortUrl in self.short2long:
            shortUrl = self.generateRandomShortUrl()

        self.long2short[url] = shortUrl
        self.short2long[shortUrl] = url
        return shortUrl


    def generateRandomShortUrl(self):
        from random import randrange
        shortUrl = "http://tiny.url/"
        for i in range(6):
            key = randrange(self.tableSize)
            shortUrl += self.alnumtable[key]
        return shortUrl

    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, url):
        if url in self.short2long:
            return self.short2long[url]
        return ""
