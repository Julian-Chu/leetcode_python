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


'''
two direction BFS
'''
from collections import deque

class Solution:
    direction = [
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1)
    ]
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """

    def shortestPath(self, grid, source, destination):
        if not grid:
            return -1
        if (source.x, source.y) == (destination.x, destination.y):
            return 0
        if grid[destination.x][destination.y] == 1:
            return -1

        forward_queue = deque([(source.x, source.y)])
        forward_set = set([(source.x, source.y)])
        backward_queue = deque([(destination.x, destination.y)])
        backward_set = set([(destination.x, destination.y)])

        distance = 0
        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(grid, forward_queue, forward_set, backward_set):
                return distance
            distance += 1
            if self.extend_queue(grid, backward_queue, backward_set, forward_set):
                return distance

        return -1

    def extend_queue(self, grid, queue, visited, opposite_visited):
        for _ in range(len(queue)):
            (x, y) = queue.popleft()
            for dx, dy in self.direction:
                next_x, next_y = x + dx, y + dy
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                if (next_x, next_y) in opposite_visited:
                    return True
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
        return False

    def is_valid(self, grid, x, y, visited):
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        if (x, y) in visited:
            return False
        if grid[x][y]:
            return False
        return True


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        if not grid:
            return -1
        n, m = len(grid), len(grid[0])
        if grid[n - 1][m - 1]:
            return -1

        forward_direction = [(1, 2), (-1, 2), (2, 1), (-2, 1)]
        backward_direction = [(1, -2), (-1, -2), (2, -1), (-2, -1)]

        forward_queue = collections.deque([(0, 0)])
        forward_set = set([(0, 0)])
        backward_queue = collections.deque([(n - 1, m - 1)])
        backward_set = set([(n - 1, m - 1)])

        distance = 0
        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(grid, forward_queue, forward_set, backward_set, forward_direction):
                return distance
            distance += 1
            if self.extend_queue(grid, backward_queue, backward_set, forward_set, backward_direction):
                return distance

        return -1

    def extend_queue(self, grid, queue, visited, opposite_visited, direction):
        for _ in range(len(queue)):
            (x, y) = queue.popleft()
            for dx, dy in direction:
                next_x, next_y = x + dx, y + dy
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                if (next_x, next_y) in opposite_visited:
                    return True
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
        return False

    def is_valid(self, grid, x, y, visited):
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        if (x, y) in visited:
            return False
        if grid[x][y]:
            return False
        return True