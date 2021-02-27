from typing import List
from unittest import TestCase


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums[:]
        for i in range(2,len(nums)):
            if i==2:
                dp[i] = dp[i - 2] + nums[i]
                continue
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]

        res = 0
        for v in dp:
            res = max(res, v)
        return res


class TestSolution(TestCase):
    def test_rob(self):
        test_cases = [
            {
                "name": "[1,2,3,1]",
                "nums": [1, 2, 3, 1],
                "expected": 4
            },
            {
                "name": "[2,7,9,3,1]",
                "nums": [2, 7, 9, 3, 1],
                "expected": 12
            },
            {
                "name": "[2,1]",
                "nums": [2, 1],
                "expected": 2
            },
        ]

        solution = Solution()
        for testcase in test_cases:
            self.assertEqual(testcase["expected"], solution.rob(testcase["nums"]),
                             testcase["name"])
