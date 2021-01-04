class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        h1 = h2 = -max(prices)
        s1 = s2 = 0

        for price in prices:
            s1 = max(s1, h1 + price)
            s2 = max(s2, h2 + price)
            h1 = max(h1, - price)
            h2 = max(h2, s1 - price)
        return s2


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        n = len(prices)
        k = 2
        dp = [[0] * n for _ in range(k + 1)]

        for i in range(1, k + 1):
            maxDiff = -float('inf')
            for j in range(1, n):
                maxDiff = max(maxDiff, dp[i - 1][j - 1] - prices[j - 1])
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxDiff)
        return dp[k][n - 1]


"""
timeout
"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        memo = {}
        return self.dfs(prices, 0, 0, 2, 2, memo)

    def dfs(self, prices, index, profit, buy_times, sell_times, memo):

        if buy_times == 0 and sell_times == 0:
            return profit

        if index == len(prices):
            return profit

        key = (index, buy_times, sell_times, profit)
        if key in memo:
            return memo[key]
        ans = -float('inf')
        if buy_times == sell_times and buy_times > 0:
            ans = max(ans, self.dfs(prices, index + 1, profit - prices[index], buy_times - 1, sell_times, memo))

        if sell_times > buy_times and sell_times > 0:
            ans = max(ans, self.dfs(prices, index + 1, profit + prices[index], buy_times, sell_times - 1, memo))
        ans = max(ans, self.dfs(prices, index + 1, profit, buy_times, sell_times, memo))
        memo[key] = ans
        return ans

"""
timeout
"""

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        n = len(prices)
        k = 2
        dp = [[0] * n for _ in range(k + 1)]

        for i in range(1, k + 1):
            for j in range(1, n):
                for m in range(j):
                    dp[i][j] = max(dp[i][j], dp[i][j - 1], dp[i - 1][m] + prices[j] - prices[m])
        return dp[k][n - 1]