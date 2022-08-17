class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard = [['.'] * n for _ in range(n)]

        res = []

        def dfs(idx: int):
            if idx == n:
                tmp = []
                for i in range(len(chessboard)):
                    tmp.append(''.join(chessboard[i]))
                res.append(tmp)
                return

            for i in range(n):
                if not self.isAvailable(chessboard, idx, i):
                    continue

                chessboard[idx][i] = 'Q'
                dfs(idx + 1)
                chessboard[idx][i] = '.'

        dfs(0)

        return res

    def isAvailable(self, chessboard, x, y):
        n = len(chessboard)
        offsets = [(-1, -1), (-1, 1), (-1, 0)]
        for k in range(1, x + 1):
            for (x_offset, y_offset) in offsets:
                if x + x_offset * k < 0 or y + y_offset * k < 0 or y + y_offset * k >= n:
                    continue
                if chessboard[x + x_offset * k][y + y_offset * k] == 'Q':
                    return False

        return True

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs(n, [], res)
        return res

    def dfs(self, n, cols, res):
        if len(cols) == n:
            res.append(self.drawChessboard(cols))
            return

        row = len(cols)

        for col in range(n):
            if not self.isValid(cols, row, col):
                continue
            cols.append(col)
            self.dfs(n, cols, res)
            cols.pop()

    def isValid(self, cols, row, col):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if r-c == row-col or r+c == row+col:
                return False
        return True

    def drawChessboard(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            tmp = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(tmp))
        return board
