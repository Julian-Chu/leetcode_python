from typing import List
from unittest import TestCase


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
