from typing import List
from unittest import TestCase


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict = set(wordDict)
        sizes = [len(word) for word in dict]
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n + 1):
            if not dp[i]:
                continue
            for size in sizes:
                if i + size <= n:
                    dp[i + size] = dp[i + size] or s[i:i + size] in dict

        return dp[n]


class TestSolution(TestCase):
    def test_wordBreak(self):
        test_cases = [
            {
                "name": "leetcode",
                "s": "leetcode",
                "dict": ["leet", "code"],
                "expected": True
            },
            {
                "name": "applepenapple",
                "s": "applepenapple",
                "dict": ["apple", "pen"],
                "expected": True
            },
            {
                "name": "catsandog",
                "s": "catsandog",
                "dict": ["cats", "dog", "sand", "and", "cat"],
                "expected": False
            },
        ]

        solution = Solution()
        for testcase in test_cases:
            self.assertEqual(solution.wordBreak(testcase["s"], testcase["dict"]), testcase["expected"],
                             testcase["name"])
