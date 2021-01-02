class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """

    def longestCommonSubsequence(self, A, B):
        if not A or not B:
            return 0

        n, m = len(A), len(B)

        dp = [[0] * (m + 1) for _ in range(2)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i % 2][j] = max(dp[i % 2][j - 1], dp[(i - 1) % 2][j])
                if A[i - 1] == B[j - 1]:
                    dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - 1] + 1)
        return dp[n % 2][m]
