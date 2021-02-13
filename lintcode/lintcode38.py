"""
每個cycle可以拿掉一個col或是row，最多拿掉m+n
"""
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return 0

        row, col = len(matrix), len(matrix[0])
        i, j = row - 1, 0
        count = 0
        while i >= 0 and j < col:
            if matrix[i][j] == target:
                count += 1
                i -= 1
                j += 1
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return count


"""
可以處理重複整數 like [1,1,1,1,1,1,2]
"""
class Solution:
    def searchMatrix(self, matrix, target) -> int:

        if not matrix or not matrix[0]: return 0

        m, n = len(matrix), len(matrix[0])
        i, j, num_less_or_equal = m- 1, 0, 0
        while i >= 0 and j < n:
            if matrix[i][j] <= target:
                num_less_or_equal += i + 1
                j += 1
            else:
                i -= 1

        i, j, num_greater_or_equal = 0, n - 1, 0
        while i < m and j >= 0:
            if matrix[i][j] >= target:
                num_greater_or_equal += m - i
                j -= 1
            else:
                i += 1

        return (num_less_or_equal + num_greater_or_equal) - m * n


"""
BFS  O(vertex * edge)
"""
import collections


class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return 0

        cnt = 0

        queue = collections.deque([(0, 0)])
        visited = set([(0, 0)])

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if matrix[x][y] == target:
                    cnt += 1
                    continue

                for dx, dy in [(1, 0), (0, 1)]:
                    next_x = x + dx
                    next_y = y + dy
                    if not (0 <= next_x < len(matrix) and 0 <= next_y < len(matrix[0])):
                        continue
                    if (next_x, next_y) in visited:
                        continue
                    if matrix[x][y] > target:
                        continue
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))

        return cnt