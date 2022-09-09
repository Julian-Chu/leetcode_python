class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return 0

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(0, amount+1):
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[amount] if dp[amount] != float('inf') else -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return 0

        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(0, amount+1):
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[amount] if dp[amount] < amount+1 else -1