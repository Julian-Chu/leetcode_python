from typing import List
from unittest import TestCase


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(numbers):
            if num in dict.keys():
                return [dict[num] + 1, i + 1]
            dict[target - num] = i


class TestSolution(TestCase):
    def test_twoSum(self):
        test_cases = [
            {
                "name": "[2,7,11,15]",
                "input": [2, 7, 11, 15],
                "target": 9,
                "expected": [1, 2]
            },
            {
                "name": "[0,0,3,4]",
                "input": [0, 0, 3, 4],
                "target": 0,
                "expected": [1, 2]
            }]

        solution = Solution();
        for ts in test_cases:
            self.assertEqual(solution.twoSum(ts["input"], ts['target']), ts["expected"])
