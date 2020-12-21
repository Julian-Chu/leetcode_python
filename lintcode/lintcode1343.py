class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return the sum of two strings
    """

    def SumofTwoStrings(self, A, B):

        index_a = len(A) - 1
        index_b = len(B) - 1
        res = ""
        while index_a >= 0 and index_b >= 0:
            a, b = int(A[index_a]), int(B[index_b])
            res = str(a + b) + res
            index_a -= 1
            index_b -= 1

        if index_a >= 0:
            a = int(A[:index_a + 1])
            res = str(a) + res
            index_a -= 1

        if index_b >= 0:
            b = int(B[:index_b + 1])
            res = str(b) + res
            index_b -= 1

        return res