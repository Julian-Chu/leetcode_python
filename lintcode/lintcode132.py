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
