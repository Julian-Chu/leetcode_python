class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: the lowest ASCII sum of deleted characters to make two strings equal
    """

    def minimumDeleteSum(self, s1, s2):

        n, m = len(s1), len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = 0
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] != s2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
                else:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[n][m]


class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: the lowest ASCII sum of deleted characters to make two strings equal
    """

    def minimumDeleteSum(self, s1, s2):

        n, m = len(s1), len(s2)

        dp = [[0] * (m + 1) for _ in range(2)]

        dp[0][0] = 0

        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, n + 1):
            dp[i % 2][0] = dp[(i - 1) % 2][0] + ord(s1[i - 1])
            for j in range(1, m + 1):
                if s1[i - 1] != s2[j - 1]:
                    dp[i % 2][j] = min(dp[(i - 1) % 2][j] + ord(s1[i - 1]), dp[i % 2][j - 1] + ord(s2[j - 1]))
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
        return dp[n % 2][m]


class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: the lowest ASCII sum of deleted characters to make two strings equal
    """

    def minimumDeleteSum(self, s1, s2):
        memo = {}
        return self.dfs(s1, 0, s2, 0, memo)

    def dfs(self, s1, s1_index, s2, s2_index, memo):
        key = (s1_index, s2_index)
        if key in memo:
            return memo[key]

        if s1_index == len(s1):
            memo[key] = sum([ord(c) for c in s2[s2_index:]])
            return memo[key]
        if s2_index == len(s2):
            memo[key] = sum([ord(c) for c in s1[s1_index:]])
            return memo[key]

        ans = float('inf')
        if s1[s1_index] == s2[s2_index]:
            ans = min(ans, self.dfs(s1, s1_index + 1, s2, s2_index + 1, memo))

        ans = min(ans, self.dfs(s1, s1_index + 1, s2, s2_index, memo) + ord(s1[s1_index]))
        ans = min(ans, self.dfs(s1, s1_index, s2, s2_index + 1, memo) + ord(s2[s2_index]))

        memo[key] = ans
        return ans
