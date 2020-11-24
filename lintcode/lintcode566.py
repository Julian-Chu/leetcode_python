'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''


class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """

    def __init__(self, chunkSize):
        self.chunkSize = chunkSize
        self.fileChunkCount = {}
        self.chunks = {}

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """

    def read(self, filename):
        if filename not in self.fileChunkCount:
            return None
        chunkCount = self.fileChunkCount[filename]
        contents = []
        for chunkIndex in range(chunkCount):
            contents.append(self.readChunk(filename, chunkIndex))
        return ''.join(contents)

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """

    def write(self, filename, content):
        count = 0

        chunkSize = self.chunkSize
        while content:
            count += 1
            writeToChunk = content[:chunkSize]
            content = content[chunkSize:]
            self.writeChunk(filename, count - 1, writeToChunk)

        self.fileChunkCount[filename] = count


