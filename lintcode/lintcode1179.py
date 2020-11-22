class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """

    def findCircleNum(self, M):
        import collections
        if not M:
            return 0
        circles = 0
        n = len(M)

        for i in range(n):
            if M[i][i] == 0:
                continue
            circles += 1
            queue = collections.deque([i])
            while queue:
                for _ in range(len(queue)):
                    friend_index = queue.popleft()
                    M[friend_index][friend_index] = 0

                    for next_friend_index in range(n):
                        if M[friend_index][next_friend_index] == 1 and M[next_friend_index][next_friend_index] == 1:
                            queue.append(next_friend_index)
        return circles
