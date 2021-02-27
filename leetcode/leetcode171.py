from unittest import TestCase


class Solution:
    def titleToNumber(self, s: str) -> int:
        sum=0
        for v in s:
           sum*=26
           sum+= ord(v) - ord('A')+1
        return sum


class TestSolution(TestCase):
    def test_titleToNumber(self):
        test_cases = [
            {
                "name": "A",
                "n": "A",
                "expected": 1
            },
            {
                "name": "AB",
                "n": "AB",
                "expected": 28
            },
            {
                "name": "ZY",
                "n": "ZY",
                "expected": 701
            },
            {
                "name": "AAA",
                "n": "AAA",
                "expected": 703
            },
        ]

        solution = Solution()
        for testcase in test_cases:
            self.assertEqual(testcase["expected"], solution.titleToNumber(testcase["n"]),
                             testcase["name"])
