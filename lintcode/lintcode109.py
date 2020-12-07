class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        self.mininum = sys.maxsize
        self.traverse(triangle, 0, 0, 0)
        return self.min_path

    def traverse(self, triangle, x, y, path_sum):
        if x == len(triangle):
            self.mininum = min(self.mininum,  path_sum)
            return

        self.traverse(triangle, x + 1, y, path_sum + triangle[x][y])
        self.traverse(triangle, x + 1, y + 1,  path_sum + triangle[x][y])


class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        res = self.divideconquer(triangle, 0, 0)
        return res

    def divideconquer(self, triangle, x, y):
        if x == len(triangle) - 1:
            return triangle[x][y]

        left = self.divideconquer(triangle, x + 1, y)
        right = self.divideconquer(triangle, x + 1, y + 1)

        return triangle[x][y] + min(left, right)


class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        res = self.divide_conquer(triangle, 0, 0, {})
        return res

    def divide_conquer(self, triangle, x, y, memo):
        if x == len(triangle) - 1:
            return triangle[x][y]

        if (x, y) in memo:
            return memo[(x, y)]

        left = self.divide_conquer(triangle, x + 1, y, memo)
        right = self.divide_conquer(triangle, x + 1, y + 1, memo)
        memo[(x, y)] = triangle[x][y] + min(left, right)
        return memo[(x, y)]