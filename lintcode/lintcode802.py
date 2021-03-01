class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """

    def solveSudoku(self, board):
        self.dfs(board, 0)

    def dfs(self, board, index):
        if index == 81:
            return True

        i, j = index // 9, index % 9
        if board[i][j] != 0:
            return self.dfs(board, index + 1)

        for val in range(1, 10):
            if not self.isValid(board, i, j, val):
                continue
            board[i][j] = val
            if self.dfs(board, index + 1):
                return True
            board[i][j] = 0
        return False

    def isValid(self, board, row, col, val):
        if board[row][col] != 0:
            return False

        for i in range(9):
            if board[i][col] == val:
                return False
            if board[row][i] == val:
                return False
            r, c = row // 3 * 3 + i//3, col // 3 * 3 +i % 3
            if board[r][c] == val:
                return False
        return True

class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """

    def solveSudoku(self, board):
        used = self.initial_used(board)
        self.dfs(board, 0, used)

    def initial_used(self, board):
        used = {
            'row': [set() for _ in range(9)],
            'col': [set() for _ in range(9)],
            'box': [set() for _ in range(9)],
        }

        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    continue
                used['row'][i].add(board[i][j])
                used['col'][j].add(board[i][j])
                used['box'][i // 3 * 3 + j // 3].add(board[i][j])
        return used

    def is_valid(self, i, j, val, used):
        if val in used['row'][i]:
            return False
        if val in used['col'][j]:
            return False
        if val in used['box'][i // 3 * 3 + j // 3]:
            return False
        return True

    def dfs(self, board, index, used):
        if index == 81:
            return True

        i, j = index // 9, index % 9
        if board[i][j] != 0:
            return self.dfs(board, index + 1, used)

        for val in range(1, 10):
            if not self.is_valid(i, j, val, used):
                continue

            board[i][j] = val
            used['row'][i].add(val)
            used['col'][j].add(val)
            used['box'][i // 3 * 3 + j // 3].add(val)
            if self.dfs(board, index + 1, used):
                return True
            used['box'][i // 3 * 3 + j // 3].remove(val)
            used['col'][j].remove(val)
            used['row'][i].remove(val)
            board[i][j] = 0

        return False


class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """

    def solveSudoku(self, board):
        self.dfs(board)

    def dfs(self, board):
        i, j, choices = self.get_least_choices_grid(board)

        if i is None:
            return True

        for val in choices:
            board[i][j] = val
            if self.dfs(board):
                return True
            board[i][j] = 0

        return False

    def get_least_choices_grid(self, board):
        x, y, choices = None, None, [0] * 10

        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    continue
                vals = []
                for val in range(1, 10):
                    if self.is_valid(board, i, j, val):
                        vals.append(val)
                if len(vals) < len(choices):
                    x, y, choices = i, j, vals
        return x, y, choices

    def is_valid(self, board, x, y, val):
        for i in range(9):
            if board[x][i] == val:
                return False
            if board[i][y] == val:
                return False
            if board[x // 3 * 3 + i // 3][y // 3 * 3 + i % 3] == val:
                return False
        return True