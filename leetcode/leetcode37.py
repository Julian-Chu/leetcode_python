class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = len(board)
        row_visited = [set() for _ in range(n)]
        col_visited = [set() for _ in range(n)]
        box_visited = [set() for _ in range(n)]

        for row in range(n):
            for col in range(n):
                num = board[row][col]
                row_visited[row].add(num)
                col_visited[col].add(num)
                box_visited[self.get_box_index(row, col)].add(num)

        self.dfs(board, 0, 0, row_visited, col_visited, box_visited)

    def dfs(self, board, row, col, row_visited, col_visited, box_visited):
        n = len(board)
        # print(row)
        if row == len(board):
            return True

        if board[row][col] != '.':
            if col == len(board) - 1:
                if self.dfs(board, row + 1, 0, row_visited, col_visited, box_visited):
                    return True
            else:
                if self.dfs(board, row, col + 1, row_visited, col_visited, box_visited):
                    return True
            return False

        for i in range(1, n + 1):
            num_str = str(i)
            box_index = self.get_box_index(row, col)
            if num_str in row_visited[row] or num_str in col_visited[col]:
                continue
            if num_str in box_visited[box_index]:
                continue
            row_visited[row].add(num_str)
            col_visited[col].add(num_str)
            box_visited[box_index].add(num_str)
            board[row][col] = num_str
            if col == len(board) - 1:
                if self.dfs(board, row + 1, 0, row_visited, col_visited, box_visited):
                    return True
            else:
                if self.dfs(board, row, col + 1, row_visited, col_visited, box_visited):
                    return True
            board[row][col] = '.'
            row_visited[row].remove(num_str)
            col_visited[col].remove(num_str)
            box_visited[box_index].remove(num_str)
        return False

    def get_box_index(self, row, col):
        return row // 3 * 3 + col // 3

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.dfs(board)


    def dfs(self, board: List):
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    continue

                for k in range(1, 10):
                    val = str(k)
                    if not self.isValid(board, i, j , val):
                        continue
                    board[i][j] = val
                    if self.dfs(board):
                        return True
                    board[i][j] = "."
                return False
        return True

    def isValid(self, board, row, col , val):
        for idx in range(9):
            if board[idx][col] == val:
                return False

            if board[row][idx] == val:
                return False

            row_start = row//3 * 3
            col_start = col//3 * 3

            for i in range(row_start, row_start+3):
                for j in range(col_start, col_start+3):
                    if board[i][j] == val:
                        return False
        return True