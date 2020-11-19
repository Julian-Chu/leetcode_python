class TinyUrl2:
    domainName = "http://tiny.url/"

    def __init__(self):
        self.alnumtable = []
        for i in range(97, 122):
            self.alnumtable.append(chr(i))
        for i in range(65, 90):
            self.alnumtable.append(chr(i))
        for i in range(0, 9):
            self.alnumtable.append(str(i))
        self.tableSize = len(self.alnumtable)
        self.long2short = {}
        self.short2long = {}

    """
    @param: long_url: a long url
    @param: key: a short key
    @return: a short url starts with http://tiny.url/
    """

    def createCustom(self, long_url, key):
        shortUrl = self.domainName + key
        if long_url in self.long2short and self.long2short[long_url] != shortUrl:
            return "error"
        if shortUrl in self.short2long and self.short2long[shortUrl] != long_url:
            return "error"

        if long_url in self.long2short:
            return self.long2short[long_url]

        self.long2short[long_url] = shortUrl
        self.short2long[shortUrl] = long_url
        return shortUrl


    """
    @param: long_url: a long url
    @return: a short url starts with http://tiny.url/
    """


    def longToShort(self, long_url):
        if long_url in self.long2short:
            return self.long2short[long_url]

        shortUrl = self.generateRandomShortUrl()
        while shortUrl in self.short2long:
            shortUrl = self.generateRandomShortUrl()

        self.long2short[long_url] = shortUrl
        self.short2long[shortUrl] = long_url
        return shortUrl


    def generateRandomShortUrl(self):
        from random import randrange
        shortUrl = "http://tiny.url/"
        for i in range(6):
            key = randrange(self.tableSize)
            shortUrl += self.alnumtable[key]
        return shortUrl


    """
    @param: short_url: a short url starts with http://tiny.url/
    @return: a long url
    """


    def shortToLong(self, short_url):
        if short_url in self.short2long:
            return self.short2long[short_url]
        return 'error'


class TinyUrl2:
    def __init__(self):
        self.l2s = {}
        self.s2l = {}
        self.cnt = 0
        self.tinyUrl = 'http://tiny.url/'
        self.charset = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'

    def newShortUrl(self):
        res = ''
        tmp = self.cnt
        for i in range(6):
            res += self.charset[tmp % 62]
            tmp //= 62
        self.cnt += 1
        return self.tinyUrl + res

    """
    @param: long_url: a long url
    @param: key: a short key
    @return: a short url starts with http://tiny.url/
    """

    def createCustom(self, long_url, key):
        short_url = self.tinyUrl + key
        if long_url in self.l2s:
            if self.l2s[long_url] == short_url:
                return short_url
            else:
                return 'error'
        if short_url in self.s2l:
            return 'error'
        self.l2s[long_url] = short_url
        self.s2l[short_url] = long_url
        return short_url

    """
    @param: long_url: a long url
    @return: a short url starts with http://tiny.url/
    """

    def longToShort(self, long_url):
        if long_url in self.l2s:
            return self.l2s[long_url]
        short_url = self.newShortUrl()
        self.l2s[long_url] = short_url
        self.s2l[short_url] = long_url
        return short_url

    """
    @param: short_url: a short url starts with http://tiny.url/
    @return: a long url
    """

    def shortToLong(self, short_url):
        if short_url in self.s2l:
            return self.s2l[short_url]
        else:
            return 'error'