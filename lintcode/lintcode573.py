class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """

    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1

        n, m = len(grid), len(grid[0])
        dist = [[float('inf') for _ in range(m)] for _ in range(n)]
        counts = [[0 for _ in range(m)] for _ in range(n)]
        nums = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, counts)
                    nums += 1

        min_dist = float('inf')
        for i in range(n):
            for j in range(m):
                if counts[i][j] == nums and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        return min_dist if min_dist != float('inf') else -1

    def bfs(self, grid, x, y, dist, counts):
        from collections import deque
        queue = deque([(x, y)])
        visited = set([(x, y)])
        level = 0

        while queue:
            n = len(queue)
            for _ in range(n):
                x, y = queue.popleft()
                if dist[x][y] == float('inf'):
                    dist[x][y] = 0
                dist[x][y] += level

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if not self.is_valid(grid, nx, ny):
                        continue
                    if (nx, ny) in visited:
                        continue

                    if grid[nx][ny] == 0:
                        counts[nx][ny] += 1
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            level += 1

    def is_valid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])