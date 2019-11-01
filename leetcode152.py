from typing import List
from unittest import TestCase


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos, neg, max = 1, 1, nums[0]

        for i in range(0, len(nums)):
            if nums[i] > 0:
                pos, neg = nums[i] * pos, nums[i] * neg
            elif nums[i] < 0:
                pos, neg = nums[i] * neg, nums[i] * pos
            else:
                pos, neg = 0, 1

            if max<pos:
                max = pos

            if pos <=0:
                pos=1

        return max


class TestSolution(TestCase):
    def test_maxProduct(self):
        test_cases = [
            {
                "name": "[2,3,-2,4]",
                "input": [2, 3, -2, 4],
                "expected": 6
            },
            {
                "name": "[-2,0,-1]",
                "input": [-2, 0, -1],
                "expected": 0
            },
            {
                "name": "[3,-1,4]",
                "input": [3, -1, 4],
                "expected": 4
            }
        ]

        solution = Solution()
        for testcase in test_cases:
            assert solution.maxProduct(testcase["input"]) == testcase["expected"]
