class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def wordSquares(self, words):
        if not words:
            return []
        n = len(words[0])
        prefix_dict = {"": []}
        for word in words:
            prefix = ""
            prefix_dict[prefix].append(word)
            for c in word:
                prefix += c
                if prefix not in prefix_dict:
                    prefix_dict[prefix] = []
                prefix_dict[prefix].append(word)
        result = []
        self.dfs(words, n, [], result, prefix_dict)
        return result

    def dfs(self, words, length, combination, result, prefix_dict):
        if len(combination) == length:
            result.append(combination[:])
            return

        n = len(combination)
        prefix = ""
        for i in range(n):
            prefix += combination[i][n]
            if prefix not in prefix_dict:
                return
        for word in prefix_dict[prefix]:
            combination.append(word)
            self.dfs(words, length, combination, result, prefix_dict)
            combination.pop()


"""
timeout
"""
class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def wordSquares(self, words):
        if not words:
            return []
        n = len(words[0])

        result = []
        self.dfs(words, n, [], result)
        return result

    def dfs(self, words, length, combination, result):
        if len(combination) == length:
            result.append(combination[:])
            return

        n = len(combination)
        prefix = ""
        for i in range(n):
            prefix += combination[i][n]
        for word in words:
            if not word.startswith(prefix):
                continue

            combination.append(word)
            self.dfs(words, length, combination, result)
            combination.pop()

    def check_read_same(self, combination):
        mid = len(combination) - 1
        for i in range(mid):
            if combination[mid][i] != combination[i][mid]:
                return False
        return True