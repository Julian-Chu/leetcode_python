



"""
O(k)
"""
class NumMatrix:
    """
    @param: matrix: a 2D matrix
    """

    def __init__(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        self.prefix_sum = [[0] * (m + 1) for _ in range(n)]
        prefix_sum = self.prefix_sum
        for i in range(n):
            for j in range(1, m + 1):
                prefix_sum[i][j] = prefix_sum[i][j - 1] + matrix[i][j - 1]

        self.memo = {}

    """
    @param: row1: An integer
    @param: col1: An integer
    @param: row2: An integer
    @param: col2: An integer
    @return: An integer
    """

    def sumRegion(self, row1, col1, row2, col2):
        key = (row1, col1, row2, col2)
        if key in self.memo:
            return self.memo[key]
        total = 0
        for i in range(row1, row2 + 1):
            total += self.prefix_sum[i][col2 + 1] - self.prefix_sum[i][col1]

        self.memo[key] = total
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)