class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here

        # state
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

"""
rolling array
"""
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = 1

        for j in range(1, n):
            dp[0][j] = 1

        for i in range(1, m):
            dp[i % 2][0] = 1
            for j in range(1, n):
                dp[i % 2][j] = dp[(i - 1) % 2][j] + dp[i % 2][j - 1]

        return dp[(m - 1) % 2][n - 1]

"""
memoization
"""


class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        return self.dfs(0, 0, m, n, {})

    def dfs(self, i, j, m, n, memo):
        key = (i, j)
        if key in memo:
            return memo[key]

        if i == m - 1 and j == n - 1:
            return 1

        path = 0

        if i + 1 < m:
            path += self.dfs(i + 1, j, m, n, memo)
        if j + 1 < n:
            path += self.dfs(i, j + 1, m, n, memo)

        memo[key] = path
        return path
