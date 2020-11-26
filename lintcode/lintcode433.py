class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        if not grid:
            return 0

        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for _ in range(n)]
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                if visited[i][j]:
                    continue

                islands += 1

                queue = [(i, j)]
                visited[i][j] = True

                while len(queue) > 0:
                    for _ in range(len(queue)):
                        island_i, island_j = queue.pop()

                        for offset_i, offset_j in offsets:
                            adjacent_i = island_i + offset_i
                            adjacent_j = island_j + offset_j
                            if adjacent_i < 0 or adjacent_i > n - 1:
                                continue

                            if adjacent_j < 0 or adjacent_j > m - 1:
                                continue

                            if visited[adjacent_i][adjacent_j] or grid[adjacent_i][adjacent_j] == 0:
                                continue

                            visited[adjacent_i][adjacent_j] = True
                            queue.append((adjacent_i, adjacent_j))

        return islands
