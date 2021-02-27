class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """

    def totalNQueens(self, n):
        return self.dfs(n, [])

    def dfs(self, n, cols):
        row = len(cols)
        if row == n:
            return 1

        sum = 0
        for col in range(n):
            if not self.is_valid(cols, row, col):
                continue
            cols.append(col)
            sum += self.dfs(n, cols)
            cols.pop()

        return sum

    def is_valid(self, cols, row, col):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if r - c == row - col or r + c == row + col:
                return False
        return True