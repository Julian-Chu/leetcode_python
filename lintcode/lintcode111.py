class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        if n <= 2:
            return n
        a, b = 1, 2

        for _ in range(2, n):
            a, b = b, a + b

        return b
