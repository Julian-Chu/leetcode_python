class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0 for i in range(numCourses)]
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degrees[node_in] += 1

        num_choose = 0
        queue = collections.deque()

        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            num_choose += 1
            for next_course in graph[course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    queue.append(next_course)

        return num_choose == numCourses