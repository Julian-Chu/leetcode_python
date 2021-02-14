import collections


"""
bidirectional BFS
"""
class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """

    def sixDegrees(self, graph, s, t):
        if not graph:
            return -1
        if not s or not t:
            return -1
        if s.label == t.label:
            return 0
        new_graph = {node.label: [neighbor.label for neighbor in node.neighbors] for node in graph}

        degree = 0
        queue_forward = collections.deque([s.label])
        visited_forward = set([s.label])

        queue_backward = collections.deque([t.label])
        visited_backward = set([t.label])

        while queue_forward and queue_backward:
            degree += 1
            if self.extend_queue(queue_forward, new_graph, visited_forward, visited_backward):
                return degree
            degree += 1
            if self.extend_queue(queue_backward, new_graph, visited_backward, visited_forward):
                return degree
        return -1

    def extend_queue(self, queue, graph, visited, opposite_visited):
        for _ in range(len(queue)):
            node = queue.popleft()

            for next_node in graph[node]:
                if next_node in opposite_visited:
                    return True
                visited.add(next_node)
                queue.append(next_node)

        return False

"""
bidirectional BFS
"""
class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """

    def sixDegrees(self, graph, s, t):
        if not graph:
            return -1
        if not s or not t:
            return -1
        if s.label == t.label:
            return 0
        new_graph = {node.label: [neighbor.label for neighbor in node.neighbors] for node in graph}

        degree = 0
        queue_forward = collections.deque([s.label])
        visited_forward = set([s.label])

        queue_backward = collections.deque([t.label])
        visited_backward = set([t.label])

        while queue_forward and queue_backward:
            degree += 1
            for _ in range(len(queue_forward)):
                node = queue_forward.popleft()

                for next_node in new_graph[node]:
                    if next_node in visited_backward:
                        return degree
                    if next_node in visited_forward:
                        continue
                    visited_forward.add(next_node)
                    queue_forward.append(next_node)

            degree += 1
            for _ in range(len(queue_backward)):
                node = queue_backward.popleft()

                for next_node in new_graph[node]:
                    if next_node in visited_forward:
                        return degree
                    if next_node in visited_backward:
                        continue
                    visited_backward.add(next_node)
                    queue_backward.append(next_node)
        return -1

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