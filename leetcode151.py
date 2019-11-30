from unittest import TestCase


class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split(" ")
        res = []
        for str in reversed(strs):
            if str == '':
                continue
            res.append(str)
        return " ".join(res)


class TestSolution(TestCase):
    def test_reverseWords(self):
        test_cases = [
            {
                "name": "the sky is blue",
                "str": "the sky is blue",
                "expected": "blue is sky the"
            },
            {
                "name": "   hello world!  ",
                "str": "   hello world!  ",
                "expected": "world! hello"
            },
            {
                "name": "a good  example",
                "str": "a good  example",
                "expected": "example good a"
            },
        ]

        solution = Solution()
        for testcase in test_cases:
            self.assertEqual(testcase["expected"], solution.reverseWords(testcase["str"]),
                             testcase["name"])
