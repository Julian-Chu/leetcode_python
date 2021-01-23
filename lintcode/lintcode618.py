"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
import collections


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """

    def searchNode(self, graph, values, node, target):

        queue = collections.deque([node])
        visited = set([node])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if values[node] == target:
                    return node
                for next_node in node.neighbors:
                    if next_node not in visited:
                        queue.append(next_node)
                        visited.add(next_node)
        return None