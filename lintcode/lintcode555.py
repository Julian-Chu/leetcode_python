class CountingBloomFilter:
    """
    @param: k: An integer
    """

    def __init__(self, k):
        self.bitset = {}
        self.hashFunc = []
        for i in range(k):
            self.hashFunc.append(HashFunction(i * 2 + 3, random.randint(10000, 20000)))

    """
    @param: word: A string
    @return: nothing
    """

    def add(self, word):
        for f in self.hashFunc:
            position = f.hash(word)
            if position not in self.bitset:
                self.bitset[position] = 0
            self.bitset[position] += 1

    """
    @param: word: A string
    @return: nothing
    """

    def remove(self, word):
        if self.contains(word):
            for f in self.hashFunc:
                position = f.hash(word)
                self.bitset[position] -= 1

    """
    @param: word: A string
    @return: True if contains word
    """

    def contains(self, word):
        for f in self.hashFunc:
            position = f.hash(word)
            if position not in self.bitset or self.bitset[position] == 0:
                return False
        return True


import random


class HashFunction:
    def __init__(self, seed, cap):
        self.seed = seed
        self.cap = cap

    def hash(self, word):
        ret = 0
        for i in word:
            ret = ret * self.seed + ord(i)
            ret %= self.cap

        return ret
