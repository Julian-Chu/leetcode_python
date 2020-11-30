class StandardBloomFilter:
    """
    @param: k: An integer
    """

    def __init__(self, k):
        self.bitset = {}
        self.hashFunc = []
        for i in range(k):
            self.hashFunc.append(HashFunction(random.randint(10000, 20000), i * 2 + 3))

    """
    @param: word: A string
    @return: nothing
    """

    def add(self, word):
        for f in self.hashFunc:
            position = f.hash(word)
            self.bitset[position] = 1

    """
    @param: word: A string
    @return: True if contains word
    """

    def contains(self, word):
        for f in self.hashFunc:
            position = f.hash(word)
            if position not in self.bitset:
                return False

        return True


import random


class HashFunction:
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in value:
            ret += self.seed * ret + ord(i)
            ret %= self.cap

        return ret
