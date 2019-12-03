from unittest import TestCase


class Solution:
    def numDecodings(self, s: str) -> int:
        s = str(s)
        if not s or s[0] == '0':
            return 0
        n = len(s)

        f = (3) * [0]

        f[1] = 1
        f[0] = 1

        for i in range(2, n + 1):
            one, two = 0, 0
            if int(s[i - 2:i]) <= 26 and s[i - 2] != '0':
                two = f[(i - 2) % 3]
            if s[(i - 1)] != '0':
                one = f[(i - 1) % 3]
            f[i % 3] = one + two
        return f[n % 3]


class TestSolution(TestCase):
    def test_numDecodings(self):
        test_cases = [
            {
                "name": "12",
                "input": 12,
                "expected": 2
            },
            {
                "name": "226",
                "input": 226,
                "expected": 3
            },
            {
                "name": "100",
                "input": 100,
                "expected": 0
            },
            {
                "name": "10",
                "input": 10,
                "expected": 1
            },
            {
                "name": "1",
                "input": 1,
                "expected": 1
            },
            {
                "name": "301",
                "input": 301,
                "expected": 0
            },

        ]

        solution = Solution()
        for ts in test_cases:
            self.assertEqual(ts["expected"], solution.numDecodings(ts["input"]))
