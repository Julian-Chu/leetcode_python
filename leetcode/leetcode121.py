from typing import List
from unittest import TestCase
# greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        low = prices[0]
        result = 0
        for price in prices:
            low = min(low, price)
            result = max(result, price - low)

        return result

# dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])

        return dp[-1][1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max: int = 0
        temp:int =0
        for i in range(1, len(prices)):
            temp += prices[i] - prices[i - 1]
            if temp < 0:
                temp = 0
            if max < temp:
                max = temp
        return max


class TestSolution(TestCase):
    def test_maxProfit(self):
        test_cases = [
            {
                "name": "[7,1,5,3,6,4]",
                "input": [7, 1, 5, 3, 6, 4],
                "expected": 5
            }

        ]
        for test_case in test_cases:
            solution = Solution()
            assert solution.maxProfit(test_case["input"]) == test_case["expected"]
