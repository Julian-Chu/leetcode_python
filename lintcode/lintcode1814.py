"""
board[i][j] = "." behaves like visited, so visited is unnecessary
"""
class Trie:
    def __init__(self):
        self.children = {}
        self.hasWord = False

    def add(self, key):
        if key == '':
            self.hasWord = True
            return

        if key[0] not in self.children:
            self.children[key[0]] = Trie()
        self.children[key[0]].add(key[1:])


class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: return the maximum nunber
    """

    def wordSearchIII(self, board, words):
        trie = Trie()
        for word in words:
            trie.add(word)

        self.results = 0
        self.ans = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.search(trie, trie, board, r, c, r, c)
        return self.ans

    def search(self, root, trie, board, x, y, start_x, start_y):
        char = board[x][y]
        if char not in trie.children:
            return
        trie = trie.children[char]
        board[x][y] = '.'
        if trie.hasWord:  # found word, then start to search next word from point close to previous start
            self.results += 1
            trie.hasWord = False
            self.ans = max(self.ans, self.results)
            for i in range(start_x, len(board)):
                if i == start_x:
                    range_j = range(start_y + 1, len(board[0]))
                else:
                    range_j = range(len(board[0]))
                for j in range_j:
                    if board[i][j] != '.':
                        self.search(root, root, board, i, j, i, j)
            trie.hasWord = True
            self.results -= 1

        for dx, dy in self.DIRECTIONS:
            r = x + dx
            c = y + dy
            if r < 0 or r == len(board) or c < 0 or c == len(board[0]):
                continue
            self.search(root, trie, board, r, c, start_x, start_y)
        board[x][y] = char