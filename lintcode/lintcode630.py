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