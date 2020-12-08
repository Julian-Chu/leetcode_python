class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        if not A:
            return False

        # state
        dp = [False] * len(A)
        # initilaization:
        dp[0] = True
        # function
        for i in range(1, len(A)):
            for j in range(i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break

        # answer
        return dp[-1]


