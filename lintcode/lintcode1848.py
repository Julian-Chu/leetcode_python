class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.isWord = True
        node.word = word


class Solution:
    DIRECT_X = [1, 0, 0, -1]
    DIRECT_Y = [0, 1, -1, 0]

    def wordSearchIII(self, board, words):
        trie = Trie()
        for word in words:
            trie.add(word)

        self.results = 0
        self.ans = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.search(trie.root, trie.root, board, r, c, r, c)
        return self.ans

    def search(self, root, trie, board, x, y, start_x, start_y):
        char = board[x][y]
        if char not in trie.children:
            return
        trie = trie.children[char]
        board[x][y] = '.'
        if trie.isWord:
            self.results += 1
            trie.isWord = False
            self.ans = max(self.ans, self.results)
            for i in range(start_x, len(board)):
                if i == start_x:
                    range_j = range(start_y + 1, len(board[0]))
                else:
                    range_j = range(len(board[0]))
                for j in range_j:
                    if board[i][j] != '.':
                        self.search(root, root, board, i, j, i, j)
            trie.isWord = True
            self.results -= 1

        for i in range(4):
            r = x + self.DIRECT_X[i]
            c = y + self.DIRECT_Y[i]
            if r < 0 or r == len(board) or c < 0 or c == len(board[0]):
                continue
            self.search(root, trie, board, r, c, start_x, start_y)
        board[x][y] = char


"""
TLE
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.isWord = True
        node.word = word


class Solution:
    DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: return the maximum nunber
    """

    def wordSearchIII(self, board, words):
        if not board or not words:
            return 0
        trie = Trie()
        for word in words:
            trie.add(word)
        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]
        self.Count = 0
        self.maxCount = 0
        for i in range(n):
            for j in range(m):
                visited[i][j] = True
                c = board[i][j]
                self.dfs(board, i, j, trie.root, trie.root.children.get(c), visited, i, j)
                visited[i][j] = False
        return self.maxCount

    def dfs(self, board, x, y, root, node, visited, start_x, start_y):
        if node is None:
            return
        if node.isWord:
            self.Count += 1
            self.maxCount = max(self.maxCount, self.Count)
            node.isWord = False


            # for i in range(len(board)):  # timeout
            for i in range(start_x, len(board)):
                if i == start_x:
                    range_j = range(start_y + 1, len(board[0]))
                else:
                    range_j = range(len(board[0]))
                for j in range_j:
                    if visited[i][j]:
                        continue
                    visited[i][j] = True
                    self.dfs(board, i, j, root, root.children.get(board[i][j]), visited, start_x, start_y)
                    visited[i][j] = False
            node.isWord = True
            self.Count -= 1

        for dx, dy in self.DIRECTION:
            next_x = x + dx
            next_y = y + dy
            if not self.isValid(board, next_x, next_y):
                continue
            if visited[next_x][next_y]:
                continue
            visited[next_x][next_y] = True
            self.dfs(board, next_x, next_y, root, node.children.get(board[next_x][next_y]), visited, start_x, start_y)
            visited[next_x][next_y] = False

    def isValid(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
