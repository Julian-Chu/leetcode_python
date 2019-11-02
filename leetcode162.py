from typing import List
from unittest import TestCase


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return i-1

        return len(nums) - 1


class TestSolution(TestCase):
    def test_findPeakElement(self):
        test_cases = [
            {
                "name": "[1,2,3,1]",
                "input": [1, 2, 3, 1],
                "expected": [2]
            },
            {
                "name": "[1,2,1,3,5,6,4]",
                "input": [1, 2, 1, 3, 5, 6, 4],
                "expected": [1, 5]
            },
            {
                "name": "[1,2]",
                "input": [1, 2],
                "expected": [1]
            },
            {
                "name": "[2,1]",
                "input": [2, 1],
                "expected": [0]
            },
            {
                "name": "[1,3,2,1]",
                "input": [1, 3, 2, 1],
                "expected": [1]
            },
        ]
        solution = Solution()
        for ts in test_cases:
            v = solution.findPeakElement(ts["input"])
            self.assertTrue(any(e == v for e in ts["expected"]))
