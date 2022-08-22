from typing import List
from unittest import TestCase

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)

        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[-1][1]

class Solution:
    def maxProfit(self, price: List[int]) -> int:
        maxProfit: int = 0
        for i in range(1, len(price)):
            if price[i - 1] < price[i]:
                maxProfit += price[i] - price[i - 1]

        return maxProfit


class TestSolution(TestCase):
    def test_maxProfit(self):
        test_cases = [
            {
                "name": "[7,1,5,3,6,4]",
                "input": [7, 1, 5, 3, 6, 4],
                "expected": 7
            },
            {
                "name": "[1,2,3,4,5]",
                "input": [1, 2, 3, 4, 5],
                "expected": 4
            }
        ]

        solution = Solution()
        for testcase in test_cases:
            assert solution.maxProfit(testcase["input"]) == testcase["expected"]
