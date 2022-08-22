from typing import List
from unittest import TestCase

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def robRange(nums_original, start, end) -> int:
            nums = nums_original[start:end+1]
            n = len(nums)

            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])

            return dp[-1]


        return max(robRange(nums, 0, len(nums)-2), robRange(nums, 1, len(nums)-1))

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
