
""""
O(n^3)
"""
class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):

        n, m = len(matrix), len(matrix[0])

        for top in range(n):
            arr = [0] * m
            for down in range(top, n):
                prefix_sum = 0
                prefix_hash = {0 :-1}
                for col in range(m):
                    arr[col] += matrix[down][col]
                    prefix_sum += arr[col]
                    if prefix_sum in prefix_hash:
                        return [(top, prefix_hash[prefix_sum] +1), (down, col)]
                    prefix_hash[prefix_sum] = col
        return None


"""
O(n^4)
"""
class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """

    def submatrixSum(self, matrix):
        if not matrix:
            return []

        n, m = len(matrix), len(matrix[0])
        sums = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                sums[i][j] = sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1] + matrix[i - 1][j - 1]

        for row2 in range(n):
            for row1 in range(row2, n):
                for col2 in range(m):
                    for col1 in range(col2, m):
                        if self.sumRange(sums, row1, col1, row2, col2) == 0:
                            return [[row1, col1], [row2, col2]]

        return [[0, 0], [0, 0]]

    def sumRange(self, sums, row1, col1, row2, col2):
        row2 += 1
        col2 += 1
        return sums[row2][col2] - sums[row1][col2] - sums[row2][col1] + sums[row1][col1]
