from typing import List
from unittest import TestCase


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
