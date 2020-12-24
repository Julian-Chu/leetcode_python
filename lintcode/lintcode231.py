class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """

    def __init__(self, dict):
        typeahead = {}
        for word in dict:
            for i in range(len(word)):
                for j in range(i + 1, len(word) + 1):
                    key = word[i:j]
                    if key not in typeahead:
                        typeahead[key] = set()
                    typeahead[key].add(word)
        self.typeahead = typeahead

    """
    @param: str: a string
    @return: a list of words
    """

    def search(self, str):
        if str not in self.typeahead:
            return []

        return list(self.typeahead[str])


"""
array 去重 加速
"""
class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    def __init__(self, dict):
        # do initialize if necessary
        self.mp = {}
        for s in dict:
            l = len(s)
            for i in range(l):
                for j in range(i + 1, l + 1):
                    tmp = s[i:j]
                    if tmp not in self.mp:
                        self.mp[tmp] = [s]
                    elif self.mp[tmp][-1] != s:
                        self.mp[tmp].append(s)

    # @param word: a string
    # @return a list of words
    def search(self, word):
        # write your code here
        if word not in self.mp:
            return []
        else:
            return self.mp[word]