class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        root = node
        if root is None:
            return None

        # get all nodes
        nodes = self.getnodes(node)

        # copy nodes
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        # copy neighbors
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def getnodes(self, node):
        q = collections.deque([node])
        result = set([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    q.append(neighbor)

        return result