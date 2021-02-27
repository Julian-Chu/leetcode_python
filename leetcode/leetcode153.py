from typing import List
from unittest import TestCase


class Solution:
    def findMin(self, nums: List[int]) -> int:
        min:int = nums[0]
        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                min = nums[i]
        return min


class TestSolution(TestCase):
    def test_findMin(self):
        test_cases = [
            {
                "name": "[3,4,5,1,2]",
                "input": [3,4,5,1,2],
                "expected": 1
            },
            {
                "name": "[4,5,6,7,0,1,2]",
                "input": [4,5,6,7,0,1,2],
                "expected": 0
            },
            {
                "name": "[1]",
                "input": [1],
                "expected": 1
            }
        ]
        solution = Solution();
        for ts in test_cases:
            self.assertEqual(solution.findMin(ts["input"]), ts["expected"])
