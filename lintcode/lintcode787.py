class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """

    def hasPath(self, maze, start, destination):
        if not maze:
            return False

        start_x, start_y = start[0], start[1]
        end_x, end_y = destination[0], destination[1]

        queue = collections.deque([(start_x, start_y, 0)])
        visited = {(start_x, start_y): 0}

        while queue:
            for _ in range(len(queue)):
                x, y, dist = queue.popleft()
                if (x, y) == (end_x, end_y):
                    return True

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_x = x
                    next_y = y
                    next_dist = dist
                    while self.isValid(maze, next_x + dx, next_y + dy):
                        next_x += dx
                        next_y += dy
                        next_dist += 1

                    if next_x == x and next_y == y:
                        continue
                    if (next_x, next_y) in visited and visited[(next_x, next_y)] <= next_dist:
                        continue
                    queue.append((next_x, next_y, next_dist))
                    visited[(next_x, next_y)] = next_dist

        return False

    def isValid(self, maze, x, y):
        if not (0 <= x < len(maze) and 0 <= y < len(maze[0])):
            return False
        if maze[x][y] == 1:
            return False
        return True