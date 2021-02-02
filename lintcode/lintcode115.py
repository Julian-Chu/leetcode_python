class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        return self.dfs(0, 0, obstacleGrid, {})

    def dfs(self, i, j, obstacleGrid, memo):
        key = (i, j)
        if key in memo:
            return memo[key]
        if obstacleGrid[i][j] == 1:
            memo[key] = 0
            return memo[key]

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if i == m - 1 and j == n - 1:
            return 1

        path = 0

        if i + 1 < m:
            path += self.dfs(i + 1, j, obstacleGrid, memo)
        if j + 1 < n:
            path += self.dfs(i, j + 1, obstacleGrid, memo)
        memo[key] = path
        return path


class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = 1

        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        encounterObstacle = False
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                encounterObstacle = True

            if not encounterObstacle:
                dp[i % 2][0] = 1
            else:
                dp[i % 2][0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i % 2][j] = 0
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j] + dp[i % 2][j - 1]

        return dp[(m - 1) % 2][n - 1]