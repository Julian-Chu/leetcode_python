class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """

    def permutationIndex(self, A):
        if not A:
            return 0

        factorial = 1
        res = 1
        for i in range(len(A) - 1, -1, -1):
            smaller = 0
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    smaller += 1
            res += smaller * factorial
            factorial *= (len(A) - i)
        return res
