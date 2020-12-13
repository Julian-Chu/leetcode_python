class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        self.mininum = sys.maxsize
        self.traverse(triangle, 0, 0, 0)
        return self.min_path

    def traverse(self, triangle, x, y, path_sum):
        if x == len(triangle):
            self.mininum = min(self.mininum,  path_sum)
            return

        self.traverse(triangle, x + 1, y, path_sum + triangle[x][y])
        self.traverse(triangle, x + 1, y + 1,  path_sum + triangle[x][y])


class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        res = self.divideconquer(triangle, 0, 0)
        return res

    def divideconquer(self, triangle, x, y):
        if x == len(triangle) - 1:
            return triangle[x][y]

        left = self.divideconquer(triangle, x + 1, y)
        right = self.divideconquer(triangle, x + 1, y + 1)

        return triangle[x][y] + min(left, right)


class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        res = self.divide_conquer(triangle, 0, 0, {})
        return res

    def divide_conquer(self, triangle, x, y, memo):
        if x == len(triangle) - 1:
            return triangle[x][y]

        if (x, y) in memo:
            return memo[(x, y)]

        left = self.divide_conquer(triangle, x + 1, y, memo)
        right = self.divide_conquer(triangle, x + 1, y + 1, memo)
        memo[(x, y)] = triangle[x][y] + min(left, right)
        return memo[(x, y)]


"""
dp
"""


class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]

        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

        return min(dp[n - 1])

"""
dp + rolling array
"""

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        n = len(triangle)
        dp = [[0] * n, [0] * n]

        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i % 2][0] = dp[(i - 1) % 2][0] + triangle[i][0]
            dp[i % 2][i] = dp[(i - 1) % 2][i - 1] + triangle[i][i]
            for j in range(1, i):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - 1]) + triangle[i][j]

        return min(dp[(n - 1) % 2])