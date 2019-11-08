from unittest import TestCase


class Solution:
    def numDecodings(self, s: str) -> int:
        strVal = str(s)
        n = len(strVal)
        if n == 0:
            return 0

        bytes = [int(str.encode(e)) - int(str.encode('0')) for e in strVal]
        print(bytes)
        if bytes[0] == 0:
            return 0
        if n==1:
            return 1
        dp = [1]
        last, lastTwo = bytes[0], 0

        for i in range(1, n):
            last, lastTwo = bytes[i], last * 10 + bytes[i]
            dp.append(0)
            if last > 0:
                dp[i] += dp[i - 1]

            if 26 >= lastTwo >= 10:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]

        return dp[n - 1]


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
