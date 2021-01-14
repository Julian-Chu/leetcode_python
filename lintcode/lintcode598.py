class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        if not grid:
            return 0

        DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(grid), len(grid[0])
        queue = collections.deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i, j))

        days = -1
        while queue:
            next_q = collections.deque()
            days += 1
            for i in range(len(queue)):
                zombie_x, zombie_y = queue.popleft()
                for dx, dy in DIRECTION:
                    x = zombie_x + dx
                    y = zombie_y + dy
                    if not self.is_valid(grid, x, y):
                        continue
                    grid[x][y] = 1
                    next_q.append((x, y))
            queue = next_q

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    return -1

        return days

    def is_valid(self, grid, x, y):
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y] == 2 or grid[x][y] == 1:
            return False
        return True
