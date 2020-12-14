class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """

    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return 1

        left_inc = 0
        left_dec = 0

        longest = 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                longest = max(longest, i - left_dec)
                left_dec = i
            elif A[i] < A[i - 1]:
                longest = max(longest, i - left_inc)
                left_inc = i
            else:
                left_inc = i
                left_dec = i

        longest = max(len(A) - left_dec, len(A) - left_inc, longest)

        return longest


class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """

    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0

        longest, incr, desc = 1, 1, 1

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                incr += 1
                desc = 1
            elif A[i] < A[i - 1]:
                incr = 1
                desc += 1
            else:
                incr = 1
                desc = 1

            longest = max(longest, incr, desc)

        return longest







