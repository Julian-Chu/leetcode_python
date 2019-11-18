from unittest import TestCase


class Solution:
    def myPow(self, x: float, n: int) -> float:
        v = int(x**n*100000)/100000
        return v

class TestSolution(TestCase):
    def test_myPow(self):
        test_cases = [
            {
                "name": "2.0000**10",
                "x": 2.00000,
                "n": 10,
                "expected": 1024
            },
            {
                "name": "2.10000 **3",
                "x": 2.10000,
                "n": 3,
                "expected": 9.261000
            },
            {
                "name": "2 ** -2",
                "x": 2,
                "n": -2,
                "expected": 0.25
            }
        ]
        solution = Solution();
        for ts in test_cases:
            self.assertEqual(solution.myPow(ts["x"], ts["n"]), ts["expected"])
