from unittest import TestCase


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n = len(needle)

        for i in range(len(haystack) - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1


class TestSolution(TestCase):
    def test_strStr(self):
        test_cases = [
            {
                "name": "hello ll",
                "haystack": "hello",
                "needle": "ll",
                "expected": 2
            },
            {
                "name": "aaaa bba",
                "haystack": "aaaaa",
                "needle": "bba",
                "expected": -1
            },
            {
                "name": "aaaaa ",
                "haystack": "aaaaa",
                "needle": "",
                "expected": 0
            },
            {
                "name": "aaaaaa a",
                "haystack": "aaaaaa",
                "needle": "a",
                "expected": 0
            },
        ]

        solution = Solution()
        for testcase in test_cases:
            self.assertEqual(testcase["expected"], solution.strStr(testcase["haystack"], testcase["needle"]),
                             testcase["name"])
