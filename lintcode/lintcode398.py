"""
timeout
"""
class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def longestContinuousIncreasingSubsequence2(self, matrix):
        self.max_length = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(matrix, i, j, [[False] * len(matrix[0]) for _ in range(len(matrix))], {}, 1)
        return self.max_length

    def dfs(self, matrix, i, j, visited, memo, length):
        if self.is_no_next(matrix, i, j, visited):
            self.max_length = max(self.max_length, length)
            return

        for (dx, dy) in self.directions:
            x = i + dx
            y = j + dy
            if self.inside(x, y, matrix) == False:
                continue
            if visited[x][y] == False and matrix[x][y] > matrix[i][j]:
                visited[x][y] = True
                self.dfs(matrix, x, y, visited, memo, length + 1)
                visited[x][y] = False

    def inside(self, i, j, matrix):
        m = len(matrix)
        n = len(matrix[0])

        return i >= 0 and i < m and j >= 0 and j < n

    def is_no_next(self, matrix, i, j, visited):
        is_end = True
        for dx, dy in self.directions:
            x = i + dx
            y = j + dy
            if self.inside(x, y, matrix) == False or visited[x][y]:
                continue
            if matrix[i][j] < matrix[x][y]:
                is_end = False
                break

        return is_end


"""
dfs + memoization
最大的點return 1
回傳長度(到前一點的最長長度)+1建構 memo[(i,j)] 最大長度
"""

class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def longestContinuousIncreasingSubsequence2(self, matrix):
        if not matrix:
            return 0
        memo = {}
        longest = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                length = self.dfs(matrix, i, j, memo, 1)
                longest = max(longest, length)
        return longest

    def dfs(self, matrix, i, j, memo, length):
        if (i, j) in memo:
            return memo[(i, j)]

        longest = 1
        for (dx, dy) in self.directions:
            x = i + dx
            y = j + dy
            if self.inside(x, y, matrix) == False:
                continue
            if matrix[i][j] >= matrix[x][y]:
                continue
            longest = max(longest, self.dfs(matrix, x, y, memo, length) + 1)
        memo[(i, j)] = longest
        return longest

    def inside(self, i, j, matrix):
        m = len(matrix)
        n = len(matrix[0])

        return i >= 0 and i < m and j >= 0 and j < n

"""
dp=>將所有點依據值大小轉成一維
dp從小值排到最大值
"""

class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def longestContinuousIncreasingSubsequence2(self, matrix):
        if not matrix:
            return 0

        points = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                points.append((matrix[i][j], i, j))
        dp = {}
        points.sort()
        for point in points:
            x = point[1]
            y = point[2]
            dp[(x, y)] = 1
            for dx, dy in self.directions:
                prev_x = x + dx
                prev_y = y + dy

                if 0 <= prev_x < len(matrix) and 0 <= prev_y < len(matrix[0]):
                    if (prev_x, prev_y) in dp and matrix[prev_x][prev_y] < point[0]:
                        dp[(x, y)] = max(dp[(x, y)], dp[(prev_x, prev_y)] + 1)

        return max(dp.values())





