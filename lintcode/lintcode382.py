class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        if not S:
            return 0
        S.sort()
        ans = 0
        n = len(S)

        for i in range(n):  # i is longest side
            left, right = 0, i - 1
            while left < right:
                if S[left] + S[right] > S[i]:  # all lefts to right are in answer
                    ans += right - left
                    right -= 1
                else:
                    left += 1

        return ans
