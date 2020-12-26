class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        results = []
        self.dfs(n, [], results)
        return results

    def dfs(self, n, cols, results):
        row = len(cols)
        if row == n:
            results.append(self.drawChessBoard(cols))
            return

        for col in range(n):
            if not self.isValid(cols, row, col):
                continue
            cols.append(col)
            self.dfs(n, cols, results)
            cols.pop()

    def isValid(self, cols, row, col):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if r - c == row - col or r + c == row + col:
                return False
        return True

    def drawChessBoard(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board