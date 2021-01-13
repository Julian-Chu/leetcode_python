class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            indegree[node_in] += 1

        queue = collections.deque()
        for node_in in range(len(indegree)):
            if indegree[node_in] == 0:
                queue.append(node_in)
        print(queue)
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for node_in in graph[node]:
                indegree[node_in] -= 1
                if indegree[node_in] == 0:
                    queue.append(node_in)
        if len(result) != numCourses:
            return []
        return result

