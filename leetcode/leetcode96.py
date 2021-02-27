from unittest import TestCase


class Solution:
    def numTrees(self, n: int) -> int:
        if n<2:
            return n
        if n==2:
            return 2

        arr = [0 for i in range(n+1)]
        arr[0], arr[1] = 1,1

        for i in range(2,n+1):
           for j in range(1,i+1):
            arr[i] += arr[j-1]*arr[i-j]

        return arr[-1]


class TestSolution(TestCase):
    def test_numTrees(self):
        test_cases = [
            {
                "name": "3",
                "input": 3,
                "expected": 5
            },
            {
                "name": "4",
                "input": 4,
                "expected": 14
            },
        ]

        solution = Solution()
        for ts in test_cases:
            self.assertEqual(ts["expected"], solution.numTrees(ts["input"]))
