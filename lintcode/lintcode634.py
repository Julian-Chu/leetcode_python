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
            prefix += combination[i][n]  # ["wall","area"] => 下一個word的prefix是"le"
            if prefix not in prefix_dict:
                return
        for word in prefix_dict[prefix]:
            combination.append(word)
            self.dfs(words, length, combination, result, prefix_dict)
            combination.pop()


# Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_list = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.word_list.append(word)
        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node

    def get_words_with_prefix(self, prefix):
        node = self.find(prefix)
        return [] if node is None else node.word_list

    def contain(self, word):
        node = self.find(word)
        return node is not None and node.is_word


class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def wordSquares(self, words):
        trie = Trie()
        for word in words:
            trie.add(word)

        squares = []
        for word in words:
            self.search(trie, [word], squares)
        return squares

    def search(self, trie, square, squares):
        n = len(square[0])
        curt_index = len(square)
        if curt_index == n:
            squares.append(list(square))
            return

            # prunning
        for row_index in range(curt_index, n):
            prefix = ''.join([square[i][row_index] for i in range(curt_index)])
            if trie.find(prefix) is None:
                return

        prefix = ''.join([square[i][curt_index] for i in range(curt_index)])
        for word in trie.get_words_with_prefix(prefix):
            square.append(word)
            self.search(trie, square, squares)
            square.pop()


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