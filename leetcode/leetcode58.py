from unittest import TestCase


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        found = False

        for i in reversed(s):
            if i == " ":
                if found:
                    break
                continue
            l += 1
            found = True
        return l


class TestSolution(TestCase):

    def test_lengthOfLastWord(self):
        test_cases = [
            {
                "name": "Hello World",
                "str": "Hello World",
                "expected": 5
            },
            {
                "name": "Hello World ",
                "str": "Hello World ",
                "expected": 5
            },
            {
                "name": "b   a    ",
                "str": "b    a    ",
                "expected": 1
            },
            {
                "name": "",
                "str": "",
                "expected": 0
            },
        ]

        solution = Solution()
        for testcase in test_cases:
            self.assertEqual(testcase["expected"], solution.lengthOfLastWord(testcase["str"]),
                             testcase["name"])
