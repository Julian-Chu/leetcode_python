"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
import collections


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        nodes_indegree = self.get_nodes_indegree(graph)

        order = []
        queue = collections.deque([node for node in nodes_indegree if nodes_indegree[node] == 0])

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                nodes_indegree[neighbor] -= 1
                if nodes_indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order

    def get_nodes_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1

        return node_to_indegree


