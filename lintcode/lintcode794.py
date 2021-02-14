import collections


class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """

    def minMoveStep(self, init_state, final_state):
        if not init_state:
            return 0
        init = self.martixToString(init_state)
        final = self.martixToString(final_state)
        queue = collections.deque([init])

        # Memory Exceed Limit
        # visited = set([init])
        # step = -1
        # while queue:
        #     step+=1
        #     for _ in range(len(queue)):
        #         state = queue.popleft()
        #         if state == final:
        #             return step

        #         for next_state in self.get_next_states(state):
        #             if next_state in visited:
        #                 continue
        #             queue.append(next_state)
        # return -1
        distance = {init: 0}

        while queue:
            curt = queue.popleft()
            if curt == final:
                return distance[curt]

            for next in self.get_next_states(curt):
                if next in distance:
                    continue

                queue.append(next)
                distance[next] = distance[curt] + 1

        return -1

    def get_next_states(self, state):
        states = []
        zeroIndex = state.find('0')
        x = zeroIndex // 3
        y = zeroIndex % 3

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < 3 and 0 <= next_y < 3:
                nextIndex = next_x * 3 + next_y
                next_state = list(state)
                next_state[zeroIndex], next_state[nextIndex] = next_state[nextIndex], next_state[zeroIndex]
                states.append("".join(next_state))
        return states

    def martixToString(self, matrix):
        state = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                state += str(matrix[i][j])

        return state
"""
雙向BFS
"""
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """

    def minMoveStep(self, init_state, final_state):
        if not init_state:
            return 0
        init = self.martixToString(init_state)
        final = self.martixToString(final_state)
        forward_queue = collections.deque([init])
        forward_set = set([init])

        backward_queue = collections.deque([final])
        backward_set = set([final])
        step = 0

        while forward_queue and backward_queue:
            step += 1
            if self.extend_queue(forward_queue, forward_set, backward_set):
                return step
            step += 1
            if self.extend_queue(backward_queue, backward_set, forward_set):
                return step
        return -1

    def extend_queue(self, queue, visited, opposite_visited):
        for _ in range(len(queue)):
            curr = queue.popleft()
            for next in self.get_next_states(curr):
                if next in visited:
                    continue
                if next in opposite_visited:
                    return True
                queue.append(next)
                visited.add(next)

        return False

    def get_next_states(self, state):
        states = []
        zeroIndex = state.find('0')
        x = zeroIndex // 3
        y = zeroIndex % 3

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < 3 and 0 <= next_y < 3:
                nextIndex = next_x * 3 + next_y
                next_state = list(state)
                next_state[zeroIndex], next_state[nextIndex] = next_state[nextIndex], next_state[zeroIndex]
                states.append("".join(next_state))
        return states

    def martixToString(self, matrix):
        state = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                state += str(matrix[i][j])

        return state

"""
Time exceed limit
"""
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """

    def minMoveStep(self, init_state, final_state):
        key_final = self.gen_key(final_state)
        if self.gen_key(init_state) == key_final:
            return 0
        queue = collections.deque([init_state])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        move = 0
        while queue:
            move += 1
            for _ in range(len(queue)):
                state = queue.popleft()
                visited.add(self.gen_key(state))
                (x, y) = self.find_zero_index(state)
                for dx, dy in directions:
                    next_x = x + dx
                    next_y = y + dy
                    if not self.is_valid(init_state, next_x, next_y):
                        continue
                    new_state = self.copy_state(state)
                    new_state[next_x][next_y], new_state[x][y] = new_state[x][y], new_state[next_x][next_y]
                    key_new_state = self.gen_key(new_state)
                    if key_new_state in visited:
                        continue
                    if key_new_state == key_final:
                        return move

                    queue.append(new_state)
        # print(visited)
        return -1

    def is_valid(self, matrix, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

    def find_zero_index(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    return (i, j)
        return (-1, -1)

    def gen_key(self, matrix):
        return "".join([str(num) for nums in matrix for num in nums])

    def copy_state(self, matrix):
        copy = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                copy[i][j] = matrix[i][j]
        return copy