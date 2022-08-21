class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        paths = [[0] *n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break

            paths[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            paths[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                    continue

                paths[i][j] = paths[i-1][j] + paths[i][j-1]

        return paths[m-1][n-1]