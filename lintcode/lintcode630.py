class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        if not grid or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        m = len(grid[0])

        steps = [[1, 2], [-1, 2], [2, 1], [-2, 1]]
        import collections
        queue = collections.deque([[0, 0]])
        route_len = 0

        while queue:
            route_len += 1
            size = len(queue)
            for _ in range(size):
                start_point = queue.popleft()

                for step in steps:
                    next_row = start_point[0] + step[0]
                    next_col = start_point[1] + step[1]
                    if next_row == n - 1 and next_col == m - 1:
                        return route_len

                    if n > next_row >= 0 and m > next_col >= 0 and grid[next_row][next_col] != 1:
                        grid[next_row][next_col] = 1
                        queue.append([next_row, next_col])
        return -1


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        direction = [(1, 2), (-1, 2), (2, 1), (-2, 1)]

        m = len(grid)
        n = len(grid[0])

        dp = [[float('inf')] * n for _ in range(m)]

        dp[0][0] = 0

        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    continue
                for dx, dy in direction:
                    if 0 <= i - dx < m and 0 <= j - dy < n:
                        dp[i][j] = min(dp[i][j], dp[i - dx][j - dy] + 1)

        print(dp)
        if dp[m - 1][n - 1] == float('inf'):
            return -1
        return dp[m - 1][n - 1]


