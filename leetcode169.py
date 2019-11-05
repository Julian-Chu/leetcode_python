from typing import List
from unittest import TestCase


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numSet = set(nums)

        for num in numSet:
            if nums.count(num) > len(nums)/2:
                return num


class TestSolution(TestCase):
    def test_majorityElement(self):
        test_cases = [
            {
                "name": "[3,2,3]",
                "input": [3, 2, 3],
                "expected": 3
            },
            {
                "name": "[2,2,1,1,1,2,2]",
                "input": [2, 2, 1, 1, 1, 2, 2],
                "expected": 2
            }]

        solution = Solution();
        for ts in test_cases:
            self.assertEqual(solution.majorityElement(ts["input"]), ts["expected"])
