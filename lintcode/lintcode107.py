"""
dfs + memo
"""
class Solution:
    """
    @param s: A string
    @param wordSet: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, wordSet):
        if not wordSet:
            return not s
        max_length = len(max(wordSet, key=len))
        return self.dfs(s, wordSet, {}, max_length)

    def dfs(self, s, wordSet, memo, max_length):
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return True

        for i in range(1, min(max_length, len(s)) + 1):
            prefix = s[:i]
            if prefix not in wordSet:
                continue
            canBreak = self.dfs(s[i:], wordSet, memo, max_length)
            if canBreak:
                memo[s] = True
                return canBreak
        memo[s] = False
        return False


"""
dp
"""
class Solution:
    """
    @param s: A string
    @param wordSet: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, wordSet):
        if not wordSet:
            return not s
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        max_length = max([len(word) for word in wordSet])
        for i in range(n + 1):
            for l in range(1, max_length + 1):
                if i < l:
                    break
                if not dp[i - l]:
                    continue
                word = s[i - l:i]
                if word in wordSet:
                    dp[i] = True
                    break

        return dp[-1]





