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

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)

        dp[0] = True

        for i in range(1, n+1):
            for word in wordDict:
                if i >= len(word):
                    dp[i] = dp[i] or (dp[i-len(word)] and s[(i- len(word)):i] == word)

        return dp[n]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(s: str, word_dict: set, start: int, memo: dict)->bool:
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            for end in range(start+1, len(s)+1):
                if s[start:end] in word_dict and dfs(s, word_dict, end, memo):
                    memo[start] = True
                    return memo[start]
            memo[start] = False
            return memo[start]

        return dfs(s, set(wordDict), 0, {})

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)

        for i in range(0, len(s)):
            for j in range(0, i+1):
                word = s[j:i+1]
                dp[i] = dp[i] or (word in wordDict and (j==0 or dp[j-1] == True))

        return dp[-1]