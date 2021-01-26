"""
use Trie
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        node.word = word

    # def find(self, word):
    #     node = self.root
    #     for c in word:
    #         node = node.children.get(c)
    #         if node is None:
    #             return None
    #     return node


class Solution:
    DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        if not board or not words:
            return []

        trie = Trie()
        for word in words:
            trie.add(word)

        results = set()
        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                visited[i][j] = True
                c = board[i][j]
                self.dfs(board, i, j, trie.root.children.get(c), visited, results)
                visited[i][j] = False
        return list(results)

    def dfs(self, board, x, y, node, visited, results):
        if node is None:
            return
        if node.is_word:
            results.add(node.word)
        for dx, dy in self.DIRECTION:
            next_x = x + dx
            next_y = y + dy
            if not self.isValid(board, next_x, next_y):
                continue
            if visited[next_x][next_y]:
                continue
            visited[next_x][next_y] = True
            self.dfs(board, next_x, next_y, node.children.get(board[next_x][next_y]), visited, results)
            visited[next_x][next_y] = False

    def isValid(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])


"""
normal
"""
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def wordSearchII(self, board, words):
        prefix = set()
        for word in words:
            for i in range(len(word)):
                prefix.add(word[:i + 1])
        m = len(board)
        n = len(board[0])
        results = set()
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                self.dfs(board, words, prefix, visited, i, j, board[i][j], results)
                visited[i][j] = False
        return list(results)

    def dfs(self, board, words, prefix, visited, x, y, word, results):
        if word not in prefix:
            return

        if word in words:
            results.add(word)

        for dx, dy in self.directions:
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_x >= len(board) or new_y < 0 or new_y >= len(board[0]):
                continue

            if visited[new_x][new_y]:
                continue
            visited[new_x][new_y] = True
            self.dfs(board, words, prefix, visited, new_x, new_y,
                     word + board[new_x][new_y], results)
            visited[new_x][new_y] = False


"""
prefix
"""
DX = [0, 1, -1, 0]
DY = [1, 0, 0, -1]
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        if board is None or len(board) == 0:
            return []
        if board[0] is None or len(board[0]) == 0:
            return []

        visited = [[0] * len(board[0]) for _ in range(len(board))]
        prefix_is_word = self.get_prefix_set(words)
        result_set = set()

        for i in range(len(board)):
            for j in range(len(board[i])):
                visited[i][j] = True
                self.dfs(board, visited, i, j, board[i][j], prefix_is_word, result_set)
                visited[i][j] = False

        return list(result_set)

    def get_prefix_set(self, words):
        prefix_is_word = {}
        for word in words:
            prefix_is_word[word] = True
            for i in range(len(word)):
                prefix = word[:i + 1]
                if prefix not in prefix_is_word:
                    prefix_is_word[prefix] = False

        return prefix_is_word

    def inside(self, board, x, y):
        return x >= 0 and x < len(board) and y >= 0 and y < len(board[0])

    def dfs(self, board, visited, x, y, word, prefix_is_word, result_set):
        if word not in prefix_is_word:
            return

        if prefix_is_word[word]:
            result_set.add(word)

        for i in range(4):
            adjX = x + DX[i]
            adjY = y + DY[i]
            if not self.inside(board, adjX, adjY) or visited[adjX][adjY]:
                continue

            visited[adjX][adjY] = True
            self.dfs(board, visited, adjX, adjY, word + board[adjX][adjY], prefix_is_word, result_set)
            visited[adjX][adjY] = False
