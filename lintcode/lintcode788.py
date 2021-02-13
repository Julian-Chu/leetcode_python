class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """

    def shortestDistance(self, maze, start, destination):
        if not maze:
            return -1

        start_x = start[0]
        start_y = start[1]
        end_x = destination[0]
        end_y = destination[1]

        minDist = float('inf')
        queue = collections.deque([(start_x, start_y, 0)])

        visited = {}

        while queue:
            for _ in range(len(queue)):
                x, y, dist = queue.popleft()

                if dist > minDist:
                    continue

                if (x, y) == (end_x, end_y):
                    minDist = min(minDist, dist)

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_x = x
                    next_y = y
                    next_dist = dist
                    while self.is_valid(maze, next_x + dx, next_y + dy):
                        next_x = next_x + dx
                        next_y = next_y + dy
                        next_dist += 1
                    if next_x == x and next_y == y:
                        continue
                    if (next_x, next_y) in visited and visited[(next_x, next_y)] < next_dist:
                        continue
                    queue.append((next_x, next_y, next_dist))
                    visited[(next_x, next_y)] = next_dist

        if minDist == float('inf'):
            return -1
        return minDist

    def is_valid(self, maze, x, y):
        if not (0 <= x < len(maze) and 0 <= y < len(maze[0])):
            return False
        if maze[x][y] == 1:
            return False
        return True


"""
@param maze: the maze
@param start: the start
@param destination: the destination
@return: the shortest distance for the ball to stop at the destination
"""
import collections


def shortestDistance(self, maze, start, destination):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    x_start = start[0]
    y_start = start[1]
    x_end = destination[0]
    y_end = destination[1]
    dist = 0
    queue = collections.deque([(x_start, y_start, dist)])
    min_dist = float('inf')
    res = dict()
    # res[(x_start, y_start)] = dist
    while queue:
        print(queue)
        for _ in range(len(queue)):
            (x, y, dist) = queue.popleft()
            if dist >= min_dist:
                continue
            if (x, y) == (x_end, y_end):
                print(min_dist)
                min_dist = min(min_dist, dist)
            if (x, y) in res and dist >= res[(x, y)]:
                continue

            res[(x, y)] = dist

            for dx, dy in directions:
                cur_x, cur_y, new_dist = x, y, dist
                while self.is_valid(maze, cur_x, cur_y):
                    cur_x, cur_y = cur_x + dx, cur_y + dy
                    new_dist += 1
                cur_x -= dx
                cur_y -= dy
                new_dist -= 1

                queue.append((cur_x, cur_y, new_dist))

    return -1 if min_dist == float('inf') else min_dist


def is_valid(self, maze, x, y):
    if x < 0 or x >= len(maze):
        return False
    if y < 0 or y >= len(maze[0]):
        return False
    if maze[x][y] == 1:
        return False
    return True