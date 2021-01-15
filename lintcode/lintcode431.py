"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        parent = {node.label:node.label for node in nodes}
        for node in nodes:
            for neighbor in node.neighbors:
                root_node = self.find(parent, node.label)
                root_neighbor = self.find(parent, neighbor.label)
                if root_node != root_neighbor:
                    parent[root_neighbor] = root_node

        root_dict = {}
        for child in parent:
            root = self.find(parent, child)
            if root not in root_dict:
                root_dict[root] = []
            root_dict[root].append(child)

        ans = []
        for key in root_dict:
            ans.append(root_dict[key])

        return ans


    def find(self, parent, nodeLabel):
        path = []
        while nodeLabel != parent[nodeLabel]:
            path.append(nodeLabel)
            nodeLabel = parent[nodeLabel]

        for n in path:
            parent[n] = nodeLabel

        return nodeLabel


class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """

    def connectedSet(self, nodes):
        res = []
        visited = set()

        for node in nodes:
            if node in visited:
                continue
            connected = []
            queue = collections.deque([node])
            visited.add(node)
            while queue:
                curr = queue.popleft()
                connected.append(curr.label)
                for neightbor in curr.neighbors:
                    if neightbor not in visited:
                        queue.append(neightbor)
                        visited.add(neightbor)

            if connected:
                res.append(sorted(connected))

        return res