class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def stoneGame(self, A):
        n = len(A)
        if n < 2:
            return 0

        dp = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0

        prefixSum = [0] * (n + 1)

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + A[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + prefixSum[j + 1] - prefixSum[i])

        return dp[0][-1]
