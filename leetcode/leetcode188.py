class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [[0] * (2*k+1) for _ in range(len(prices))]

        for j in range(1, 2*k+1, 2):
            dp[0][j] = -prices[0]


        for i in range(1,len(prices)):
            for j in range(1, 2*k+1, 2):
                dp[i][j] = max(dp[i-1][j-1] - prices[i], dp[i-1][j])
                dp[i][j+1] = max(dp[i-1][j] + prices[i], dp[i-1][j+1])

        return dp[-1][2*k]