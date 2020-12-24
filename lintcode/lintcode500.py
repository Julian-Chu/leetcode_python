'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''


class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        word2id = {}
        for doc in docs:
            for word in doc.content.split():
                if word not in word2id:
                    word2id[word] = [doc.id]
                    continue
                if word2id[word][-1] == doc.id:
                    continue
                word2id[word].append(doc.id)
                # arr = word2id[word]
                # index = len(arr) - 1
                # while index >0:
                #     if arr[index-1] <= arr[index]:
                #         break
                #     arr[index-1], arr[index] = arr[index], arr[index-1]
                #     index-=1

        return word2id


