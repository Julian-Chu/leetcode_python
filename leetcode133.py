"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0):
        self.val = val
        self.neighbors = []
"""


class Node:
    def __init__(self, val=0):
        self.val = val
        self.neighbors = []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node: 'Node', dict):
            if not node:
                return None
            if node  in dict:
                return dict[node]
            node_clone = Node(node.val)
            dict[node] = node_clone
            for n in node.neighbors:
                node_clone.neighbors.append(dfs(n, dict))
            return node_clone

        return dfs(node, {})
