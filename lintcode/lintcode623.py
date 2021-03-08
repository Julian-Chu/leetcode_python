"""
memo, but TLE
"""
class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """

    def kDistance(self, words, target, k):
        result = []
        memo = {}
        for word in words:
            step = self.dfs(word, target, memo)
            if step <= k:
                result.append(word)
        return result

    def dfs(self, word, target, memo):
        if word == target:
            return 0
        if not word:
            return len(target)
        if not target:
            return len(word)
        key = (word, target)
        if key in memo:
            return memo[key]

        if word[0] == target[0]:
            memo[key] = self.dfs(word[1:], target[1:], memo)
            return memo[key]

        res = min(
            self.dfs(word[1:], target, memo),
            self.dfs(word, target[1:], memo),
            self.dfs(word[1:], target[1:], memo)
        ) + 1

        memo[key] = res
        return res

"""
Trie
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        node.word = word


class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """

    def kDistance(self, words, target, k):
        trie = Trie()
        for word in words:
            trie.add_word(word)

        n = len(target)
        # dp = [0] * (n+1)
        dp = [i for i in range(n + 1)]
        result = []
        self.find(trie.root, target, k, dp, result)
        return result

    def find(self, node, target, k, dp, result):
        n = len(target)
        if node.is_word and dp[n] <= k:
            result.append(node.word)
            # no return here
        next = [0] * (n + 1)
        for c in node.children:
            next[0] = dp[0] + 1
            for i in range(1, n + 1):
                if target[i - 1] == c:  # same character , no replace
                    next[i] = min(dp[i - 1], dp[i] + 1, next[i - 1] + 1)
                else:  # replace or delete or insert
                    next[i] = min(dp[i - 1] + 1, dp[i] + 1, next[i - 1] + 1)
            self.find(node.children[c], target, k, next, result)