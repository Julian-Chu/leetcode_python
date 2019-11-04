from typing import List
from unittest import TestCase


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x, cnt = 0, 0
        for _, v in enumerate(nums):
            if x == v:
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                x = v

        return x


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
