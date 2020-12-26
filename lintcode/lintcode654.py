class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

    def multiply(self, A, B):
        rows = []
        m = len(A)
        n = len(B[0])

        for i in range(len(A)):
            row = []
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    row.append((j, A[i][j]))
            rows.append(row)

        cols = []

        for j in range(len(B[0])):
            cols.append([(i, B[i][j]) for i in range(len(B)) if B[i][j] != 0])

        matrix = [[0] * n for _ in range(m)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = self.multiply_sum_element(rows[i], cols[j])
        return matrix

    def multiply_sum_element(self, arr1, arr2):
        i, j = 0, 0
        res = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i][0] < arr2[j][0]:
                i += 1
            elif arr1[i][0] > arr2[j][0]:
                j += 1
            else:
                res += arr1[i][1] * arr2[j][1]
                i += 1
                j += 1

        return res


class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

    def multiply(self, A, B):
        n = len(A)
        m = len(A[0])
        k = len(B[0])

        C = [[0] * k for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if A[i][j] != 0:
                    for l in range(k):
                        C[i][l] += A[i][j] * B[j][l]
        return C

