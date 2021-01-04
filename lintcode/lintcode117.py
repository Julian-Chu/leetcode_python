class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """

    def jump(self, A):
        rightmost = 0
        end = 0
        step = 0
        for i in range(len(A) - 1):
            rightmost = max(rightmost, A[i] + i)

            if end == i:
                end = rightmost
                step += 1
        return step

class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """

    def jump(self, A):
        if not A:
            return 0

        n = len(A)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if A[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
                    break
        return dp[n - 1]


"""
memory limit exceed
"""
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """

    def jump(self, A):
        if not A:
            return 0

        n = len(A)
        dp = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
            if i != n - 1 and A[i] > 0:
                dp[i][i + 1] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if A[i] + i >= j:
                    dp[i][j] = 1
                    continue
                for k in range(i, j):
                    if A[k] + k >= j:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        return dp[0][n - 1]
