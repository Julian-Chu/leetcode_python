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


"""
TLE
"""
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        comb = [['.'] * n for _ in range(n)]
        result = []
        self.dfs(n, 0, comb, result)
        return result

    def dfs(self, n, start, comb, result):
        if start == n:
            clone = [''.join(x[:]) for x in comb]
            result.append(clone)
            return

        for i in range(n):
            if self.canPlaced(comb, start, i):
                comb[start][i] = 'Q'
                self.dfs(n, start + 1, comb, result)
                comb[start][i] = '.'

    def canPlaced(self, comb, row, col):
        n = len(comb)
        nextpos = [(row, col), (row, col), (row, col)]
        offset = [(-1, 0), (-1, -1), (-1, 1)]
        for _ in range(row - 1, -1, -1):
            for i in range(3):
                x = nextpos[i][0] + offset[i][0]
                y = nextpos[i][1] + offset[i][1]
                nextpos[i] = (x, y)
                if not (0 <= x < n and 0 <= y < n):
                    continue
                if comb[x][y] == 'Q':
                    return False
        return True