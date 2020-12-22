import collections


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """

    def sixDegrees(self, graph, s, t):
        g = self.construct_graph(graph)

        visited = set()
        queue = collections.deque([s.label])
        degree = -1
        while queue:
            degree += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == t.label:
                    return degree
                if node in visited:
                    continue
                visited.add(node)
                for neighbor in g[node]:
                    queue.append(neighbor)
        return -1

    def construct_graph(self, graph):
        new_graph = {}
        for root in graph:
            new_graph[root.label] = set()
            for neighbor in root.neighbors:
                new_graph[root.label].add(neighbor.label)

        return new_graph