class Codec:
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

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.long2short:
            return self.long2short[longUrl]

        shortUrl = self.generateRandomShortUrl()
        while shortUrl in self.short2long:
            shortUrl = self.generateRandomShortUrl()

        self.long2short[longUrl] = shortUrl
        self.short2long[shortUrl] = longUrl
        return shortUrl

    def generateRandomShortUrl(self):
        from random import randrange
        shortUrl = "http://tiny.url/"
        for i in range(6):
            key = randrange(self.tableSize)
            shortUrl += self.alnumtable[key]
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.short2long:
            return self.short2long[shortUrl]
        return ""

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))