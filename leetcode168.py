from unittest import TestCase


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        a_num = ord('A')
        while n > 0:
            remainder = n % 26
            n = n // 26
            if remainder == 0:
                res = 'Z' + res
                n = n - 1
            else:
                res = chr(a_num + remainder - 1) + res

        return res


class TestSolution(TestCase):
    def test_convertToTitle(self):
        test_cases = [
            {
                "name": "1",
                "n": 1,
                "expected": "A"
            },
            {
                "name": "28",
                "n": 28,
                "expected": "AB"
            },
            {
                "name": "701",
                "n": 701,
                "expected": "ZY"
            },
            {
                "name": "52",
                "n": 52,
                "expected": "AZ"
            },
            {
                "name": "27",
                "n": 27,
                "expected": "AA"
            },
            {
                "name": "703",
                "n": 703,
                "expected": "AAA"
            },
            {
                "name": "1048",
                "n": 1048,
                "expected": "ANH"
            },
        ]

        solution = Solution()
        for testcase in test_cases:
            self.assertEqual(testcase["expected"], solution.convertToTitle(testcase["n"]),
                             testcase["name"])
