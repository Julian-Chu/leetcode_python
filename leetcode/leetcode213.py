from typing import List
from unittest import TestCase


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp1 = nums[:n - 1]
        dp2 = nums[1:]

        maxVal = 0
        for i in range(n - 1):
            if i == 2:
                dp1[i] += dp1[i - 2]
                dp2[i] += dp2[i - 2]
            if i > 2:
                dp1[i] += max(dp1[i - 2], dp1[i - 3])
                dp2[i] += max(dp2[i - 2], dp2[i - 3])

            maxVal = max(maxVal, dp1[i])
            maxVal = max(maxVal, dp2[i])

        return maxVal


class TestSolution(TestCase):
    def test_rob(self):
        test_cases = [
            {
                "name": "[2,3,2]",
                "nums": [2, 3, 2],
                "expected": 3
            },
            {
                "name": "[1,2,3,1]",
                "nums": [1, 2, 3, 1],
                "expected": 4
            },
            {
                "name": "[1,0,2]",
                "nums": [1, 0, 2],
                "expected": 2
            },
            {
                "name": "[1,0]",
                "nums": [1, 0],
                "expected": 1
            },

            {
                "name": "[]",
                "nums": [],
                "expected": 0
            },

            {
                "name": "[1]",
                "nums": [1],
                "expected": 1
            },
        ]

        solution = Solution()
        for testcase in test_cases:
            self.assertEqual(testcase["expected"], solution.rob(testcase["nums"]),
                             testcase["name"])
