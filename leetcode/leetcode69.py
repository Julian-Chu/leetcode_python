from unittest import TestCase


class Solution:
    def mySqrt(self, x: int) -> int:
        res = x
        while res*res > x:
            res = (res+ x/res)/2
        return int(res)


class TestSolution(TestCase):
    def test_mySqrt(self):
        test_cases = [
            {
                "name": "4",
                "x": 4,
                "expected": 2
            },
            {
                "name": "8",
                "x": 8,
                "expected": 2
            },
        ]
        solution = Solution();
        for ts in test_cases:
            self.assertEqual(solution.mySqrt(ts["x"]), ts["expected"], ts["name"])
