class Solution:
    """
    @param P: an integer array P
    @param Q: an integer array Q
    @param k: the number of allowed changes
    @return: return LCS with at most k changes allowed.
    """

    def longestCommonSubsequence2(self, P, Q, k):
        n, m = len(P), len(Q)
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][0], dp[i][j - 1][0])
                if P[i - 1] == Q[j - 1]:
                    dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j - 1][0] + 1)

                for u in range(1, k + 1):
                    if P[i - 1] == Q[j - 1]:
                        dp[i][j][u] = dp[i - 1][j - 1][u] + 1
                    else:
                        # num不相等:
                        # - 不變動: 繼承i-1, j, u
                        # - 不變動: 繼承 i, j-1, u
                        # - 變動: i-1, j-1, u-1

                        dp[i][j][u] = max(
                            dp[i - 1][j][u],
                            dp[i][j - 1][u],
                            dp[i - 1][j - 1][u - 1] + 1
                        )
        return dp[-1][-1][-1]
