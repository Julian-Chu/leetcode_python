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