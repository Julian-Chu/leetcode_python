from typing import List
from unittest import TestCase


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(0, len(numbers)):
            if target - numbers[i] in d:
                return [d[target-numbers[i]], i+1]
            d[numbers[i]] = i+1
        return []




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
