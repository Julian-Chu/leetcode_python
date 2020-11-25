# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """

    def shortestPath(self, grid, source, destination):
        if not grid or not source or not destination:
            return -1

        if grid[source.x][source.y] == 1 or grid[destination.x][destination.y] == 1:
            return -1

        visited = set()
        visited.add((source.x, source.y))
        queue = [source]
        route = 0
        delta = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                point = queue.pop(0)
                if (point.x, point.y) == (destination.x, destination.y):
                    return route

                for delta_x, delta_y in delta:
                    next_x = point.x + delta_x
                    next_y = point.y + delta_y

                    if next_x < 0 or next_x > len(grid) - 1:
                        continue
                    if next_y < 0 or next_y > len(grid[0]) - 1:
                        continue

                    if grid[next_x][next_y] == 0 and (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        queue.append(Point(next_x, next_y))

            route += 1

        return -1


"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        import collections
        queue = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}
        DIRECTIONS = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(next_x, next_y, grid):
                    continue
                distance[(next_x, next_y)] = distance[(x, y)] + 1
                queue.append((next_x, next_y))

        return -1

    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])

        if x < 0 or x >= n or y < 0 or y >= m:
            return False

        return not grid[x][y]