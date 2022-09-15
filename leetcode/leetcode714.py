class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0
        min_price = prices[0]
        for price in prices[1:]:
            if min_price > price:
                min_price = price
                continue

            if min_price <= price <= min_price + fee:
                continue

            if price > min_price + fee:
                result += price - min_price - fee

                min_price = price - fee

        return result


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)

        return max(dp[-1])
