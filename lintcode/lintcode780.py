class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """

    def removeInvalidParentheses(self, s):
        res = []
        left, right = self.LeftRightCount(s)
        self.dfs(s, left, right, 0, res)
        return res

    def dfs(self, s, left, right, start, res):
        if left == 0 and right == 0:
            if self.is_valid(s):
                res.append(s)
            return

        for i in range(start, len(s)):
            if i > start and s[i - 1] == s[i]:
                continue
            if s[i] == '(' and left > 0:
                self.dfs(s[:i] + s[i + 1:], left - 1, right, i, res)
            if s[i] == ')' and right > 0:
                self.dfs(s[:i] + s[i + 1:], left, right - 1, i, res)

    def is_valid(self, s):
        left, right = self.LeftRightCount(s)
        return left == 0 and right == 0

    def LeftRightCount(self, s):
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            if ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right
